import streamlit as st
import random

def generate_password(space, length):
    return ''.join(random.SystemRandom().choice(space) for _ in range(length))

char_set_1 = "!@#$%^&*()_+-={}[]|\\:;'<>,.?/"
char_set_1_mobile_friendly = '`!@&()-+:;",.?*'
char_set_2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz"

st.title('Password Generator')
st.write("Generate secure passwords with customizable options.")

col1, col2 = st.columns(2)

with col1:
    is_mobile = st.checkbox("Mobile Friendly", value=True, help="Select if the password should be mobile-friendly.")
    length = st.slider("Password Length", min_value=6, max_value=20, value=10, help="Choose the length of the password.")

with col2:
    chosen_set = char_set_1_mobile_friendly if is_mobile else char_set_1
    char_set_1 = st.text_input("Special Characters", value=chosen_set, help="Enter special characters for the password.")
    char_set_2 = st.text_input("Numbers and Letters", value=char_set_2, help="Enter numbers and letters for the password.")

if st.button("Generate Password"):
    password_space = char_set_1 + char_set_2
    generated_password = generate_password(password_space, length)
    st.info('Your Password: ' + generated_password)
