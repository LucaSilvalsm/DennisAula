import requests
import json
from LibPessoas import Pessoa

def JSON2Pessoa(dadosJSON):
    p = Pessoa(dadosJSON["nome"],dadosJSON["idade"])
    p.matricula = dadosJSON["matricula"]
    return p

class PessoaNet:
    def __init__(self):
        self.baseURL = 'http://localhost:8001/api/pessoas'
        
    def obterTodos(self):
        resposta = requests.get(self.baseURL)
        return list(map(lambda x: JSON2Pessoa(x),
                        json.loads(resposta.content)))
    
    def obter(self, matricula):
        resposta = requests.get(f'{self.baseURL}/{matricula}')
        return JSON2Pessoa(json.loads(resposta.content))
    
    def incluir(self, p):
        resposta = requests.post(self.baseURL,json=p.serialize())
        return JSON2Pessoa(json.loads(resposta.content))
        
    def alterar(self, p):
        resposta = requests.put(f'{self.baseURL}/{p.matricula}',json=p.serialize())
        return resposta.status_code # cod HTTP 200 = sucesso
    
    def excluir(self, matricula):
        resposta = requests.delete(f'{self.baseURL}/{matricula}')
        return resposta.status_code # cod HTTP 200 = sucesso

    
        
