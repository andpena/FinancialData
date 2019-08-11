import socket
import win32api
import TypeDataTryd as tdt
from TimesAndTrades.OutputTimesTrades import OutputTimesTrades

#---ESCOLHER O ATIVO EXEMPLO:-----------#
# PETR4  - Petrobras
# VALE3  - Vale
# ITUB4  - Itau
# INDQ19 - Indice Bovespa
# WINQ19 - Mini Indice Bovespa
#========================================#
ATIVO = 'WINQ19'
#========================================#

#---INFORMACOES DO SERVIDOR--------------#
#========================================#
HOST = '127.0.0.1'
PORT = 12002
#========================================#

#---OPCAO DE COTACAO---------------------#
#========================================#

#========================================#

def ByteConvert(dataInfo):
    return str.encode(dataInfo + ATIVO + '#')

#Inicia a Execução
ott = OutputTimesTrades()
try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        print("Id da thread principal %d" % (win32api.GetCurrentThreadId()))
        while True:
            try:
                s.sendall(ByteConvert(tdt.NEGOCIO_COMPLETO) )
                data = s.recv(32768)
                ott.OutputData(data.decode())		
            except Exception as ex:
                print(ex)
            
except Exception as ex:
    print('Não foi possivel conectar no servidor RTD. Erro: ', ex)
