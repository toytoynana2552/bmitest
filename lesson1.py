import streamlit as st

import io

st.set_page_config(page_title='BODY MESS INDEX',page_icon='🦊')
st.header('หาค่า BMI')
if st.button('วิธีเพิ่มน้ำหนัก'):
   st.video('https://youtu.be/q02nagGu4bg?feature=shared')
if st.button('วิธีลดน้ำหนัก'):
   st.video('https://youtu.be/UdO8kelHy-o?feature=shared')


st.info('ผอม')
st.success('ปกติ')
st.warning('อ้วนระดับ1')
st.error('อ้วนระดับ2')
st.error('อ้วนระดับ3')
Kg=st.number_input('น้ำหนัก (Kg) :')
cm=st.number_input('ส่วนสูง (cm) :')


if st.button('คำนวณ'):
    BMI=Kg /(cm/100)**2
    tt = f' ค่า BMI ของคุณคือ {BMI:.2f}'
    if BMI < 18.5:
        st.info(tt)
        st.image('C:/aipython/BMI1.png')
        
    elif BMI < 23:
        st.success(tt)
        st.image('C:/aipython/BMI2.png')
        
    elif BMI < 30:
        st.warning(tt)
        st.image('C:/aipython/BMI3.png')
        
    elif BMI < 35:
        st.error(tt)
        st.image('C:/aipython/BMI4.png')
        
    elif BMI > 35:
        st.error(tt)
        st.image('C:/aipython/BMI5.png')
        
   

   
st.title("Botnoi Voice API Demo")

API_URL = "https://api-voice.botnoi.ai/openapi/v1/generate_audio"
API_TOKEN = "bWNCzVAFS9OwgWRPSPKKuZwBaERkh1gA"

text_input = st.text_input("ข้อความที่ต้องการแปลงเป็นเสียง", "สวัสดีครับ")
speaker_id = st.text_input("Speaker ID", "1")
generate_btn = st.button("Generate Voice")

if generate_btn:
    payload = {
        "text": text_input,
        "speaker": speaker_id,
        "volume": 1,
        "speed": 1,
        "type_media": "mp3",
        "save_file": "true",
        "language": "th",
        "page": "user"
    }

    headers = {
        "accept": "application/json",
        "Content-Type": "application/json",
        "botnoi-token": API_TOKEN
    }

    try:
        res = requests.post(API_URL, json=payload, headers=headers, timeout=30)
        res.raise_for_status()
        data = res.json()
        st.write("API Response:", data)

        # ดึง URL ไฟล์เสียง
        audio_url = (
            data.get("url")
            or data.get("audio_url")
            or (data.get("data") or {}).get("url")
        )

        if audio_url:
            audio_bytes = requests.get(audio_url, timeout=30).content
            out_path = Path("botnoi_voice.mp3")
            out_path.write_bytes(audio_bytes)
            st.success(f"✅ บันทึกเสียงเรียบร้อย → {out_path.resolve()}")
            st.audio(audio_bytes, format="audio/mp3")
        else:
            st.error("ไม่พบลิงก์ไฟล์เสียงใน response")

    except Exception as e:
        st.error(f"เกิดข้อผิดพลาด: {e}")
