from flask import Flask, request, jsonify
import random
from flask_cors import CORS

app = Flask(__name__)
CORS(app) 

funny_responses = [
    "Por que o pombo não usa tênis? Porque ele já tem asa!",
    "Qual é o animal mais antigo do mundo? A zebra, porque é preta e branca!",
    "O que o zero disse para o oito? Que cinto bonito!",
    "Qual é o animal que nasce no ovo e morre na goiaba? O ovo de colher!",
    "Por que o livro de matemática cometeu suicídio? Porque tinha muitos problemas!",
    "Qual é o lugar em que ninguém vê? O dentista!",
    "Por que a plantinha não fala? Porque ela não é de papo!",
    "Qual é o doce que vira monstro? O biscoito da sorte!",
    "Por que o jacaré tirou o pé da lama? Porque senão o sapo afundava!"
]
@app.route("/api/chat", methods=["GET"])
def chat():
    user_message = request.args.get('message', '')

    if any(word in user_message.lower() for word in ["piada", "engraçado", "risada"]):
        bot_message = random.choice(funny_responses) 
    else:
        bot_message = "Desculpe, não entendi. Pode repetir?"

    return jsonify({"message": bot_message})

if __name__ == "__main__":
    app.run(debug=True)
