from .models import Localities
from django.forms import ModelForm, TextInput

class LocalitiesForm(ModelForm):
    class Meta:
        model = Localities
        fields = ['title', 'leader', 'number_of_inhabitants', 'budget', 'spending', 'deficit', 'img_link']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название населенного пункта'
            }),
            "leader": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Глава'
            }),
            "number_of_inhabitants": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Население'
            }),
            "budget": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Бюджет'
            }),
            "spending": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Расходы'
            }),
            "deficit": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дефицит'
            }),
            "img_link": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ссылка на картинку'
            }),
        }