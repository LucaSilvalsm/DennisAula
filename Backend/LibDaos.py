from LibPessoas import Pessoa
from SQL_Model import PessoaDB
from SQL_Engine import engine
from sqlalchemy import select, update
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)

class PessoaDAO:
    def __init__(self):
        pass
    def incluir(self, pessoa):
        session = Session()
        p = PessoaDB(nome = pessoa.nome, idade = pessoa.idade)
        session.add(p)
        session.commit()
        pessoa.matricula = p.matricula
        return pessoa
    def alterar(self, pessoa):
        session=Session()
        session.execute(update(PessoaDB),[pessoa.serialize()])
        session.commit()
    def excluir(self, chave):
        session = Session()
        p = session.get(PessoaDB, chave)
        session.delete(p)
        session.commit()
    def obterTodos(self):
        session = Session()
        stmt = select(PessoaDB)
        pessoas = []
        for p in session.scalars(stmt):
            pessoa = Pessoa(p.nome,p.idade)
            pessoa.matricula = p.matricula
            pessoas.append(pessoa)
        session.commit()
        return pessoas
    def obter(self, chave):
        session = Session()
        p = session.get(PessoaDB, chave)
        pessoa = Pessoa(p.nome,p.idade)
        pessoa.matricula = p.matricula
        session.commit()
        return pessoa