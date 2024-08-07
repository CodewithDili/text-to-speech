try:
    from gtts import gTTS
    print("gTTS is installed correctly.")
except ImportError as e:
    print("gTTS is not installed.")
    print(e)
