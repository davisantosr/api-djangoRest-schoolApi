from rest_framework import viewsets
from contato.models import Contato
from .serializer import ContatoSerializer

class ContatosViewSet(viewsets.ModelViewSet):
  """Exibindo todos os Contatos"""
  queryset = Contato.objects.all()
  serializer_class = ContatoSerializer