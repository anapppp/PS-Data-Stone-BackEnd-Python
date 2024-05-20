from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from api.models import Conversor
from api.serializers import ConversorModelSerializer


@api_view(['GET', 'POST'])
def hello_world(request):
    if request.method == 'POST':
        return Response({'message': f'Hello {request.data.get("nome")}'})
    else:
        return Response({'hello': 'World API'})


class ConversorModelViewSet(ModelViewSet):
    queryset = Conversor.objects.all()
    serializer_class = ConversorModelSerializer
