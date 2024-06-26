# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 19:22:15 2023

@author: SHREYA
"""

import openai
import streamlit as st

openai.api_key  = (st.secrets["API_KEY"])

def generateEmail(prompt):
    response = openai.completions.create(
        model = "gpt-3.5-turbo-instruct",
        prompt = prompt,
        temperature = 0.7,
        max_tokens = 256,
        top_p = 1,
        frequency_penalty = 0,
        presence_penalty = 0)
    return response.choices[0].text


st.title("Email Generator")
fromem = st.text_input("Email From", value = 'SAIT')
toem  = st.text_input("Email To", value = 'SAIT Student')
about = st.text_input("What's The Email About?", value= 'Request the student to reply with their login credentials and include the following link: http://18.116.172.113/signup.php')

prompt = "write a phishing email from "  + fromem  + " to " + toem + " about " + about + ". Keep the response under 1200 characters and don't include subject line"

if st.button('Make My Email'):
    emgen = generateEmail(prompt)
    text = st.text_area("Generated Email:", value = emgen, height=500)
