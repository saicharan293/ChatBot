from flask import Flask, render_template, request,jsonify
import pathlib
import textwrap

import google.generativeai as genai

model=genai.GenerativeModel('gemini-pro')
GOOGLE_API_KEY="AIzaSyDENVUlQODIgXvzsxG5HA-XOB2dkMUWePA"
genai.configure(api_key=GOOGLE_API_KEY)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_message', methods=['POST'])
    
def send_message():
    try:
        data=request.json
        user_message = data.get('message','')

        if user_message=='':
            return jsonify({'error':"No message provided"}), 400
        # Process the user message and generate a response
        bot_response = process_message(user_message)
        return jsonify({'answer':bot_response})
    # return render_template('index.html', message=user_message, response=bot_response)
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'error': 'Internal server error'}), 500

def process_message(message):
    if message.lower() == 'exit':
        return "Goodbye!"
    else:
        try:
            # Example using model.generate_content (replace with your specific logic)
            response = model.generate_content(message)
            return response.text
        except Exception as e:
            print(f"Error in processing message: {e}")
            return "Sorry, I couldn't process your request."
   

if __name__ == '__main__':
    app.run(debug=True)