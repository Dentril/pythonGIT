import http.client
import base64

# Defina seu token de acesso pessoal
token = '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'
repositorio = 'codigos'
arquivo_local = 'web.html'
pasta_destino = 'codigos.git'

# Leitura do conteúdo do arquivo
with open(arquivo_local, 'rb') as file:
    arquivo_bytes = file.read()

# Codifique o conteúdo do arquivo para base64
arquivo_base64 = base64.b64encode(arquivo_bytes).decode()

# Construa a URL para a API
url = f'https://api.github.com/repos/{repositorio}/contents/{pasta_destino}/{arquivo_local}'

# Crie o cabeçalho com o token de acesso pessoal e o User-Agent
headers = {
    "Authorization": f"Token {token}",
    "Content-Type": "application/json",
    "User-Agent": "MeuApp"
}

# Crie o payload para enviar para a API
payload = {
    "message": "Adicionando arquivo",
    "content": arquivo_base64
}

# Faça uma requisição PUT para enviar o arquivo
conn = http.client.HTTPSConnection("api.github.com")
conn.request("PUT", url, body=str(payload), headers=headers)
response = conn.getresponse()

# Verifique a resposta da requisição
if response.status == 201:
    print('Arquivo enviado com sucesso!')
else:
    print('Ocorreu um erro ao enviar o arquivo.')
    print(response.read().decode())'