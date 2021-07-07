from typing import final
from django.shortcuts import render
from django.utils.translation import gettext_lazy as _   # international translation
from django.utils.translation import get_language, activate, gettext 

def home(request):
    trans = translate(language='fr')
    return render(request, 'home.html', {'trans': trans})

def item(request):
    trans = translate(language='fr')
    return render(request, 'item.html')

def translate(language):
    cur_language = get_language()
    try:
        activate(language)
        text = gettext('hello')
    finally:
        activate(cur_language)
    return text