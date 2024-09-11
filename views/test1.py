import streamlit as st

st.title("텍스트")


st.divider()  # 가로 긴 줄 구분선


st.title('This is title')          # 대제목
st.header('This is header')        # 중제목
st.subheader('This is subheader')  # 소제목


st.divider()  # 가로 긴 줄 구분선


# markdown
st.markdown(
    '''
    This is main text.
    This is how to change the color of text :yellow[Yellow,] :blue[Blue,] :green[Green.]
    This is **Bold** and *Italic* text
    '''
)


st.divider()  # 가로 긴 줄 구분선


# text
st.text(
    '''
    This is main text.
    This is how to change the color of text :red[Red,] :blue[Blue,] :green[Green.]
    This is **Bold** and *Italic* text
    '''
)


st.divider()  # 가로 긴 줄 구분선


# code
code = '''
import matplotlib.pyplot as plt

plt.title('linestyle')
plt.plot([10, 20, 30, 40], color='r', marker=".", linestyle='--', label='dashed')
plt.plot([40, 30, 20, 10], color='g', marker="^", ls=':', label='dotted')
plt.legend()
plt.show()
'''
st.code(code, language='python')

