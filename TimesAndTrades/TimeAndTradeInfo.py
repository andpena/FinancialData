class TimesTrades(object):
    def __init__(self, ItensTT):
        self.id      = ItensTT.id
        self.hora    = ItensTT.hora
        self.preco   = ItensTT.preco
        self.qtde    = ItensTT.qtde
        self.cpa     = ItensTT.cpa
        self.vda     = ItensTT.vda
        self.agressor= ItensTT.agressor

class ItensTT(object):
    def __init__(self, Id=None, Hora=None, Preco=None, Qtde=None, Cpa=None, Vda=None, Agressor=None ):
        self.id = Id
        self.hora = Hora
        self.preco = Preco
        self.qtde = Qtde
        self.cpa = Cpa
        self.vda = Vda
        self.agressor = Agressor.replace('#','')        