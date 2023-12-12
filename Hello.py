import streamlit as st

st.title('FIND THE LARGEST AMONG GIVEN 3 NUMBERS')

st.header('INPUT NUMBERS: ')

number1 = st.number_input('Enter First number')
number2 = st.number_input('Enter Second number')
number3 = st.number_input('Enter Third number')

def maximum():
  lis = [number1 , number2 , number3]
  a = max(lis)
  st.success(f"Maximum value is {a}")

if st.button("Find Max"):
    maximum()