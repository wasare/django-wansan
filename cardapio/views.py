from django.shortcuts import render, get_object_or_404
from django.template.response import TemplateResponse

from cardapio.models import Loja

# Create your views here.
def lojas(request):
    todas_lojas = Loja.objects.all()
    print()
    print(todas_lojas)
    print()
    return TemplateResponse(
			request,
			'cardapio/lojas.html',
			{'lojas': todas_lojas }
		)

def loja_detail(request, loja_id):
	loja = get_object_or_404(Loja, pk=loja_id)
	return render(request, 'cardapio/loja_detail.html', {'loja': loja})
