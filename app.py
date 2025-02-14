from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
<<<<<<< HEAD
    return "Hello, Flask Musddik is here to resolve you!"
=======
    return "Hello, Flask build by mk!"
>>>>>>> origin/main

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
