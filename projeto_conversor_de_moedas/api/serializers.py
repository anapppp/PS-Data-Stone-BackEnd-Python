from rest_framework.serializers import Serializer, CharField, DateTimeField


class ExchangeRateSerializer(Serializer):
    name = CharField(),
    create_date = DateTimeField(),
    exchange_rate = CharField
