import os
#metodo seguro - retorna None se não existir
api_key = os.getenv("API_KEY")
print(f"Minha chave de API é: {api_key}")

#com o valor padrão
ambiente = os.getenv("AMBIENTE", "desenvolvimento")
print(f"Estou rodando no ambiente: {ambiente}") 

#ver todas as variáveis de ambiente
for key, value in os.environ.items():
    if key.startswith('PYTHON'):
        print(f"{key}: {value}")

#acessar diretamente (cuidado!)
#database_url = os.environ["DATABASE_URL"]

#definindo uma nova variável de ambiente
os.environ["NOVA_VAR"] = "temp_value"
print(f"NOVA_VAR: {os.getenv('NOVA_VAR')}")
