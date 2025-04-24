import streamlit as st
import json
import random
from faker import Faker

fake = Faker('pt_BR')

def gerar_json():
    nome = fake.name()
    email = fake.email()
    senha = "will@1234!"
    telefone1 = fake.msisdn()[2:11]
    telefone2 = fake.msisdn()[2:11]

    return {
        "ID": random.randint(1, 1000),
        "Nome": nome,
        "Login": email,
        "SenhaAtual": senha,
        "SenhaNova": senha,
        "Posto": 0,
        "Email": email,
        "HostName": "",
        "Autenticado": True,
        "AuthToken": "",
        "Mensagem": "",
        "SenhaExpirada": False,
        "SessaoRegistrada": True,
        "Empresa": {
            "id": 0,
            "nomeOficial": fake.company(),
            "nomeFantasia": fake.company_suffix(),
            "cnpj": fake.cnpj(),
            "tipoEmpresa": random.choice([0, 1, 2]),
            "webSite": fake.url(),
            "UsuarioID": 0,
            "experiencia": fake.catch_phrase(),
            "endereco": {
                "id": 0,
                "tipoLogradouro": random.choice([1, 2]),
                "nome_logradouro": fake.street_name(),
                "numero": fake.building_number(),
                "complemento": random.choice(["Bloco A", "Fundos", "Apto 202", "Casa 1", "Sala 5", "Beacon Academy!"]),
                "bairro": fake.bairro(),
                "municipio": {
                    "id": fake.random_int(min=1000000, max=9999999),
                    "descricao": fake.word(),
                    "estado": {
                        "id": 35,
                        "descricao": "São Paulo",
                        "sigla": "SP"
                    }
                },
                "cep": fake.postcode(),
                "observacoes": fake.sentence()
            }
        },
        "telefones": [
            {
                "ddi": "55",
                "ddd": "13",
                "numero": telefone1,
                "tipoTelefone": 1,
                "observacoes": ""
            },
            {
                "ddi": "55",
                "ddd": "11",
                "numero": telefone2,
                "tipoTelefone": 1,
                "observacoes": ""
            }
        ]
    }

# Interface do Streamlit
st.title("Gerador de JSON Aleatório")
st.write("Clique no botão para gerar um novo JSON.")

if st.button("Gerar JSON"):
    json_gerado = gerar_json()
    st.json(json_gerado)
    st.download_button("Baixar JSON", data=json.dumps(json_gerado, indent=4), file_name="dados.json", mime="application/json")
