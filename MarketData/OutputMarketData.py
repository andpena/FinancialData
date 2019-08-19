import os
from colorama import  Fore,Back, Style, init

class OutputMarketData:
    def __init__(self):
        #--Inicia o COLORAMA para o texto sair---# 
        # colorido no console (firula...!!!)
        init()  
        clear = lambda: os.system('cls')
        clear() 
        #========================================#

    def OutputData(self,arrDados, arrAtivo):
        arrTpCot = ["Ativo                         ","Última                        ","Var.                          ","Qtd. Compra                   ","Compra                        ","Venda                         ",
                    "Qtd. Venda                    ","Abertura                      ","Máxima                        ","Mínima                        ","Fechamento                    ","Volume                        ",
                    "Hora                          ","Fech. Ajustado                ","Núm. de Negócios              ","Média                         ","Papéis Negociados             ","TODO IDENTIFICAR (01)         ","Estado                        ",
                    "Vencimento                    ","Lote Mínimo                   ",
                    "Dias até Vencimento           ","Dias Úteis até Vencimento     ","Var. %                        ","Var. (Var. %)                 ","Data                          ",
                    "Data/Hora                     ","Descrição                     ","Exercício                     ",
                    "Var. Simb.                    ","Semanal (Var. %)              ","Mensal (Var. %)               ","Anual (Var. %)                ","30 Dias (Var. %)              ","12 Meses (Var. %)             ",
                    "52 Semanas (Var. %)           ","2 Anos (Var. %)               ","Ajuste PU                     ","Ajuste PU Anterior            ",
                    "Preço Teórico                 ","Quantidade Teórica            ","Fim do Leilão                 ","Contratos em Aberto           ","Fech. Ajustado Anterior       ","MCap                          ",
                    "Ações no Mercado              ","Agr. Cmp.                     ","Agr. Cmp. (Direto)            ","Agr. Cmp. (Não-direto)        ","Agr. Vnd.                     ","Agr. Vnd. (Direto)            ",
                    "Agr. Vnd. (Não-direto)        ","Saldo Agr.                    ","Saldo Agr. (Direto)           ","Saldo Agr. (Não-direto)       ","Agr. Cmp. %                   ","Agr. Cmp. % (Direto)          ",
                    "Agr. Cmp. % (Não-direto)      ","Agr. Vnd. %                   ","Agr. Vnd. % (Direto)          ","Agr. Vnd. % (Não-direto)      ","Qtd. Rest.                    ","Ind. Sald.                    ",
                    "Neg. Agr. Cmp.                ","Neg. Agr. Cmp. (Direto)       ","Neg. Agr. Cmp. (Não-direto)   ","Neg. Agr. Vnd.                ","Neg. Agr. Vnd. (Direto)       ","Neg. Agr. Vnd. (Não-direto)   ",
                    "Saldo Neg. Agr.               ","Saldo Neg. Agr. (Direto)      ","Saldo Neg. Agr. (Não-direto)  ","Neg. Agr. Cmp. %              ","Neg. Agr. Cmp. % (Direto)     ","Neg. Agr. Cmp. % (Não-direto) ",
                    "Neg. Agr. Vnd. %              ","Neg. Agr. Vnd. % (Direto)     ","Neg. Agr. Vnd. % (Não-direto) ","PTAX P1                       ","PTAX P2                       ","PTAX P3                       ",
                    "PTAX P4                       ","PTAX Oficial                  ","PTAX Fut. P1                  ","PTAX Fut. P2                  ","PTAX Fut. P3                  ","PTAX Fut. P4                  ",
                    "PTAX Fut. Oficial             "] 
        strLayout = ""
        for i in range(len(arrTpCot[:37])):
            strLayout += arrTpCot[i]
            for y in range(len(arrDados)):
                if(i==27):
                    strLayout += " "+ arrDados[y][i][:10].ljust(17) + "|".rjust(7)
                else:
                    strLayout += " "+ arrDados[y][i].ljust(17) + "|".rjust(7)
            
            strLayout += "\n"
            if(i == 0):
                strLayout +="-".rjust(155,"-") +"\n"   
        print("\033[2;1H")
        print(strLayout) 
        
        strLayout = "" 
