import whisper
from googletrans import Translator
from gtts import gTTS
from playsound import playsound

model = whisper.load_model("large")
audio = "test1.mp3"
transcribe = model.transcribe(audio)
print(transcribe["text"])
transcribed_text = transcribe["text"]
print("   ")
print("**********Translate Audio*******")
translator = Translator()
language = "en"
translated_text = translator.translate(transcribed_text, dest=language)
print(translated_text.text)
tts = gTTS(translated_text.text, lang=language, slow=False)
tts.save("outputaudio.mp3")
playsound("outputaudio.mp3")
