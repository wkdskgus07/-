import streamlit as st

st.title("Hello")
st.header("안녕~!")
st.write("안녕하세요 반가워요!")
st.subheader("Welcome to nahyeon's world!!")
clicked = st.button("시작하기")
if clicked :
  st.write("버튼 클릭됨")
