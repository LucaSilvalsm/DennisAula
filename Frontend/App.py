from flask import Flask, render_template, request, redirect
from LibIntegracao import PessoaNet
from LibPessoas import Pessoa

app = Flask(__name__)

cliente = PessoaNet()

@app.route("/")
def home(): 
    return render_template("index.html")

@app.get("/pessoas/lista")
def obterTodos():
    return render_template("listaPessoas.html", pessoas=cliente.obterTodos()) 

@app.get("/pessoas/inclui")
def formIncluir():
    return render_template("formPessoas.html")

@app.post("/pessoas/inclui")
def incluir():
    nome = request.form.get("n1")
    idade = int(request.form.get("i1"))
    cliente.incluir(Pessoa(nome,idade))
    return redirect("/pessoas/lista")

@app.get("/pessoas/exclui")
def excluir():
    matricula = int(request.args["matricula"])
    cliente.excluir(matricula)
    return redirect("/pessoas/lista")

@app.get("/pessoas/altera")
def formAlterar():
    matricula = int(request.args["matricula"])
    return render_template("formPessoasAltera.html",
                           p=cliente.obter(matricula))


@app.post("/pessoas/altera")
def alterar():
    matricula = int(request.form.get("m1"))
    nome = request.form.get("n1")
    idade = int(request.form.get("i1"))
    p = Pessoa(nome, idade)
    p.matricula = matricula
    cliente.alterar(p)
    return redirect("/pessoas/lista")

if __name__ == '__main__':
    app.run(debug=True, port=8008)

