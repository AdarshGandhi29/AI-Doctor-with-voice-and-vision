# 🏥 AI Doctor 2.0 – Vision & Voice Based Multimodal Chatbot

A multimodal AI-powered medical chatbot that enables patients to interact using **text**, **voice**, and **medical images**. The system integrates **LLMs**, **speech models**, and **vision models** to simulate intelligent, real-time doctor consultation experiences.

---

## 🚀 Features

- 🧠 **Multimodal Inference**: Combines text, voice, and image inputs using **LLaMA 3 Vision** via **GROQ API**.
- 🎙️ **Voice Input/Output**: Enables full duplex interaction using **Whisper (STT)** and **gTTS / ElevenLabs (TTS)**.
- 🖼️ **Medical Image Understanding**: Accepts diagnostic images (e.g., X-rays) for intelligent analysis.
- 💬 **Interactive UI**: Built using **Gradio** for real-time communication and seamless UX.
- 🔄 **End-to-End Workflow**: Voice/Image → Preprocessing → LLM → Voice/Text Response.

---

## 🧠 System Architecture

- [Voice Input] → Whisper STT
- [Image Input] → Preprocessing
- [Text + Image Input] → LLaMA 3 Vision via GROQ API
- [LLM Output] → gTTS / ElevenLabs TTS
- [UI] → Gradio (real-time interaction)

---

## 🛠️ Tech Stack

- Python
- Gradio (UI)
- GROQ API (LLM inference)
- LLaMA 3 Vision (multimodal model)
- Whisper (Speech-to-Text)
- gTTS / ElevenLabs (Text-to-Speech)
- ffmpeg & portaudio (audio recording)
- PIL / ImageLib (image preprocessing)

---

## 📦 Project Structure

ai-doctor-2.0/
├── app.py # Main logic for Gradio interface
├── llm_inference.py # GROQ + LLaMA 3 Vision call logic
├── speech_utils.py # Whisper STT and TTS integration
├── image_utils.py # Image preprocessing
├── requirements.txt
└── README.md

---

## 📈 Future Improvements

- Finetune vision model on medical datasets
- Add multilingual voice/text support
- Upgrade to premium LLMs for enhanced accuracy

---

> ⚠️ Disclaimer: This project is a prototype and not intended for real-world clinical use.
