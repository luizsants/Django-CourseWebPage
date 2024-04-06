from django.shortcuts import render

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
