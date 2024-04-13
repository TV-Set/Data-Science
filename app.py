from flask import Flask, render_template, request
from processing import predict, load_models

app = Flask(__name__)
@app.route("/", methods=["get", "post"]) # 127.0.0.1:5000 + "/" = 127.0.0.1:5000/

def main(): # Данная функция вызывается с помощью декоратора "@app.route()"
    model, scaler_x, scaler_y = load_models()
    message = "Ничего не введено"
    if request.method == "POST":
        density_1 = request.form.get("density_1")
        module_1 = request.form.get("module_1")
        amount = request.form.get("amount")
        epoxy = request.form.get("epoxy")
        temp = request.form.get("temp")
        density_2 = request.form.get("density_2")
        module_2 = request.form.get("module_2")
        hard = request.form.get("hard")
        resin = request.form.get("resin")
        pitch = request.form.get("pitch")
        patch = request.form.get("patch")
        angle = request.form.get("angle")
        try:
            density_1 = float(density_1)
            module_1 = float(module_1)
            amount = float(amount)
            epoxy = float(epoxy)
            temp = float(temp)
            density_2 = float(density_2)
            module_2 = float(module_2)
            hard = float(hard)
            resin = float(resin)
            pitch = float(pitch)
            patch = float(patch)
            density_1, module_1, amount, epoxy, temp, density_2, module_2, hard, resin, pitch, patch = scaler_x.transform([[density_1], [module_1], [amount], [epoxy], [temp], [density_2], [module_2], [hard], [resin], [pitch], [patch], [angle]])
            result = predict(density, model)
            message = f'Соотношение "матрица-наполнитель": {density}'
        except:
            message = f"Вы ввели некорректное значение: {density_1}, {module_1}, {amount}, {epoxy}, {temp}, {density_2}, {module_2}, {hard}, {resin}, {pitch}, {patch}"

    return render_template("index.html", message=message)

app.run()