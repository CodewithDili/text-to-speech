# Text-to-Speech Converter

A simple Python script to convert text to speech using the Google Text-to-Speech (gTTS) API and play the audio using pydub.

## Features

- Converts input text to speech.
- Supports multiple languages.
- Plays the generated speech audio.

## Requirements

- Python 3.x
- `gtts` library
- `pydub` library
- `simpleaudio` library
- `ffmpeg` (required by pydub for audio playback)

## Setup

1. **Clone the repository:**

    ```bash
    git clone https://github.com/CodewithDili/text-to-speech-converter.git
    cd text-to-speech-converter
    ```

2. **Upgrade pip:**

    ```bash
    python -m pip install --upgrade pip
    ```

3. **Install required libraries:**

    ```bash
    pip install gtts pydub simpleaudio
    ```

4. **Install ffmpeg:**

    - Download and install `ffmpeg` from [here](https://ffmpeg.org/download.html).
    - Ensure `ffmpeg` is in your system's PATH.

## Usage

1. **Run the script:**

    ```bash
    python text_to_speech.py
    ```

2. **Follow the prompts:**

    - Enter the text you want to convert to speech.
    - Enter the language code (e.g., 'en' for English, 'es' for Spanish).

## Script

```python
from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play
import os

def text_to_speech(text, lang='en'):
    """
    Converts text to speech using gTTS and plays the audio using pydub.

    Parameters:
        text (str): The text to convert to speech.
        lang (str): The language in which the text should be spoken. Default is English ('en').

    Returns:
        None
    """
    tts = gTTS(text=text, lang=lang)
    audio_file = "speech.mp3"
    tts.save(audio_file)

    # Play the audio file using pydub
    audio = AudioSegment.from_file(audio_file)
    play(audio)

    # Remove the audio file after playing it
    os.remove(audio_file)

if __name__ == "__main__":
    text = input("Enter the text you want to convert to speech: ")
    language = input("Enter the language (default is 'en' for English): ").strip() or 'en'
    try:
        text_to_speech(text, language)
    except Exception as e:
        print(f"Error: {e}")
License
This project is licensed under the MIT License. See the LICENSE file for details.

Contributing
Fork the repository.
Create your feature branch (git checkout -b feature/fooBar).
Commit your changes (git commit -am 'Add some fooBar').
Push to the branch (git push origin feature/fooBar).
Create a new Pull Request.

Acknowledgements
Google Text-to-Speech API (gTTS)
pydub
ffmpeg


### Instructions to Add the README.md File to Your Repository

1. **Create the README.md file:**

    - Open a text editor and paste the content above.
    - Save the file as `README.md` in your project directory.

2. **Add the README.md file to the repository:**

    ```bash
    git add README.md
    git commit -m "Add README.md file"
    git push origin main
    ```








