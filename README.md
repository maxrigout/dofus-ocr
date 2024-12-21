# Dofus OCR

This open-source, free app aims at bridging the language barrier inherent to the vast majority of Dofus players being French by providing a real-time translater for in-and-outbound messaging. If you feel a feature would be helpful, feel free to request it or make a pull request. Any help maintaining and growing this project is most welcome.

# Installation

## Executable

If you wish, you may find an executable directly under `releases`, note that this is inherently unsafe, and I do not recommend it. 

## Run (Windows instructions)

Below are the steps to running this app yourself without downloading an executable.

### 1. Install python 3.12.2
   Head over to [Python's 3.12.2 release](https://www.python.org/downloads/release/python-3122/) and install it using the installer befitting your machine.
### 2. Add python to your PATH
   This is explained in many places, and if you're tech savvy you likely already know how to do this, if not, refer to [this article](https://realpython.com/add-python-to-path/).
### 3. Clone this repo
   The simplest way to do this if you aren't a developer is to simply click the green "Code" button and choose to download this repository as a zip-file. Once done, extract it someplace you'd like to keep it. 
   
   Then, in your command prompt, navigate to that folder, and execute the following command : `py -m venv venv` to create a virtual environment inside a `.\venv` folder.
### 4. Enter the environment, and run the app
   Now, still in the same command line interface, run `.\venv\Scripts\activate` to enter the virtual environment. Within this environment, run `pip install -r .\requirements.txt`. 

   Then, once that is done, you may now run `py .\dofus_ocr_app.py`. This will execute the app, and each time you wish to run it again, you must run `.\venv\Scripts\activate` followed by  `py .\dofus_ocr_app.py` from the root folder of the extracted zip file.
   
