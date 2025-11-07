from pathlib import Path
from PyPDF2 import PdfReader
from gtts import gTTS

pdf_path = Path(r"D:\paython\vs code\paython project\sample.pdf.pdf")
if not pdf_path.exists():
    print("ERROR: PDF file not found:", pdf_path)
    raise SystemExit

reader = PdfReader(str(pdf_path))
text = ""
for page in reader.pages:
    page_text = page.extract_text()
    if page_text:
        text += page_text + "\n"

if text.strip() == "":
    print("No text found in PDF.")
else:
    tts = gTTS(text)
    tts.save("audiobook.mp3")
    print("Audiobook created successfully: audiobook.mp3")
