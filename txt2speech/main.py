import pyttsx3


def convert_text_to_speech(text: str, title:str, rt: int = 150, vlm: float = 1.0, vc: int = 1):
    engine = pyttsx3.init()  # object creation
    """ RATE"""
    rate = engine.getProperty('rate')   # getting details of current speaking rate
    engine.setProperty('rate', rt)     # setting up new voice rate
    """VOLUME"""
    volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
    engine.setProperty('volume',vlm)    # setting up volume level  between 0 and 1
    """VOICE"""
    voices = engine.getProperty('voices')       #getting details of current voice
    engine.setProperty('voice', voices[vc].id)   #changing index, changes voices. 1 for female
    """Saving Voice to a file"""
    engine.save_to_file(text, f'{title}.mp3')
    engine.runAndWait()