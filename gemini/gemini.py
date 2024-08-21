import pathlib
import textwrap

import google.generativeai as genai

model=genai.GenerativeModel('gemini-pro')
GOOGLE_API_KEY="AIzaSyDENVUlQODIgXvzsxG5HA-XOB2dkMUWePA"

genai.configure(api_key=GOOGLE_API_KEY)

def prompt():
    context=""
    while True:
        user_input=input("YOU: ")
        if user_input.lower()=='exit':
            break
        response=model.generate_content(user_input)
        print("ChatBot: ",response.text)
        context+= f"\nUser: {user_input}\nAI:{response.text}"
        # print(response.text)

if __name__=="__main__":
    prompt()