from flask import Flask, render_template, request, jsonify
import speech_recognition as sr
import random
import string

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('welcome.html')

@app.route('/login', methods=['POST'])
def login():
    # Initialize the recognizer
    r = sr.Recognizer()

    # Use the microphone as the audio source
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

        try:
            # Convert the audio to text
            text = r.recognize_google(audio)
            print("You said: " + text)

            # Check if the user said the correct password
            if text.lower() == "wellsfargo":
                return jsonify({'success': True}), 200
            else:
                return jsonify({'success': False, 'message': 'Incorrect password'}), 401

        except:
            # If the speech recognition failed, return an error message
            return jsonify({'success': False, 'message': 'Speech recognition failed'}), 500

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Get the user's input from the form
        name = request.form['name']
        email = request.form['email']
        voice = request.form['voice']

        # Generate a random password
        password = ''.join(random.choices(string.ascii_letters + string.digits, k=10))

        # Save the user's information to a database or file
        # For this example, we'll just print it to the console
        print(f"Name: {name}")
        print(f"Email: {email}")
        print(f"Voice: {voice}")
        print(f"Password: {password}")

        return jsonify({'success': True}), 200

    else:
        # If the user accessed the page through a GET request,
        # render the registration form
        return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)
