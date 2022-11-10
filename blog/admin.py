# importa o decorator admin que habilita características de admin no nosso model
from django.contrib import admin
from .models import Post # importa o model que vamos habilitar no admin site

# registar o model Post e habilita
@admin.register(Post) 
class PostAdmin(admin.ModelAdmin): 
    # configura o model Post no admin site.
    list_display = ('body_text','pub_date', 'id')
    list_filter = ('pub_date',)

