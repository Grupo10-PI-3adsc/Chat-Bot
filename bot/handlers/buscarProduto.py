import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("API_BASE_URL")

def buscar_produto():
    produtoBusca = input("Qual produto você procura? ")

    url = f"{BASE_URL}/produtos/buscar-por-nome"
    params = {'nome': produtoBusca}

    response = requests.get(url, params=params)

    if response.status_code == 200:
        try:
            produtos = response.json()
            if produtos:
                print("Resultado JSON formatado:")
                print(json.dumps(produtos, indent=4, ensure_ascii=False))
                
                print("\nProdutos encontrados:")
                for produto in produtos:
                    print(f"Nome: {produto['nome']}")
                    print(f"Preço: R${produto['preco']}")
                    print("-" * 20)
            else:
                print("Produto não encontrado.")
        except Exception as e:
            print("Erro ao processar o JSON:", e)
    elif response.status_code == 204:
        print("Produto não encontrado.")
    else:
        print("Erro ao conectar:", response.status_code)
