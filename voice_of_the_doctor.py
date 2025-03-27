import sys
sys.dont_write_bytecode = True

import os
import platform
import subprocess
import shutil
from gtts import gTTS  # type: ignore
import elevenlabs  # type: ignore
from elevenlabs.client import ElevenLabs  # type: ignore

# Load API Key from environment variable
ELEVENLABS_API_KEY = os.environ.get("ELEVENLABS_API_KEY")


def text_to_speech_with_gtts(input_text, output_filepath):
    """Convert text to speech using gTTS and save the output."""
    language = "en"
    audioobj = gTTS(text=input_text, lang=language, slow=False)
    audioobj.save(output_filepath)
    play_audio(output_filepath)


def text_to_speech_with_elevenlabs(input_text, output_filepath):
    """Convert text to speech using ElevenLabs API and save the output."""
    client = ElevenLabs(api_key=ELEVENLABS_API_KEY)
    audio = client.generate(
        text=input_text,
        voice="Aria",
        output_format="mp3_22050_32",
        model="eleven_turbo_v2"
    )
    elevenlabs.save(audio, output_filepath)
    play_audio(output_filepath)


def play_audio(output_filepath):
    """Play the generated audio file based on the operating system."""
    os_name = platform.system()
    try:
        if os_name == "Darwin":  # macOS
            subprocess.run(["afplay", output_filepath])
        elif os_name == "Windows":  # Windows
            subprocess.run(["cmd", "/c", "start", "wmplayer", output_filepath], shell=True)
        elif os_name == "Linux":  # Linux
            subprocess.run(["aplay", output_filepath])  # Alternative: use 'mpg123' or 'ffplay'
        else:
            raise OSError("Unsupported operating system")
    except Exception as e:
        print(f"An error occurred while trying to play the audio: {e}")


if __name__ == "__main__":
    # Test cases
    input_text = "Hi this is AI with Adarsh, autoplay testing!"
    text_to_speech_with_gtts(input_text, output_filepath="gtts_testing_autoplay.mp3")
    text_to_speech_with_elevenlabs(input_text, output_filepath="elevenlabs_testing_autoplay.mp3")
    
    # Cleanup __pycache__ folder if exists
    shutil.rmtree("__pycache__", ignore_errors=True)