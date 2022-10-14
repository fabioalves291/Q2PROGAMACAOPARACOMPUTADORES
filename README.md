# Q2PROGAMACAOPARACOMPUTADORES

2. Fazer um programa que efetue a leitura dos arquivos que estão contidos no arquivo 
serie_historica_anp.rar1 e realize as seguintes operações (descompacte o arquivo em um 
diretório/pasta chamado serie_historica_anp): Observação: o programa deverá reconhecer a inclusão 
de novos arquivos no diretório/pasta sem ser necessária a alteração no código fonte.
a) O programa deverá criar um diretório chamado dados_estatisticos na mesma pasta que está o 
arquivo .py;
b) Deverá ser gerada uma lista contendo as seguintes informações de todos os arquivos lidos: 
Regiao – Sigla, Estado – Sigla, Produto, Data da Coleta, Valor de Venda, Bandeira;
1 Dados extraídos de https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/serie-historica-de-precos-de-combustiveis (acessado em 17/01/2022)
Curso Superior de Tecnologia em Redes de Computadores
Disciplina: TEC.0142 - Programação para Redes (NCT)
Professor: Freitas, Charles Cesar Magno de
Página: 2 de 3
c) A lista gerada deverá ser salva em um único arquivo chamado serie_historica_anp.txt dentro 
do diretório criado no item a. Cada informação deverá ser separada por ; (ponto e vírgula).
d) Com base na lista gerada no item b, deverão ser geradas as seguintes listas abaixo (cada lista 
deverá ser salva em formato de arquivo com o dados separados por ; no diretório criado no item 
a). O nome de cada arquivo está no início de cada tópico:
i. Nome do arquivo: media_bandeira.txt
bandeira – produto – ano – valor_medio_venda – quantidade_postos
ii. Nome do arquivo: media_produto_regiao.txt
produto – região – ano – valor_medio – quantidade_postos
