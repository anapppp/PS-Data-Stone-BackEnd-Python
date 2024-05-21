from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests

__url_cotacoes = 'https://economia.awesomeapi.com.br/json/last/'


@api_view(['GET', 'POST'])
def exchange(request):

    from_currency = request.GET.get('from')
    to_currency = request.GET.get('to')
    amount = request.GET.get('amount')

    if not from_currency or not to_currency or not amount:
        return Response({"mmensagem": "Insira todos os parâmetros"}, status=status.HTTP_400_BAD_REQUEST)

    url = __url_cotacoes + from_currency + '-' + to_currency

    try:
        response = requests.get(url)

        if response.status_code == 200:
            dados = response.json()
            currency_pair = from_currency+to_currency
            nome = dados[currency_pair]['name']
            bid = float(dados[currency_pair]['bid'])
            ask = float(dados[currency_pair]['ask'])
            data_cotacao = dados[currency_pair]['create_date']
            valor_compra = float(amount)*bid
            valor_venda = float(amount)*ask
            response = {
                "nome": nome,
                "data_cotacao": data_cotacao,
                "valor_compra": valor_compra,
                "valor_venda": valor_venda
            }
            return Response(response)
        else:
            return Response({"mensagem": "Pares de moedas inválidas"}, status=status.HTTP_400_BAD_REQUEST)

    except Exception as exception:
        return Response({"mensagem": str(exception)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
