from TimesAndTrades.TimeAndTradeInfo import ItensTT, TimesTrades
from colorama import  Fore,Back, Style, init

class OutputTimesTrades:
    TimesTradesList=[]

    def __init__(self):
        self.TimesTradesList.clear()
        #--Inicia o COLORAMA para o texto sair---# 
        # colorido no console (firula...!!!)
        init()   
        #========================================#

    def OutputData(self,strDados):
        self.TimesTradesList.clear()
        ItensTTList = []
        aItem = []
        try:
            aItem =strDados.split('|')
        except Exception as ex:
            print('Erro na linha 21 - Metodo: OutputData: ', ex)
        
        #id do Times&Trades
        if ( (len(aItem)==8) and (aItem[1].find('@') == -1) ):
            try:
                ItensTTList.append(ItensTT(aItem[1],aItem[2],aItem[3],aItem[4],aItem[5],aItem[6],aItem[7]))
                self.TimesTradesList.append(TimesTrades(ItensTTList[0]))
            except Exception as ex:
                print('Erro na linha 29 - Metodo: OutputData: ', ex)

        elif (len(aItem)==8):
            try:
                id      = aItem[1].split('@')
                hora    = aItem[2].split('@')
                preco   = aItem[3].split('@')
                qtde    = aItem[4].split('@')
                cpa     = aItem[5].split('@')
                vda     = aItem[6].split('@')
                agressor= aItem[7].split('@')
                
                if(len(id)==len(agressor)):
                    for i in range(len(id)):
                        ItensTTList.clear()
                        try:
                            ItensTTList.append(ItensTT(id[i], hora[i], preco[i], qtde[i], cpa[i], vda[i], agressor[i]))
                            for x in range(len(ItensTTList)):
                                self.TimesTradesList.append(TimesTrades(ItensTTList[x]))        
                        except Exception as ex:
                            print('Erro na linha 49 - Metodo: OutputData: ', ex)
            except Exception as ex:
                print('Erro na linha 51 - Metodo: OutputData: ', ex)

            
        for i in range(len(self.TimesTradesList)):
            if(self.TimesTradesList[i].agressor=="Vendedor"):
                print(self.TimesTradesList[i].id,self.TimesTradesList[i].hora.rjust(10), self.TimesTradesList[i].preco.rjust(10),self.TimesTradesList[i].qtde.rjust(4),self.TimesTradesList[i].cpa.rjust(5),self.TimesTradesList[i].vda.rjust(5) ,Fore.RED+self.TimesTradesList[i].agressor+Style.RESET_ALL)
            elif(self.TimesTradesList[i].agressor=="Comprador"):
                print(self.TimesTradesList[i].id,self.TimesTradesList[i].hora.rjust(10), self.TimesTradesList[i].preco.rjust(10),self.TimesTradesList[i].qtde.rjust(4),self.TimesTradesList[i].cpa.rjust(5),self.TimesTradesList[i].vda.rjust(5) ,Fore.GREEN+self.TimesTradesList[i].agressor+Style.RESET_ALL)
            else:
                print(self.TimesTradesList[i].id,self.TimesTradesList[i].hora.rjust(10), self.TimesTradesList[i].preco.rjust(10),self.TimesTradesList[i].qtde.rjust(4),self.TimesTradesList[i].cpa.rjust(5),self.TimesTradesList[i].vda.rjust(5) ,self.TimesTradesList[i].agressor)

