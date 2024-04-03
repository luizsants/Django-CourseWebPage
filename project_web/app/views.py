from django.shortcuts import render

# from django.views.decorators.cache import never_cache


# @never_cache
def home(request):
    cursos = [
        {
            "nome": "Tecnologia em Análise e Desenvolvimento de Sistemas",
        },
        {
            "nome": "Redes de Computadores",
        },
        {
            "nome": "Sistemas de Informação",
        },
    ]
    contexto = {"cursos": cursos}
    return render(request, "cursos.html", contexto)
