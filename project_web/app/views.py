from django.shortcuts import render
# from django.views.decorators.cache import never_cache

# @never_cache
def home(request):
    cursos = [
        {
            'nome': 'Tecnologia em Análise e Desenvolvimento de Sistemas',
            'imagem': 'caminho/para/imagem1.jpg',
        },
        {
            'nome': 'Redes de Computadores',
            'imagem': 'caminho/para/imagem2.jpg',
        },
        {
            'nome': 'Sistemas de Informação',
            'imagem': 'caminho/para/imagem3.jpg',
        }
    ]
    contexto = {
        'cursos': cursos
    }
    return render(request, 'cursos.html', contexto)