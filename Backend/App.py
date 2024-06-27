from flask import Flask
from flask import request, jsonify, make_response
from LibControllers import PessoaController
from LibPessoas import Pessoa

app = Flask(__name__)

controle = PessoaController()

@app.get("/api/pessoas")
def obterTodos():
    return jsonify(list(map(lambda x: x.serialize(), controle.obterTodos())))

@app.get("/api/pessoas/<matricula>")
def obter(matricula):
    return jsonify(controle.obter(matricula).serialize())

@app.post("/api/pessoas")
def incluir():
    dados = request.get_json()
    p = Pessoa(dados["nome"], dados["idade"])
    p.matricula = dados["matricula"]
    controle.incluir(p)
    return jsonify(p.serialize())

@app.put("/api/pessoas/<matricula>")
def alterar(matricula):
    dados = request.get_json()
    p = controle.obter(matricula)
    p.nome = dados["nome"]
    p.idade = dados["idade"]
    controle.alterar(p)
    return make_response("Alterado!",200)

@app.delete("/api/pessoas/<matricula>")
def excluir(matricula):
    controle.excluir(matricula)
    return make_response("Removido!",200)

if __name__ == '__main__':
    app.run(debug=True, port=8001)