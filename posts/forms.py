from django import forms
# from .models import Post


class SortForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initial['sort'] = 'any'
        self.initial['op'] = 'any'
        self.initial['media'] = 'any'

    SORT_CHOICES = [
        ('any', 'Не имеет значения'),
        ('date', 'Дата'),
        ('notions', 'Ответы'),
    ]
    OP_CHOICES = [
        ('any', 'Не имеет значения'),
        ('with', 'С ним'),
        ('without', 'Без него'),
    ]
    MEDIA_CHOICES = [
        ('any', 'Не имеет значения'),
        ('with', 'С картинками'),
        ('without', 'Без картинок'),
    ]

    sort = forms.ChoiceField(label='Сортировать по:',
                             choices=SORT_CHOICES,
                             initial='any',
                             required=False)

    op = forms.ChoiceField(label='ОП',
                           choices=OP_CHOICES,
                           initial='any',
                           required=False)

    media = forms.ChoiceField(label='Медиа',
                              choices=MEDIA_CHOICES,
                              initial='any',
                              required=False)
