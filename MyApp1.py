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
cl1,cl2,cl3,cl4=st.columns(4)
cl1.write("ผลรวม")
cl1.write(dt['sepal.length'].sum())

cl2.write("ผลรวม")
cl2.write(dt['sepal.width'].sum())

cl3.write("ผลรวม")
cl3.write(dt['petal.length'].sum())

cl4.write("ผลรวม")
cl4.write(dt['petal.width'].sum())
