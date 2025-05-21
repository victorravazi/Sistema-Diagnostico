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
    MedoDeSairDeCasa = data.get("MedoDeSairDeCasa")
    data = request.json
    Cascudo = data.get("Cascudo")
    data = request.json
    AmorReciproco = data.get("AmorReciproco")
    if MedoDeSairDeCasa == 's' and Cascudo == 's' and AmorReciproco == 's':
        return jsonify({"resposta": "Você esta virando um tatu"})
    else:
        return jsonify({"resposta": "Pereça"})

if __name__ == "__main__":
    app.run(debug=True)
