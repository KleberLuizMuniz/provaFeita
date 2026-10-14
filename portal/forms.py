from django import forms

from .models import Professor #O IMPORT ESTAVA DE FORMA ERRADA, ADICIONEI O "." ANTES DE MODELS

class ProfessorForm(forms.ModelForm):
    class Meta:
        model = Professor
        fields = ['nome', 'sobrenome', 'email', 'telefone', 'registro',]
