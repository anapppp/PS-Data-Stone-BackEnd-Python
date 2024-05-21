# API para conversão monetária.

## Descrição.

Esta API foi desenvolvida utilizando o Django REST Framework para realizar a conversão de valor entre moedas em tempo real. A conversão é realizada com base nas cotações atualizadas de diversas moedas, utilizando a [API de  Cotações](https://docs.awesomeapi.com.br/api-de-moedas) da Awesome API. Esta API oferece informações como o preço de compra (bid) e o preço de venda (ask) das moedas.


## Como executar

Primeiramente, assegure-se de que o python está instalado utilizando o omando `python --version` para isso. Em seguida, siga esses passos:

1. Clone este repositório
```
git clone git@github.com:anapppp/PS-Data-Stone-BackEnd-Python.git
```

2. Entre no diretório clonado
```
cd PS-Data-Stone-BackEnd-Python
```

3. Crie um ambiente virtual

```
python -m venv .venv
```

Caso seja necessário, instale o virtualenv

```
pip install virtualenv
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

## Saída

O resultado é dado no formato Json. São retornados os campos: 
- `nome` :  de qual moeda para qual moeda o valor será convertido
- `data_cotação`: data e hora da cotação utilizada no cálculo
- `valor_compra`: o valor convertido usando a taxa de câmbio de compra
- `valor_venda`: o valor conversido usando a taxa de câmbio de venda

Este é um exemplo da saida obtida pela API.


```json
{
    "nome": "Real Brasileiro/Dólar Americano",
    "data_cotacao": "2024-05-20 21:37:05",
    "valor_compra": 15.664,
    "valor_venda": 15.68
}
```