from gtts import gTTS
import playsound
import os

def text_to_speech(text, lang='en'):
    """
    Converts text to speech using gTTS and plays the audio.

    Parameters:
        text (str): The text to convert to speech.
        lang (str): The language in which the text should be spoken. Default is English ('en').

    Returns:
        None
    """
    tts = gTTS(text=text, lang=lang)
    audio_file = "speech.mp3"
    tts.save(audio_file)
    playsound.playsound(audio_file)
    os.remove(audio_file)

if __name__ == "__main__":
    text = input("Enter the text you want to convert to speech: ")
    language = input("Enter the language (default is 'en' for English): ").strip() or 'en'
    try:
        text_to_speech(text, language)
    except Exception as e:
        print(f"Error: {e}")
