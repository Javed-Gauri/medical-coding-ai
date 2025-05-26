from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Medical Coding API - Add your AI logic here"

if __name__ == '__main__':
    app.run()
