from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
<<<<<<< HEAD
    return '<h1>Hello WSB! Greetings from Flask!</h1>'

if __name__ == "__main__":
    app.run(debug=True)
=======
	return '<h1>Hello WSB! Greetings from Flask!</h1>'
if __name__ == "__main__":
	app.run(debug=True)
>>>>>>> ebfa888 (requirements.txt)
