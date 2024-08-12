import streamlit as st
import json
from streamlit_lottie import st_lottie

# Page Settings
st.set_page_config(page_title="Contact Emon", page_icon=r"E:\Portfolio\assets\goat.png")

# Load the animation
with open(r"E:\Portfolio\assets\Animation.json") as source:
    animation = json.load(source)

# Display the Lottie animation
st_lottie(animation, width=700, height=300)

# Display the contact header
st.markdown('<h1 style="text-align:center;">Contact</h1>', unsafe_allow_html=True)

# Form for user input
with st.form("My Form", clear_on_submit=True):
    col1, col2 = st.columns(2)
    f_name = col1.text_input(label="First Name", placeholder="First")
    l_name = col2.text_input(label="Last Name", placeholder="Last")
    email = st.text_input(label="Enter Mail", placeholder="you_mail@example.com")
    message = st.text_area(label="Message", placeholder="Hello....", max_chars=200)

    submitted = st.form_submit_button("Submit")

    if submitted:
        if f_name == "" or l_name == "" or message == "" or email == "":
            st.warning("Please fill out all fields.")
        else:
            st.success("Form submitted successfully!")
            res = f"""
            <div style="text-align: center;">
                <form action="https://formsubmit.co/66fe6238339c6f0fc2fd4814f28b2478" method="POST">
                    <input type="hidden" name="First Name" value="{f_name}">
                    <input type="hidden" name="Last Name" value="{l_name}">
                    <input type="hidden" name="Message" value="{message}">
                    <input type="hidden" name="Email" value="{email}">
                    <input type="hidden" name="_captcha" value="false">
                    <input type="submit" value="Confirm" style="
                        background-color: #D1E9F6;
                        border: none;
                        color: black;
                        padding: 10px 20px;
                        text-align: center;
                        text-decoration: none;
                        display: inline-block;
                        font-size: 16px;
                        margin: 4px 2px;
                        cursor: pointer;
                        border-radius: 4px;">
                </form>
            </div>
            """
            st.markdown(res, unsafe_allow_html=True)
