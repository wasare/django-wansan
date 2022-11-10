# Python
from datetime import datetime

# Django
from django import forms

# Local
# <!-- importa o model Post -->
from blog.models import Post

# <!-- cria o ModelForm herdando da classe base -->
class PostModelForm(forms.ModelForm):
    error_css_class = 'alert-danger'

    def __init__(self, *args, **kwargs):
        super(PostModelForm, self).__init__(*args, **kwargs)
        # <!-- configura um valor inicial para o campo pub_date -->
        self.fields['pub_date'].initial = datetime.today()

        self.fields['imagem'].widget.initial_text = 'Atual'
        self.fields['imagem'].widget.input_text = 'Alterar'


    class Meta:
        # <!-- vincula o model ao Form e define os campos a exibir -->
        model = Post
        fields = ['body_text', 'pub_date', 'categoria', 'imagem']
        widgets = {
            'pub_date': forms.widgets.DateTimeInput(attrs={'type': 'datetime-local'}),
            'categoria': forms.RadioSelect(),
        }
        labels = {
            'body_text': '',
            'categoria': 'Assunto'
        }

    def clean(self):
        cleaned_data = super().clean()
        pub_date = cleaned_data.get('pub_date')
        pub_date = pub_date.replace(tzinfo=None)
        if pub_date > datetime.today():
            self.add_error(
                'pub_date',
                forms.ValidationError('Não é permitido datas futuras')
            )

