import os
import sys
import time
import json

def menu():
    print('''
1° PRIMEIRA ETAPA
é ler todos dados e agrupar todas informacoes em um arquivo
2° SEGUNDA ETAPA
é ler todos dados e fazer as comparacoes mais os calculos.
.
se ja tiver o arquivo unico com todos os dados prescione " 2 "
''')
    return
    
local = os.path.abspath('seriefinal')
arquivo = 'seriefinal.txt'
data_e_hora_em_texto = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
dadoslista = list()
#time.ctime()
print(data_e_hora_em_texto)
bandeiras = list()
produtos = list()
datasdascoletas = list()
regioes = list()
#criando pasta

while True:
    menu()
    v = input('digite 1 para a primeira etapa ou  prescione " Enter " para a segunda: ')
    if v == str(1):
        v = True
    else:
        v = False
        
    if v == True : 
        try:
            print('criando pasta seriefinal')
            os.mkdir('seriefinal')
        except FileExistsError:
            print('pasta seriefinal ja existente')
        try:
            os.mkdir('log')
        except FileExistsError:
            print('pasta log já existente ')
        
        lista_nomes_arquivos = os.listdir('serie')
    #------------------------------------#


    # criando e limpando arquivo
        file = open(fr'seriefinal/{arquivo}','w')
        file.close()
    #------------------------------------#


    # abrindo arquivos da pasta serie
        print('lendo arquivos')
        for nome_arquivo in lista_nomes_arquivos:
            file = open(r'serie/'+ nome_arquivo,'r',encoding ='UTF-8')
            print('lendo '+nome_arquivo)
            for dados in file:
                #print(dados)
                #input()
                
    # retirando dados dos arquivos
                dados = dados[:-1]
                dados = dados.split(';')
                        #print(dados)
                        #input()
                    #print(dados)
                
                try:    #se vc colcar bandeira dados[15] vai ter um momento que vai pegar numeros e com dados[-1]
                    dados[-4]
                    valor_trocar_virg_pontu = str()
                    for letra in dados[-4]:
                        if letra == ',':
                            valor_trocar_virg_pontu += '.'
                        else:
                            valor_trocar_virg_pontu += letra
        
                    bandeira={"BANDEIRA":dados[-1],"REGIAO":dados[-16],"ESTADO":dados[-15],"CNPJ-REVENDDA":dados[-12],"PRODUTO":dados[-6],"DATA-DA-COLETA":dados[-5],"VALOR-DE-VENDA":valor_trocar_virg_pontu}
                    #corrigir bandeiras que nao pode ter espaço,dois pontos, barra, contra barra.
                    palavra = str()
                    for letra  in bandeira['BANDEIRA']:
                        if letra in '"/\ ' or letra in " ' ":
                            pass
                        else:
                            palavra += letra
                    bandeira['BANDEIRA'] = palavra
                        
                except  IndexError:
                    print('!!!!   criar um log   !!!!')
                    
                #tive   colocar o raplace porque nao ficava com duas aspas 
                bandeira = str(bandeira).replace("'",'"')
                recorte = bandeira

                dadoslista.append(recorte)
                    #print(dadoslista)
                    #input(recorte)
                    
    # gravando dados selecionados em um arquivo
            filew = open(fr'seriefinal/{arquivo}','a',encoding ='UTF-8')
            print('escrevendo')
            for dados in dadoslista:
                #input(str(dados)+'\n')
                
                filew.write(dados+'\n')
            filew.close()
        
            dadoslista = list()
            
            file.close()
        print('arquivos lidos')
#------------------------------------#

#------------------------------------#
#       Regiao - Sigla;Estado - Sigla;CNPJ da Revenda;Produto;Data da Coleta;Valor de Venda;Bandeira
#       a = (dados[0]+';'+dados[1]+';'+dados[4]+';'+dados[10]+';'+dados[11]+';'+dados[12]+';'+dados[15])
#------------------------------------#



    else:
    #   ler o arquivo unico ja
        file = open(local+'/'+arquivo,'r',encoding='UTF-8')
        print('lendo arquivo ja formatado e retirando dados...')
        cont = 0
        b = 100000
        for dados in file:
            try:
                #input(dados)
                dados = json.loads(dados)
            
                #sprint('criar log')
                
                
                #mas ficou salvo como '' e nao com "" #corrigi ja na  hora de salvar o arquivo-seriefinal/escrita para agilizar o processo # comentario aqui para converter para json/dicionario é obrigatorio utilizar duas aspas " .
                #importante! quando vc usar o json ele troca as aspas duplas pela simples.
            
    #------------------------------------#

    # agora vamos pegar as bandeiras , quando o arquivo esta escrevendo o arquivo poderiamos ja pegar as bandeiras mas assim fica melhor dever como funciona o arquivo
    
    # pegando bandeiras, datas de coletas , produtos e regioes        
                if not dados['BANDEIRA'] in bandeiras:
                    bandeiras.append(dados['BANDEIRA'])
            
                #criar log
                #print(dados)
            
    #   coletando datas de coleta
            
                if dados['DATA-DA-COLETA'][-4:] not in datasdascoletas:
                    data = dados['DATA-DA-COLETA'][-4:]
                    datasdascoletas.append(data)
                
                #criar log
                
            #print(dados)
            #print(type(dados['PRODUTO']))
            
                if dados['PRODUTO'] not in produtos:
                    produtos.append(str(dados['PRODUTO']))


                if dados['REGIAO'] not in regioes:
                    regioes.append(dados['REGIAO'])
                    
            except TypeError:
                pass
            except json.decoder.JSONDecodeError:
                pass

            cont += 1
            
            if cont == b:
                print(str(cont)[0:-3],'K','linhas lidas de 4 milhoes de linhas')
                b += 100000
        
                # criar log

            #print(produtos)
            #print(bandeiras)
