# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 19:22:15 2023

@author: SHREYA
"""

import openai
import streamlit as st

openai.api_key  = API_KEY

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
about = st.text_input("What's The Email About?", value= 'Request a reply with their login credentials')

prompt = "write an email from "  + fromem  + " to " + toem + " about " + about

if st.button('Make My Email'):
    emgen = generateEmail(prompt)
    #st.write(emgen)
    text = st.text_area("Make Changes:", value = emgen, height=500)
    #generateEmail("Emailt to Ray to Say Hello"))
