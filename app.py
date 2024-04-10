from flask import Flask, render_template, request

app = Flask(__name__)
@app.route("/", methods=["get", "post"]) # 127.0.0.1:5000 + "/" = 127.0.0.1:5000/

def index(): # Данная функция вызывается с помощью декоратора "@app.route()"
    message = "Ничего не введено"
    if request.method == "POST":
        density = request.form.get("density")
        print(density)
        message = f"Вы ввели: {density}"

    return render_template("index.html", message=message)

app.run()