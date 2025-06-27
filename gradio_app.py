import sys
sys.dont_write_bytecode = True

import os
import shutil
import gradio as gr  # type: ignore
from dotenv import load_dotenv # type: ignore

from brain_of_the_doctor import encode_image, analyze_image_with_query
from voice_of_the_patient import transcribe_with_groq
from voice_of_the_doctor import text_to_speech_with_elevenlabs

# Load environment variables
load_dotenv()
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")

system_prompt = """You have to act as a professional doctor, I know you are not, but this is for learning purposes. 
What's in this image? Do you find anything wrong medically? 
If you make a differential, suggest some remedies for them. Do not add any numbers or special characters in 
your response. Your response should be in one long paragraph. Also, always answer as if you are answering a real person.
Do not say 'In the image I see' but 'With what I see, I think you have ....'
Don't respond as an AI model in markdown, your answer should mimic an actual doctor, not an AI bot. 
Keep your answer concise (max 2 sentences). No preamble, start your answer right away please."""


def process_inputs(audio_filepath, image_filepath):
    if not audio_filepath:
        return "No audio provided", "No image provided", None

    speech_to_text_output = transcribe_with_groq(
        GROQ_API_KEY=GROQ_API_KEY, 
        audio_filepath=audio_filepath, 
        stt_model="whisper-large-v3"
    )

    # Handle the image input
    if image_filepath:
        encoded_image = encode_image(image_filepath)
        doctor_response = analyze_image_with_query(
            query=system_prompt + " " + speech_to_text_output, 
            encoded_image=encoded_image, 
<<<<<<< HEAD
            model="meta-llama/llama-4-scout-17b-16e-instruct"
=======
<<<<<<< HEAD
            model="meta-llama/llama-4-scout-17b-16e-instruct"
=======
            model="llama-3.2-11b-vision-preview"
>>>>>>> 2601419a19a234a7f4f280fbc874a0a3702c70b1
>>>>>>> ab021e72601bc7d175a1836aea1a7b9601cf9d9d
        )
    else:
        doctor_response = "No image provided for analysis."

    voice_of_doctor = text_to_speech_with_elevenlabs(
        input_text=doctor_response, 
        output_filepath="final.mp3"
    )

    return speech_to_text_output, doctor_response, "final.mp3"  # Ensure output file matches


# Create the Gradio interface
iface = gr.Interface(
    fn=process_inputs,
    inputs=[
        gr.Audio(sources=["microphone"], type="filepath"),
        gr.Image(type="filepath")
    ],
    outputs=[
        gr.Textbox(label="Speech to Text"),
        gr.Textbox(label="Doctor's Response"),
        gr.Audio("final.mp3")  # Fixed filename
    ],
    title="AI Doctor with Vision and Voice"
)

iface.launch(debug=True)


shutil.rmtree('__pycache__', ignore_errors=True)