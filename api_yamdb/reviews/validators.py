import datetime as dt

from django import forms


def validete_year(value):
    if value >= dt.datetime.now().year:
        raise forms.ValidationError(
            'Год выпуска произведения не может быть в будущем.',
            params={'vavue': value},
        )
