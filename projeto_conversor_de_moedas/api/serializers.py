from rest_framework.serializers import ModelSerializer
from api.models import Conversor


class ConversorModelSerializer(ModelSerializer):
    class Meta:
        model = Conversor
        fields = '__all__'
