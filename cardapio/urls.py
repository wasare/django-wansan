from django.urls import path

from cardapio.views import lojas, loja_detail


urlpatterns = [
	path('lojas', lojas, name="lojas_list"),
	path('loja/<int:loja_id>', loja_detail, name="show_loja"),
]
