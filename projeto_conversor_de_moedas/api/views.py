from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from api.serializers import ExchangeRateSerializer

__url_cotacoes = 'https://economia.awesomeapi.com.br/json/last/'
# Ex.: https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL


@api_view(['GET', 'POST'])
def conversor(request):

    from_currency = request.GET.get('from')
    to_currency = request.GET.get('to')
    amount = request.GET.get('amount')

    url = __url_cotacoes + from_currency + '-' + to_currency

    try:
        # //q = requests.get(url)

        # print(q)
    except Exception:
        print(Exception)

    if request.method == 'POST':
        return Response({'message': f'Hello {request.data.get("nome")}'})
    else:
        return Response({'hello': 'World API'})


class ConversorModelViewSet(ModelViewSet):
    queryset = Conversor.objects.all()
    serializer_class = ConversorModelSerializer
