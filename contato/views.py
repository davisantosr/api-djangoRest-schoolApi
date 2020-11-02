from django.http import JsonResponse

def contatos(request):
  if request.method == 'GET':
    contato = {'id':1, 'nome': 'contatoNome', 'telefone': '55123456'}
    return JsonResponse(contato)