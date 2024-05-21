# API para conversão monetária.

## Descrição.

Esta API foi desenvolvida utilizando o Django REST Framework para realizar a conversão de valor entre moedas em tempo real. A conversão é realizada com base nas cotações atualizadas de diversas moedas, utilizando a [API de  Cotações](https://docs.awesomeapi.com.br/api-de-moedas) da Awesome API. Esta API oferece informações como o preço de compra (bid) e o preço de venda (ask) das moedas.


## Como executar

Primeiramente, assegure-se de que o python está instalado utilizando o omando `python -v` para isso. Em seguida, siga esses passos:

1. Clone este repositório
```
git clone git@github.com:anapppp/PS-Data-Stone-BackEnd-Python.git
```

2. Entre no diretório clonado
```
cd PS-Data-Stone-BackEnd-Python
```

3. Instale o `virtualenv` e crie um ambiente virtual
```
pip install virtualenv
```

```
python -m venv .venv
```

4. Ative o ambiente virtual

```
 .\.venv\Scripts\activate
```

5. Instale todas as dependências

```
pip install -r .\requirements.txt
```

6. Inicialize o servidor
```
python .\projeto_conversor_de_moedas\manage.py runserver
```

## Endpoints

Por padrão, o servidor será executado na porta 8000. Portanto, a URL base para acessar a API será: http://localhost:8000/api/exchange/

Para realizar uma conversão monetária, devem ser inseridos na URL da requisição os query params referentes ao par de moedas "from" e "to", e ao valor que se deseja converter "amount". Por exemplo:

```ruby
http://localhost:8000/api/exchange/?from=BRL&to=USD&amount=80
```
```ruby
http://localhost:8000/api/exchange/?from=BTC&to=EUR&amount=123.45
```

