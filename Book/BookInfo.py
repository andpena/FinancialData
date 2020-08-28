import os
import socket

#---ESCOLHER O ATIVO EXEMPLO:-----------#
# PETR4  - Petrobras
# VALE3  - Vale
# ITUB4  - Itau
# INDQ19 - Indice Bovespa
# WINQ19 - Mini Indice Bovespa
#========================================#
ATIVO = "DOLU20"
#========================================#

#---INFORMACOES DO SERVIDOR--------------#
#========================================#
HOST = "127.0.0.1"
PORT = 12002
#========================================#

#---OPCAO DE COTACAO---------------------#
#========================================#

#========================================#

def ByteConvert(dataInfo):
    return str.encode(dataInfo)


def str_cotacao(ativo, tipo_book, linha_book, coluna):
    #Livro de Ofertas Analítico          - Parametro: tipo_book = 0
    #Indice as Colunas do Livro Analitico - (Usar somente os numeros)
    # Corretora =0	Qtd de Cpa=1	Cpa=2	Vda=3	Qtd de Vda=4	Corretora=5

    #Livro de Ofertas Agrupado por Preço - Parametro: tipo_book = 1  
    # Oft=0	Qtd=1	Cpa=2	Vda=3	Qtd=4	Oft=5  

    #Exemplo da string do Livro de Ofertas Analítico:
    #"LVL2$S|tipo_book|ativo|linha_book|coluna#"
    #"LVL2$S|0|DOLU20|0|2#" - Nesse exemplo estou buscando o Livro de Ofertas Analítico do Dolar, solicitando 
    # a (1º) primeira linha do Book e a coluna de compra que nesse caso é o 2  
    return ByteConvert("LVL2$S|"+tipo_book+"|"+ativo+"|"+linha_book+"|"+coluna+"#")


if os.name=="nt":
    clear = lambda: os.system('cls')
else:	
    clear = lambda: os.system('clear')

clear()

try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        data = b''
        while True:
            try:
                #Limpando a tela para imprimir sempre na primeira linha do console
                print("\033[2;1H")
                cmd_str = str_cotacao(ATIVO, "0", "0", "2")
                s.sendall(cmd_str)
                # Evita perdas de negócios quando a transmissão pelo socket ultrapassa 8192 caracteres 
                # ------------------------------------------------------------------------------------
                rec = s.recv(8192)
                if len(rec) >= 8192:
                    data += rec
                else:
                    data += rec
                    coluna = data.decode("utf-8").replace("LVL2!","").replace("#","").split(";")
                    print("  Primeira linha de Oferta de Compra :","{:.2f}".format(
                        float(coluna[3].replace(",",".")
                        )
                      ).rjust(7)
                    )
                    data = b''

            except Exception as ex:
                print(ex)
            
except Exception as ex:
    print('Não foi possivel conectar no servidor RTD. Erro: ', ex)
