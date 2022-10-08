import whisper
import sounddevice as sd
import soundfile as sf
import time
import os


def record_audio(replay: bool = False, duration: int = 5) -> None:
    fs = 16000  # Sample rate
    seconds = duration  # Duration of recording

    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
    print("Recording audio...")
    sd.wait()  # Wait until recording is finished
    print("Audio recording complete")
    if replay:
        print("Playing audio...")
        sd.play(myrecording, fs)
        sd.wait()
        print("Audio replay Complete")
    return sf.write('output.wav', myrecording, fs)


def convert_speech_to_text(audiofile: str = None) -> str:
    model = whisper.load_model("small")

    # record audio if none is given
    if audiofile is None:
        record_audio()
    audiofile = "output.wav" if audiofile is None else audiofile

    # load audio and pad/trim it to fit 30 seconds
    audio = whisper.load_audio(audiofile)
    # remove file audiofile
    os.remove(audiofile)
    audio = whisper.pad_or_trim(audio)

    # make log-Mel spectrogram and move to the same device as the model
    mel = whisper.log_mel_spectrogram(audio).to(model.device)

    # detect the spoken language
    _, probs = model.detect_language(mel)
    # print(f"Detected language: {max(probs, key=probs.get)}")

    # decode the audio
    options = whisper.DecodingOptions(fp16=False)
    result = whisper.decode(model, mel, options)

    # print the recognized text
    print(result.text)

    return result.text
