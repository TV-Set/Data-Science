from flask import Flask

app = Flask(__name__)
@app.route("/")

def print_hello():
    return "<h1>Hello!</h1>"  # Заголовок первого уровня

app.run()