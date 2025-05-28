from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/diagnostico", methods=["POST"])
def diagnostico():
    data = request.json

    sexo = data.get("sexo")
    altura = float(data.get("altura"))
    estrutura = data.get("estrutura")
    musculo = data.get("musculo")
    definicao = data.get("definicao")

    pontos = 0

    if sexo == "masculino":
        if altura <= 1.69:
            pontos += 7
        elif 1.70 <= altura <= 1.78:
            pontos += 10
        elif 1.79 <= altura <= 1.85:
            pontos += 5
        else:
            pontos += 0
    elif sexo == "feminino":
        if altura <= 1.56:
            pontos += 7
        elif 1.57 <= altura <= 1.65:
            pontos += 10
        elif 1.66 <= altura <= 1.75:
            pontos += 5
        else:
            pontos += 0
    if estrutura == "ombros_largos":
        pontos += 10
    elif estrutura == "iguais":
        pontos += 5
    if musculo == "muito_facil":
        pontos += 20
    elif musculo == "facil":
        pontos += 15
    elif musculo == "dificil":
        pontos += 5
    elif musculo == "muito_dificil":
        pontos -= 15
    if definicao == "facil":
        pontos += 10
    elif definicao == "normal":
        pontos += 5
    elif definicao == "sofrido":
        pontos += 0
    if pontos >= 47:
        resultado = "Genética perfeita"
    elif 37 <= pontos <= 46:
        resultado = "Genética muito boa"
    elif 30 <= pontos <= 36:
        resultado = "Genética boa"
    elif 15 <= pontos <= 29:
        resultado = "Genética mediana"
    else:
        resultado = "Genética ruim"

    return jsonify({"resposta": f"Sua pontuação foi {pontos}. {resultado}."})

if __name__ == "__main__":
    app.run(debug=True)
