from rest_framework import serializers
from contato.models import Contato

class ContatoSerializer(serializers.ModelSerializer):
  class Meta:
    model = Contato
    fields = '__all__'