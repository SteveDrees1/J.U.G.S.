# J.U.G.S.

This project is a voice recognition system that uses the **Google Cloud Speech API** for online speech recognition and **PocketSphinx** for offline recognition.
It listens for voice commands and can execute certain tasks like turning lights on or off.
The system can recognize an "exit" command to stop listening and say "Goodbye" before exiting the program.

## Features
- **Google Cloud Speech API**: Performs online speech recognition using Google's powerful cloud-based service.
- **PocketSphinx**: Provides offline speech recognition, making the system functional even without internet access.
- **Text-to-Speech (TTS)**: The system uses TTS to respond verbally, such as saying "Goodbye" when exiting.
- **Custom Commands**: The system can be customized to respond to various voice commands like turning on/off lights or executing other tasks.

## Prerequisites

To set up this project, ensure you have the following installed on your system:

1. **Python 3.x**
2. **pip** (Python package manager)

## Installation

### Step 1: Clone the Repository
First, clone this repository to your local machine:

```bash
git clone https://github.com/your-username/voice-recognition-system.git
cd voice-recognition-system
```

### Step 2: Set Up a Virtual Environment (Optional but Recommended)
It is recommended to use a virtual environment to avoid conflicts with system-wide packages.

1. **Create a virtual environment**:

   - On **macOS/Linux**:
     ```bash
     python3 -m venv .venv
     ```

   - On **Windows**:
     ```bash
     python -m venv .venv
     ```

2. **Activate the virtual environment**:

   - On **macOS/Linux**:
     ```bash
     source .venv/bin/activate
     ```

   - On **Windows**:
     ```bash
     .venv\Scripts\activate
     ```

   Once activated, you should see the virtual environment name `(venv)` in your terminal.

### Step 3: Install Required Python Packages
Install the necessary Python libraries using `pip`:

```bash
pip install -r requirements.txt
```
If you don’t have a requirements.txt file, manually install the essential libraries by running:

```bash
pip install google-cloud-speech pocketsphinx pyttsx3
```
- **google-cloud-speech**: Used for online speech recognition.
- **pocketsphinx**: Provides offline speech recognition.
- **pyttsx3**: Enables text-to-speech functionality for speaking responses.
- The code includes installation instructions for both using a `requirements.txt` file and manual installation with `pip`.

Ensure that all these libraries are installed successfully before proceeding to the next step

### Step 4: Set Up Google Cloud Speech API

To use the **Google Cloud Speech-to-Text API**,
follow these steps to configure your Google Cloud project and set up authentication:

1. **Create a Google Cloud Project**:

   - Go to the [Google Cloud Console](https://console.cloud.google.com/).
   - Create a new project or select an existing one.


2. **Enable the Speech-to-Text API**:

   - In your Google Cloud project, navigate to the **API & Services** section.
   - Search for **Speech-to-Text API** and enable it for your project.


3. **Download the Credentials JSON File**:

   - Create a service account for your project.
   - Download the service account credentials file as a JSON file and save it somewhere secure.


4. **Set the `GOOGLE_APPLICATION_CREDENTIALS` Environment Variable**:

   You need to set the `GOOGLE_APPLICATION_CREDENTIALS` environment variable to the path of your downloaded credentials file.
   This allows the program to authenticate with the Google Cloud API.

   - On **macOS/Linux**, run this command in your terminal:
     ```bash
     export GOOGLE_APPLICATION_CREDENTIALS="/path/to/your/credentials.json"
     ```

   - On **Windows**, use this command:
     ```bash
     set GOOGLE_APPLICATION_CREDENTIALS="C:\path\to\your\credentials.json"
     ```

   Replace `/path/to/your/credentials.json` or `C:\path\to\your\credentials.json` with the actual path to your Google Cloud credentials file.


5. **Verify the Environment Variable** (Optional):

   You can verify that the environment variable is set correctly by running the following command:

   - On **macOS/Linux**:
     ```bash
     echo $GOOGLE_APPLICATION_CREDENTIALS
     ```

   - On **Windows**:
     ```bash
     echo %GOOGLE_APPLICATION_CREDENTIALS%
     ```

   This should print the path to your credential file.
   If it doesn’t, double-check the file path and ensure you run the correct command to set the environment variable.

Once you’ve completed these steps, your Google Cloud Speech API should be ready to use for online speech recognition.

### Step 5: Install PocketSphinx (Offline Speech Recognition)

PocketSphinx is used for offline speech recognition,
enabling the system to function even without an internet connection.
To install PocketSphinx, run the following command:

```bash
pip install pocketsphinx
```

Ensure that PocketSphinx is installed successfully before proceeding.
If any issues arise, you may need to troubleshoot depending on your operating system.

### Step 6: Run the Program
after all dependencies are installed and the Google Cloud Speech API is set up,
you can run the program with the following command:

```bash
python main.py
```

The program will begin listening for voice commands.
It will use the Google Cloud Speech API if internet connectivity is available,
and it will fall back to PocketSphinx for offline speech recognition if not.

When you say the command "exit," the program will respond with "Goodbye" and then exit gracefully.

## Troubleshooting

### 1. **Google Cloud Speech API Issues**

If you are encountering issues with the **Google Cloud Speech API**, here are a few things to check:

- **Google Cloud Credentials**: Ensure that the `GOOGLE_APPLICATION_CREDENTIALS` environment variable is correctly set. You can check this by running:

  - On **macOS/Linux**:
    ```bash
    echo $GOOGLE_APPLICATION_CREDENTIALS
    ```

  - On **Windows**:
    ```bash
    echo %GOOGLE_APPLICATION_CREDENTIALS%
    ```

  This should print the path to your credential file.
  If it does not, re-check the path and ensure the environment variable is set correctly.

- **API is Enabled**: Ensure that the **Speech-to-Text API** is enabled in your Google Cloud project. You can verify this in the [Google Cloud Console](https://console.cloud.google.com/).

- **Network Issues**: If the API is enabled but requests are still failing, make sure your network connection is stable. The Google Cloud Speech API requires an active internet connection to function.

### 2. **PocketSphinx Issues**

- **If PocketSphinx isn't working**: If PocketSphinx isn't recognizing your speech correctly, ensure your environment is quiet to avoid background noise interference.

- **Confirm the Pocket sphinx is installed**: run pip list and check for pocketsphinx in the output.


## License

This project is licensed under the **MIT License**.
This means that you are free to use, modify,
and distribute this project in both personal and commercial applications,
as long as you include the original copyright notice.

MIT License

Copyright © 2024 Steve Drees

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
 with the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or significant portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS," WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
