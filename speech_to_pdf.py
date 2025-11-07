import sounddevice as sd
import wavio
import speech_recognition as sr
from fpdf import FPDF
print("🎤 Speak now (recording for 20 seconds)")
duration = 20  #seconds
sample_rate = 44100
audio_data = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1)
sd.wait()
wavio.write("speech.wav", audio_data, sample_rate, sampwidth=2)
r = sr.Recognizer()
with sr.AudioFile("speech.wav") as source:
    audio = r.record(source)
text = r.recognize_google(audio)
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12 )
pdf.multi_cell(0, 10, text)
pdf.output(r"D:\paython\vs code\paython project\speech_to_pdf.pdf")
print(" PDF created successfully!")
