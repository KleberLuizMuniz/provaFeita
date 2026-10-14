
# Descrição do projeto (sistema escolar Django)
Op projeto está fazendo uma tabela que contenha professor aluno e aula.

# Lista dos 8 erros: número, arquivo, descrição do problema e da correção

1-
 ERRO ENCONTRADO: models.DateTimeField(default=timezone.now)sem import
 CORREÇÃO: colocar -> "from datetime import timezone"

2- 
 ERRO ENCONTRADO:  matricula = models.IntegerField() 
 CORREÇÃO: em vez de .IntegerField deveria ser charfild


3- 
 ERRO ENCONTRADO: 'templates/portal/index.html'
 CORREÇÃO: não era preciso a parte "templates/" pois o django já executa, ficando 'portal/index.html'



4-
 ERRO ENCONTRADO:from models import Professor
 CORREÇÃO: faltou o "." no Models


5-
 ERRO ENCONTRADO:  list_display = ('id', 'nome', 'email', 'telefone', 'especialidade', 'ativo',)
 CORREÇÃO: a parte de especialidade não existe no models.py, no lugar existe disciplina

6-
 ERRO ENCONTRADO: A falta do cadastro na views.py 
#From django.http import HttpResponse

def cadastro(request):
    return HttpResponse ("Ta aí bro")

7-
 ERRO ENCONTRADO:path('cadastro/', preciso mostrar a página cadastro.html),
CORREÇÃO: path('cadastro/', views.cadastro), e adicionamos from portal import views

8 -
 ERRO ENCONTRADO:
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
 CORREÇÃO:
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'portal',
]

# Instrução de como rodar o projeto localmente
pip install django
-m pip install Pillow
python manage.py makemigrations
python manage.py migrate
python manage.py runserver

# Seu nome completo
Mariana Santos
Kleber Luiz Muniz


