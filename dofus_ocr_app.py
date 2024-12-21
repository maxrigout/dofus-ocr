import tkinter as tk
from tkinter import ttk
from pynput import mouse
from PIL import ImageGrab
import pytesseract
from googletrans import Translator
import pyperclip
import threading
import time

class BoundingBoxManager:
    def __init__(self):
        self.bounding_box = []
        self.bounding_box_set = False
        self.listener_thread = None
        self.listener = None

    def on_click(self, x, y, _, pressed):
        if pressed:
            print(f"Mouse pressed at: ({x}, {y})")
            self.bounding_box.append((x, y))
            if len(self.bounding_box) == 2:
                print("Both points captured.")
                self.update_ui_with_bounding_box()
                self.listener.stop()

    def update_ui_with_bounding_box(self):
        print(f"Bounding box set: {self.bounding_box}")
        self.bounding_box_set = True

    def set_bounding_box(self):
        self.bounding_box = []
        self.bounding_box_set = False

        def start_listener():
            print("Click two points to set the bounding box...")
            try:
                self.listener = mouse.Listener(on_click=self.on_click)
                self.listener.start()
                self.listener.join()
            except Exception as e:
                print(f"Error with listener: {e}")

        self.listener_thread = threading.Thread(target=start_listener, daemon=True)
        self.listener_thread.start()

class OCRManager:
    def __init__(self, bounding_box_manager):
        self.bounding_box_manager = bounding_box_manager
        self.polling = False
        self.translator = Translator(service_urls=['translate.googleapis.com'])

    def capture_and_ocr(self):
        if len(self.bounding_box_manager.bounding_box) == 2:
            try:
                top_left = self.bounding_box_manager.bounding_box[0]
                bottom_right = self.bounding_box_manager.bounding_box[1]
                bbox = (top_left[0], top_left[1], bottom_right[0], bottom_right[1])

                image = ImageGrab.grab(bbox=bbox)
                text = pytesseract.image_to_string(image)
                return text
            except Exception as e:
                print(f"Error during OCR capture: {e}")
                return ""
        else:
            print("Bounding box not set!")
            return ""

    def translate_text(self, text, src_lang, tgt_lang):
        try:
            translation = self.translator.translate(text, src=src_lang, dest=tgt_lang)
            return translation.text
        except Exception as e:
            print(f"Translation error: {e}")
            return ""

    def start_ocr_polling(self):
        if not self.bounding_box_manager.bounding_box_set:
            print("Bounding box not set!")
            return

        self.polling = True

        def poll():
            while self.polling:
                try:
                    text = self.capture_and_ocr()
                    if text:
                        translated_text = self.translate_text(text, source_language, target_language)
                        chat_box.delete('1.0', 'end')
                        chat_box.insert('end', f"{translated_text}\n")
                        chat_box.see('end')
                    time.sleep(3)
                except Exception as e:
                    print(f"Error during OCR polling: {e}")

        thread = threading.Thread(target=poll, daemon=True)
        thread.start()

    def stop_ocr_polling(self):
        self.polling = False

# Initialize managers
bounding_box_manager = BoundingBoxManager()
ocr_manager = OCRManager(bounding_box_manager)

# Create the UI
root = tk.Tk()
root.title("Chat Translation App")

# Language Selection
ttk.Label(root, text="Source Language").grid(row=0, column=0)
source_language_dropdown = ttk.Combobox(root, values=["en", "es", "fr", "de"])
source_language_dropdown.set("en")
source_language_dropdown.grid(row=0, column=1)

def update_source_language(event):
    global source_language
    source_language = source_language_dropdown.get()

source_language_dropdown.bind("<<ComboboxSelected>>", update_source_language)

ttk.Label(root, text="Target Language").grid(row=1, column=0)
target_language_dropdown = ttk.Combobox(root, values=["en", "es", "fr", "de"])
target_language_dropdown.set("es")
target_language_dropdown.grid(row=1, column=1)

def update_target_language(event):
    global target_language
    target_language = target_language_dropdown.get()

target_language_dropdown.bind("<<ComboboxSelected>>", update_target_language)

# Buttons
ttk.Button(root, text="Set Bounding Box", command=bounding_box_manager.set_bounding_box).grid(row=2, column=0, columnspan=2, pady=5)
ttk.Button(root, text="Start OCR", command=ocr_manager.start_ocr_polling).grid(row=3, column=0, pady=5)
ttk.Button(root, text="Stop OCR", command=ocr_manager.stop_ocr_polling).grid(row=3, column=1, pady=5)


# Chat Box
ttk.Label(root, text="Translated Content").grid(row=4, column=0)
chat_box = tk.Text(root, height=20, width=100)
chat_box.grid(row=4, column=1, columnspan=2, pady=5)

# User Input
ttk.Label(root, text="Write message").grid(row=5, column=0)
user_input_field = tk.Entry(root, width=40)
user_input_field.grid(row=5, column=1, pady=5)

def copy_translated_message():
    user_message = user_input_field.get()
    if user_message:
        translated_message = ocr_manager.translate_text(user_message, target_language, source_language)
        pyperclip.copy(translated_message)
        print(f"Translated message copied: {translated_message}")

ttk.Button(root, text="Copy Translated", command=copy_translated_message).grid(row=7, column=1, pady=5)

root.mainloop()