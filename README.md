
## Chatbot API: Bitnet(LLaMA.cpp) dan OpenAI GPT-3.5

### Deskripsi  
API ini memungkinkan pengguna untuk berinteraksi dengan chatbot menggunakan dua model:
1. **Bitnet(LLaMA.cpp)**  
2. **OpenAI GPT-3.5**  

API ini juga mendukung **terjemahan otomatis** untuk berbagai bahasa, termasuk bahasa Indonesia, dan menyimpan riwayat percakapan.

---

### Base URL  
```
http://<your-api-url>/
```

---

## Endpoints  

### 1. **POST /chat**  
Endpoint ini digunakan untuk berinteraksi dengan chatbot menggunakan model **Bitnet(LLaMA.cpp)**.

#### Request Body  
```json
{
  "prompt": "Your question or message",
  "max_length": 100
}
```
- **prompt** (string): Pesan atau pertanyaan yang ingin dikirim ke chatbot.  
- **max_length** (integer, optional): Panjang maksimum respons dari chatbot.  
   - **Default**: 100  
   - **Range**: 10 hingga 512  

#### Response  
```json
{
  "response": "Chatbot's generated response"
}
```

#### Penjelasan  
- Chatbot akan **mendeteksi bahasa** dari prompt dan memberikan respons yang sesuai.  
- Jika bahasa yang terdeteksi adalah **Indonesia**, prompt akan diterjemahkan ke dalam **bahasa Inggris** sebelum dikirim ke model.  
- Bahasa lain juga akan diterjemahkan ke bahasa Inggris sebelum diproses.


---

### 2. **POST /chat_openai**  
Endpoint ini digunakan untuk berinteraksi dengan chatbot menggunakan model **OpenAI GPT-3.5**.

#### Request Body  
```json
{
  "prompt": "Your question or message",
  "max_length": 100
}
```
- **prompt** (string): Pesan atau pertanyaan yang ingin dikirim ke OpenAI GPT-3.5.  
- **max_length** (integer, optional): Panjang maksimum respons dari OpenAI.  
   - **Default**: 100  
   - **Range**: 10 hingga 512  

#### Response  
```json
{
  "response": "OpenAI's generated response"
}
```

---

## Catatan Tambahan  
- **Terjemahan Otomatis**: API mendukung input dalam bahasa Indonesia dan bahasa lainnya. Prompt akan diterjemahkan ke bahasa Inggris sebelum diproses.  
- **Pemrosesan Model**:  
   - `/chat` menggunakan **LLaMA.cpp**.  
   - `/chat_openai` menggunakan **OpenAI GPT-3.5**.

---



---

# **Chatbot Multimodal (Teks & Suara)**  
Menggunakan **Whisper** dari OpenAI dan **pyttsx3**, serta **Streamlit** untuk frontend.

---

## **Deskripsi**  
Chatbot ini mendukung input teks dan suara:  
- **Speech-to-Text** (STT) menggunakan **Whisper dari OpenAI**.  
- **Text-to-Speech** (TTS) menggunakan **pyttsx3**.  
- **Frontend antarmuka** dibangun menggunakan **Streamlit**.

---

## **Dependensi**  
Untuk menjalankan proyek ini, pastikan dependensi berikut telah diinstal:  

1. **sounddevice**: Untuk merekam audio.  
2. **pyttsx3**: Untuk mengubah teks menjadi suara.  
3. **streamlit**: Untuk membuat antarmuka web.  
4. **requests**: Untuk mengirim permintaan HTTP ke API backend.  
5. **openai**: Untuk menggunakan **Whisper** (STT) dan **GPT-3.5** (chatbot).  

---

## **Fungsi Utama**  

### 1. **record_audio**  
- **Deskripsi**: Merekam audio dari pengguna dan menyimpannya sebagai file **WAV**.  

### 2. **speech_to_text**  
- **Deskripsi**: Mengonversi audio yang direkam menjadi teks menggunakan **Whisper dari OpenAI**.  

### 3. **speak**  
- **Deskripsi**: Mengonversi respons teks chatbot menjadi suara menggunakan **pyttsx3**.  

---

## **Antarmuka Streamlit**  

### **Mode Input**  
- **Teks**  
- **Suara**  

### **Endpoints**  
- `/chat`  
- `/chat_openai`  

### **Aksi Respons**  
1. Tampilkan respons chatbot di area teks.  
2. Ubah respons chatbot menjadi suara.  

---

## **Penggunaan Berdasarkan Contoh**  

### 1. **Input Teks**  
- **Deskripsi**:  
   Pengguna memasukkan teks di antarmuka, dan permintaan dikirim ke endpoint API yang dipilih.  
- **Hasil**:  
   Respons chatbot akan **ditampilkan** di area teks dan **dibacakan kembali** dengan suara.  

**Contoh Alur**:  
```
User Input: "Apa itu AI?"  
Output: "AI adalah bidang ilmu komputer yang fokus pada pembuatan mesin cerdas."  
TTS: Respons dibacakan kembali dengan suara.
```

---

### 2. **Input Suara**  
- **Deskripsi**:  
   Pengguna merekam suara, lalu suara dikonversi menjadi teks menggunakan **Whisper**. Teks hasil konversi dikirim ke backend API.  
- **Hasil**:  
   Respons chatbot akan **ditampilkan** di area teks dan **dibacakan kembali** dengan suara.  

**Contoh Alur**:  
```
User Input: (Rekaman Suara) "Apa itu AI?"  
STT: Suara dikonversi menjadi teks: "Apa itu AI?"  
Output: "AI adalah bidang ilmu komputer yang fokus pada pembuatan mesin cerdas."  
TTS: Respons dibacakan kembali dengan suara.
```

---

## **Teknologi yang Digunakan**  
- **OpenAI Whisper**: Untuk Speech-to-Text (STT).  
- **pyttsx3**: Untuk Text-to-Speech (TTS).  
- **Streamlit**: Untuk membangun antarmuka web yang interaktif.  
- **API Backend**:  
   - Endpoint `/chat`: Menggunakan **Bitnet(LLaMA.cpp)**.  
   - Endpoint `/chat_openai`: Menggunakan **OpenAI GPT-3.5**.  

---
