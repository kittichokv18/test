import streamlit as st
import pandas as pd

st.title("website Developing using python")
#st.header("website Developing using python")

st.image('img/dance.gif')

dt=pd.read_csv('data/iris.csv')

st.subheader("ข้อมูลดอกไม้ Iris")
st.write(dt.head(10))

st.subheader("สถิติข้อมูลดอกไม้ Iris")
st.write("ผลรวม")
st.write(dt.sum())  # Sum of each column
st.write("ค่าเฉลี่ย")
st.write(dt.mean())  # Mean of each column
st.write("ค่ามากที่สุด")
st.write(dt.max())  # Maximum of each column
st.write("ค่าน้อยที่สุด")
st.write(dt.min())  # Minimum of each column