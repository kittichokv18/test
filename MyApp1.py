import streamlit as st
import pandas as pd

st.title("website Developing using python")
st.header("website Developing using python")
st.subheader("9arm ใจเกเล")
st.image('img/dance.gif')

dt=pd.read_csv('data/iris.csv')
st.write(dt.head(10))