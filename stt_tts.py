import os
import queue
import sounddevice as sd
import wave
import json
import pyttsx3
import streamlit as st
import requests
import openai

# Set API Key untuk OpenAI
openai.api_key = "your-openai-key"

# Fungsi: Simpan audio yang direkam menjadi file WAV
def record_audio(filename, duration=5, samplerate=16000):
    print("Merekam audio...")
    audio_data = sd.rec(int(samplerate * duration), samplerate=samplerate, channels=1, dtype='int16')
    sd.wait()  # Tunggu hingga rekaman selesai
    with wave.open(filename, 'wb') as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)  # 16-bit audio
        wf.setframerate(samplerate)
        wf.writeframes(audio_data.tobytes())
    print("Rekaman selesai.")

# Fungsi: STT menggunakan OpenAI Whisper
def speech_to_text(audio_file):
    with open(audio_file, 'rb') as f:
        response = openai.Audio.transcribe("whisper-1", f)
    return response['text']

# Fungsi: TTS menggunakan pyttsx3
def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  # Kecepatan bicara
    engine.say(text)
    engine.runAndWait()

# Streamlit Interface
API_URL = "http://127.0.0.1:8000"

st.title("Chatbot Multimodal (Teks & Suara)")

# Pilih endpoint
endpoint_choice = st.radio("Pilih endpoint:", ("/chat_openai", "/chat"))

# Pilih metode input
input_mode = st.radio("Pilih metode input:", ("Teks", "Suara"))

if input_mode == "Teks":
    user_text = st.text_input("Masukkan teks:")
    if st.button("Kirim"):
        if user_text.strip():
            # Kirim permintaan ke endpoint yang dipilih
            response = requests.post(f"{API_URL}{endpoint_choice}", json={"prompt": user_text, "max_length": 100})
            if response.status_code == 200:
                bot_response = response.json().get("response", "Tidak ada respons.")
                st.text_area("Respons Chatbot:", bot_response, height=150)
                speak(bot_response)  # TTS untuk respons chatbot
            else:
                st.error("Gagal menghubungi server.")
        else:
            st.warning("Teks tidak boleh kosong!")

elif input_mode == "Suara":
    if st.button("Mulai Rekaman"):
        st.info("Sedang merekam suara...")
        audio_file = "input_audio.wav"
        record_audio(audio_file)

        st.info("Mengonversi suara ke teks...")
        try:
            input_text = speech_to_text(audio_file)
            st.write(f"Input Suara ke Teks: {input_text}")

            # Kirim permintaan ke endpoint yang dipilih
            response = requests.post(f"{API_URL}{endpoint_choice}", json={"prompt": input_text, "max_length": 100})
            if response.status_code == 200:
                bot_response = response.json().get("response", "Tidak ada respons.")
                st.text_area("Respons Chatbot:", bot_response, height=150)
                speak(bot_response)  # TTS untuk respons chatbot
            else:
                st.error("Gagal menghubungi server.")
        except Exception as e:
            st.error(f"Terjadi kesalahan: {e}")
