# Projeto 1 - Gerador de dados 

#Bibliotecas

import random # Para gerar valores aleatorios


# 1° Passo -  Criar as listas de nomes, e-mails, telefones, cidades , estados 
while True:

    nomes = ['Luiz','Bruna','Kleber','Pereira','Thais']
    emails = ['Luiz@gmail.com', 'Bruna@hotmail.com', 'Kleber@yahoo.com', 'Pereira@bing.com','Thais@gmail.com']
    telefones = ['989654789','985264711','910205548', '977201146','980558879']
    cidades = ['Santo andre', 'Sao paulo', 'Sao Caetano', 'Praia grande', 'Diadema']
    estados = ['Sao paulo', 'Rio de janeiro', 'Amazonas', 'Rio Grande do Sul', 'Minas Gerais']


# 2° Passo - Perguntar para o usuario qual é o dado que ele deseja 
# gerar e se ele deseja salvar no arquivo dados.txt

    entrada = input('''Qual dado você deseja gerar: 
                [1] Nomes 
                [2] Emails
                [3] Telefones
                [4] Cidades
                [5] Estados
                [6] Finalizar Programa 
                R: ''').split()



#3° Passo - Mostrar na tela o valor gerado
    listas = [nomes, emails, telefones, cidades, estados]
    lista2 = ['Nome: ', 'Email: ', 'Telefone: ', 'Cidade: ' ,'Estado: ']
    
    
    if entrada[0] == '6':
        print('Projeto finalizado')
        break
       
    else:
        salvar_dados = input('Deseja salvar os dados? (s/n)')
        for x in entrada:
            valor_aleatorio_listas = random.choice(listas[int(x)-1])
            print(f'{lista2[int(x)-1]} {valor_aleatorio_listas}')
#4° Passo - Fazer o processo de salvar o dado gerado no arquivo .txt
            if salvar_dados == 's':
                with open("projeto1.txt","a", newline="") as arquivo:
                    arquivo.write('\n')
                    arquivo.write(lista2[int(x)-1])
                    arquivo.write(valor_aleatorio_listas)
                    arquivo.write('\n')    
                arquivo.close()
           
            




    

