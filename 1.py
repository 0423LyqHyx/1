import streamlit as st

w = st.number_input('請輸入體重(KG)')
h = st.number_input('請輸入身高(M)')
confirm_input = st.button('輸入確認')

bmi = w/(h*h)
st.write('BMI為', bmi)

if confirm_input:
    if (bmi < 18):
        st.print('體重過輕')
    elif (bmi < 24):
        st.print('體重正常')
    elif (bmi < 27):
        st.print('體重過重')
    else:
        st.print('體重肥胖')
