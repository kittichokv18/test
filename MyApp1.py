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
cl1.write("sepal.length")
cl1.write(dt['sepal.length'].sum())

cl2.write("sepal.width")
cl2.write(dt['sepal.width'].sum())

cl3.write("petal.length")
cl3.write(dt['petal.length'].sum())

cl4.write("petal.width")
cl4.write(dt['petal.width'].sum())

st.write("ค่าเฉลี่ย")
cl1.write("sepal.length")
cl1.write(dt['sepal.length'].mean())

cl2.write("sepal.width")
cl2.write(dt['sepal.width'].mean())

cl3.write("petal.length")
cl3.write(dt['petal.length'].mean())

cl4.write("petal.width")
cl4.write(dt['petal.width'].mean())
