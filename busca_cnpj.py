import requests

cnpj = input('Insira o CNPJ: ')
cnpj = cnpj.replace("-", "").replace(".", "")

if len(cnpj) == 14:
    url = f'https://brasilapi.com.br/api/cnpj/v1/{cnpj}'
    
    requisicao = requests.get(url)
    print(requisicao)
    
    dic_requisicao = requisicao.json()
    nome = dic_requisicao['nome_fantasia']
    razao_social = dic_requisicao['razao_social']
    print(nome)
    print(razao_social)
else:
    print('CNPJ inválido')
    