
## Chatbot API: LLaMA.cpp dan OpenAI GPT-3.5

### Deskripsi  
API ini memungkinkan pengguna untuk berinteraksi dengan chatbot menggunakan dua model:
1. **LLaMA.cpp**  
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
Endpoint ini digunakan untuk berinteraksi dengan chatbot menggunakan model **LLaMA.cpp**.

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
