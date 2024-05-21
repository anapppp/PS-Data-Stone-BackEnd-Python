# PS-Data-Stone-BackEnd-Python
API para conversão monetária.

# Descrição.

Foi feita usando o Django REST Framework .

A conversão foi feita usando a [API de  Cotações](https://docs.awesomeapi.com.br/api-de-moedas) da Awesome API, que atualiza as cotações de diversas moedas em tempo real.
 - preço de compra (bid) ou o preço de venda (ask) 

# Como executar

Primeiramente, assegure-se de que o python está instalado. Você pode usar o compando ``python -v` para isso.

1. Clone este repositório
```
git clone git@github.com:anapppp/PS-Data-Stone-BackEnd-Python.git
```

2. Entre no diretório clonado
```
cd PS-Data-Stone-BackEnd-Python
```

2. Crie um ambiente virtual
```
pip install virtualenv
```

```
python -m venv .venv
```

3. Ative o ambiente virtual

```
 .\.venv\Scripts\activate
```

4. Instale todas as dependências

```
pip install -r .\requirements.txt
```

5. Inicialize o servidor
```
python .\projeto_conversor_de_moedas\manage.py runserver
```

## Endpoints


Exemplo:


http://127.0.0.1:8000/api/exchange/?from=BTC&to=EUR&amount=123.45