#


        file.close()
        print('')
        print('dados lidos e retirados.')
        print('produtos,bandeiras e datas ja estão catalogadas e prontas para proxima etapa!')
        a = len(bandeiras)-1
        b = len(produtos)-1
        c = len(datasdascoletas)-1
        d = a*b*c
        print('São {} bandeiras, {} produtos, {} anos/datas. Então são {} possibilidades para verificar e calcular. \n' .format(a,b,c,d))
        #input('Enter para continuar')
        quantidade_de_postos = 0
        auxiliar_andamento = 0
        # credito que da para evitar essa redudancia mas ja demorei muito nessa questao e vou manter assim por enquanto.
        v = input('digite " a " para ver media por bandeira e " b " por produto.')
        if v == 'a':
            for bandeira in bandeiras:
                if not bandeira =='Bandeira':
                    for produto in produtos:
                        if not produto =='Produto':
                            for ano in datasdascoletas:
                                if not ano == 'leta':
                                    auxiliardevalor = float(0.0)
                                    medias = list()
                                    file = open(local+'/'+arquivo,'r',encoding='UTF-8')
                                    print('coletando -  ',bandeira,produto,ano)
                                    print('aguarde!')
                                    
                                    linha = 0
                                    for dados in file:
                                        
                                        linha += 1
                                            #input(dados)
                                        try:
                                            dados = json.loads(dados)
                                                    #input(dados)
                                                    #input(bandeira+produto+ano)
                                            if bandeira == dados['BANDEIRA']:
                                                            #input(bandeira+dados['BANDEIRA'])
                                                if produto == dados['PRODUTO']:
                                                                #input(produto+dados['PRODUTO'])
                                                             #comentar aqui 
                                                    if ano == dados['DATA-DA-COLETA'][-4:]:
                                                                    #input(ano+dados['DATA-DA-COLETA'])
                                                        auxiliardevalor += float(dados['VALOR-DE-VENDA'])
                                                        quantidade_de_postos += 1
                                                        #valor max e min
                                                        #if
                                        
                                        except json.decoder.JSONDecodeError:
                                                pass
            
                                    try:
                                        auxiliar_andamento += 1
                                        print(bandeira,produto,ano,'valor medio:', '{:.4f}'.format(auxiliardevalor/quantidade_de_postos ),'quantidade de postos(nominal):',quantidade_de_postos)
                                        print(str(auxiliar_andamento) + ' de '+ str(d))
                                    except ZeroDivisionError:
                                        print(linha)    #criar log colocar linha no log
                                        logfile = open('log/log.txt','a')
                                        logfile.write(f'')
                                        pass
                                    print('')
                                    auxiliardevalor = float(0.0)
                                    quantidade_de_postos = 0


                                    #   gravar media 
                            #criar log()
                
                #input(dados)
                #json.loads ele troca as " por ' . retire os comentarios para ver acima
            file.close()
    #       for regiao in regioes:
                                #if not regiao == '\ufeffRegiao - Sigla':
        #print(datasdascoleta)
        else:
            for regiao in regioes:
                if not regiao =='\ufeffRegiao - Sigla':
                    for produto in produtos:
                        if not produto =='Produto':
                            for ano in datasdascoletas:
                                if not ano == 'leta':
                                    auxiliardevalor = float(0.0)
                                    medias = list()
                                    file = open(local+'/'+arquivo,'r',encoding='UTF-8')
                                    print('coletando -  ',regiao,produto,ano)
                                    print('aguarde!')
                                    linha = 0
                                    for dados in file:
                                        linha += 1
                                            #input(dados)
                                        try:
                                            dados = json.loads(dados)
                                                    #input(dados)
                                                    #input(bandeira+produto+ano)
                                            if regiao == dados['REGIAO']:
                                                            #input(bandeira+dados['BANDEIRA'])
                                                if produto == dados['PRODUTO']:
                                                                #input(produto+dados['PRODUTO'])
                                                             #comentar aqui 
                                                    if ano == dados['DATA-DA-COLETA'][-4:]:
                                                                    #input(ano+dados['DATA-DA-COLETA'])
                                                        auxiliardevalor += float(dados['VALOR-DE-VENDA'])
                                                        quantidade_de_postos += 1
                                                        #valor max e min
                                                        #if
                                        
                                        except json.decoder.JSONDecodeError:
                                                pass
            
                                    try:
                                        auxiliar_andamento += 1
                                        print(regiao,produto,ano,'valor medio:', '{:.4f}'.format(auxiliardevalor/quantidade_de_postos ),'quantidade de postos(nominal):',quantidade_de_postos)
                                    except ZeroDivisionError:
                                        print(linha)    #criar log colocar linha no log
                                        logfile = open('log/log.txt','a')
                                        logfile.write(f'zero adicionar o contador de linha')
                                        pass
                                    print('')
                                    auxiliardevalor = float(0.0)
                                    quantidade_de_postos = 0
                                        
                                
    break
  
    
    
