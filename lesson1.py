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
        word='ผอม'
    elif BMI < 23:
        st.success(tt)
        st.image('C:/aipython/BMI2.png')
         word='ปกติ'
    elif BMI < 30:
        st.warning(tt)
        st.image('C:/aipython/BMI3.png')
         word='อ้วนระดับ1'
    elif BMI < 35:
        st.error(tt)
        st.image('C:/aipython/BMI4.png')
         word='อ้วนระดับ2'
    elif BMI > 35:
        st.error(tt)
        st.image('C:/aipython/BMI5.png')
         word='อ้วนระดับ3'
   
