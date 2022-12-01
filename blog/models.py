from django.db import models
from django.contrib.auth import get_user_model # o model User pode ser personalizado


# Create your models here.
class Post(models.Model):
    body_text = models.TextField('Texto Principal')
    pub_date = models.DateTimeField('Data Publicação')
    categoria = models.CharField(
        'Categoria',
        max_length=15,
        choices=[
        ('noticias', 'Notícias'),
        ('como_fazer', 'Como Fazer'),
        ('review', 'Review'),
        ],
        default=None,
        null=True
    )
    imagem = models.FileField(
        upload_to='images',
        default=None,
        null=True
    )
    autor = models.ForeignKey(
        get_user_model(),
        on_delete=models.DO_NOTHING, # ou models.CASCADE
        # null=True, # se puder ser null
    )