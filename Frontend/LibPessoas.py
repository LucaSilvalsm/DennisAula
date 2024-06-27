class Pessoa:
    def __init__(self, nome, idade):
        self.matricula = ""
        self.nome = nome
        self.idade = idade
    def __str__(self):
        return f'{self.nome} :: {self.idade}'
    def exibir(self):
        print(f'{self.nome} tem {self.idade} anos')
    def serialize(self):
        return {"matricula": self.matricula,
                "nome": self.nome,
                "idade": self.idade}

class Profissional(Pessoa):
    def __init__(self, nome, idade, profissao):
        super().__init__(nome, idade)
        self.profissao = profissao
    def __str__(self):
        return Pessoa.__str__(self)+f' :: {self.profissao}'
    def exibir(self):
        super().exibir()
        print(f'\t...e trabalha como {self.profissao}')
        