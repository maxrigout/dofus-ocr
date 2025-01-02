# Dofus OCR

This open-source, free app aims at bridging the language barrier inherent to the vast majority of Dofus players being French by providing a real-time translater for in-and-outbound messaging. If you feel a feature would be helpful, feel free to request it or make a pull request. Any help maintaining and growing this project is most welcome.

# Installation

## Executable

If you wish, you may find the latest executable directly under [releases](https://github.com/Eliott-Mischler/dofus-ocr/releases), note that this is inherently unsafe, and I do not recommend it. 

This executable requires no extra steps to run on a Windows machine. 

## Run (Windows instructions)

Below are the steps to running this app yourself without downloading an executable.

### 1. Install python 3.12.2
   Head over to [Python's 3.12.2 release](https://www.python.org/downloads/release/python-3122/) and install it using the installer befitting your machine.
### 2. Install Tesseract
   On windows, you need to head over here: [https://github.com/UB-Mannheim/tesseract/wiki](https://github.com/UB-Mannheim/tesseract/wiki).\
   On other platforms, you can refer to this page: [https://tesseract-ocr.github.io/tessdoc/Installation.html](https://tesseract-ocr.github.io/tessdoc/Installation.html).
### 3. Add python and Tesseract to your PATH
   This is explained in many places, and if you're tech savvy you likely already know how to do this, if not, refer to [this article](https://realpython.com/add-python-to-path/).\
   In a similar fashion, add Tesseract to your PATH. If you opted to install Tesseract for all Users on Windows, then it'll most likely be located at `C:\Program Files\Tesseract-OCR`.
### 4. Clone this repo
   The simplest way to do this if you aren't a developer is to simply click the green "Code" button and choose to download this repository as a zip-file. Once done, extract it someplace you'd like to keep it. 

   
   Then, in your command prompt, navigate to that folder, and execute the following command : `py -m venv venv` to create a virtual environment inside a `.\venv` folder.
### 5. Enter the environment, and run the app
   Now, still in the same command line interface, run `.\venv\Scripts\activate` to enter the virtual environment. Within this environment, run `pip install -r .\requirements.txt`. 

   Then, once that is done, you may now run `py .\dofus_ocr_app.py`. This will execute the app, and each time you wish to run it again, you must run `.\venv\Scripts\activate` followed by  `py .\dofus_ocr_app.py` from the root folder of the extracted zip file.
   
