import sys
sys.dont_write_bytecode = True

import os
import logging
import shutil
import speech_recognition as sr  # type: ignore
from pydub import AudioSegment  # type: ignore
from io import BytesIO
from groq import Groq  # type: ignore

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
stt_model = "whisper-large-v3"

def record_audio(file_path, timeout=20, phrase_time_limit=None):
    """Record audio from the microphone and save it as an MP3 file."""
    recognizer = sr.Recognizer()
    
    try:
        with sr.Microphone() as source:
            logging.info("Adjusting for ambient noise...")
            recognizer.adjust_for_ambient_noise(source, duration=1)
            logging.info("Start speaking now...")
            
            audio_data = recognizer.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
            logging.info("Recording complete.")
            
            wav_data = audio_data.get_wav_data()
            audio_segment = AudioSegment.from_wav(BytesIO(wav_data))
            audio_segment.export(file_path, format="mp3", bitrate="128k")
            
            logging.info(f"Audio saved to {file_path}")
    except Exception as e:
        logging.error(f"An error occurred: {e}")

def transcribe_with_groq(stt_model, audio_filepath, GROQ_API_KEY):
    """Transcribe audio using Groq's Whisper model."""
    if not GROQ_API_KEY:
        raise ValueError("GROQ_API_KEY is not set. Please check your environment variables.")
    
    client = Groq(api_key=GROQ_API_KEY)
    
    with open(audio_filepath, "rb") as audio_file:
        transcription = client.audio.transcriptions.create(
            model=stt_model,
            file=audio_file,
            language="en"
        )
    
    logging.info("Transcription:")
    logging.info(transcription.text)
    return transcription.text

if __name__ == "__main__":
    audio_filepath = "patient_voice_test_for_patient.mp3"
    record_audio(file_path=audio_filepath)
    transcribed_text = transcribe_with_groq(stt_model, audio_filepath, GROQ_API_KEY)
    logging.info(f"Final Transcribed Text: {transcribed_text}")
    
    # Cleanup __pycache__ folder if exists
    shutil.rmtree("__pycache__", ignore_errors=True)