# Dados financeiros Históricos/Real Time
Esse projeto é para pessoas que não querem ficar preso nas plataformas com os serviços de RTD/DDE somente no Excel.
Devido uma necessidade de analise de dados em tempo real resolvi criar um programa que conecta nesses serviços de RTD via SOCKET e com isso facilitou a anlise dos dados em Python, que antes era feita em Excel.

Porque decidi fazer essa conexão via SOCKET na plataforma Tryd e não no Metatrader que é mais simples?
R: O Metatrader não fornece as informações dos Playes no Times & Trades. E meu estudo era justamente analizar a atuação deles.

Não sou especialista em Python, então não reparem no código. 

## 01 - Times & Trades
A ideia aqui é ser bem simples, somente mostrar como é possivel buscar as informações da plataforma.(Ai cada um que use sua imaginação)
Arquivo inicia a coleta da informações do Times & Trades: python StartConnTryd.py

Video do programa rodando (Também não sei gravar video, mas vai esse mesmo):
https://youtu.be/VWotFQBHi-w

Dependencias:
https://pypi.org/project/colorama/
pip install colorama

## 02 - Monitor de Cotações
Segue mais um modulo de captura das informações da plataforma Tryd.
Arquivo inicia a coleta da informações do Monitor de Cotações: python StartConnMktTryd.py

Video do programa rodando: 
https://youtu.be/pYZuiiYTlTQ

## 03 - Book - Analítico/Fechado
Em desenvolvimento...!!!
Coloquei um exemplo na branch POC-Book. Ainda não está completa, mas traz a primeira linha do book.
## 03.1 Book Basico
Tem mais um exemplo de como obter os dados do book de ofertas na pasta Book:
link: https://github.com/andpena/FinancialData/blob/master/Book/BookInfo.py
