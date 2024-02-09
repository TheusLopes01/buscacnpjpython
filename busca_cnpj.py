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
    atividades_principais = dic_requisicao['cnae_fiscal_descricao']
    #atividades_secundaria = dic_requisicao['descricao']
    situacao_cadastral = dic_requisicao['descricao_situacao_cadastral']
    cep_cnpj = dic_requisicao['cep']
    
    print(f'Nome: {nome}')
    print(f'Razão social: {razao_social}')
    print(f'Atividades Principais: {atividades_principais}')
    #print(f'Atividades Secundárias: {atividades_secundarias}')
    print(f'Situação Cadastral: {situacao_cadastral}')
    print(f'CEP: {cep_cnpj}')
    
else:
    print('CNPJ inválido')
    