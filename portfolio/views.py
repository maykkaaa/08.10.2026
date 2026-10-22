from django.shortcuts import render
from django.http import HttpResponse


def home_view(request):
    return render(request, 'portfolio/home.html')


def projects_view(request):
    return render(request, 'portfolio/projects.html')


def project_detail_view(request, project_name):
    projects = {
        'lifecell': {
            'title': 'Lifecell Portal',
            'category': 'WEB DEVELOPMENT',
            'description': 'Розробка вебпорталу Lifecell з сучасним інтерфейсом, адаптивним дизайном та зручною навігацією.',
            'technologies': ['Python', 'Django', 'HTML', 'CSS', 'Bootstrap'],
            'image': 'images/project1.png',
        },

        'vi-climate': {
            'title': 'VI Climate',
            'category': 'WEB DEVELOPMENT',
            'description': 'Розробка сайту для власного бізнесу з продажу та підбору кондиціонерів. Сайт містить каталог товарів, інформацію про кондиціонери та зручний інтерфейс для користувачів.',
            'technologies': ['Python', 'Django', 'HTML', 'CSS', 'Bootstrap'],
            'image': 'images/project2.png',
        },

        'games': {
            'title': 'Game Projects',
            'category': 'GAME DEVELOPMENT',
            'description': 'Мої власні ігрові проєкти. Створюю ігри, працюю з ігровою логікою, механіками та дизайном.',
            'technologies': ['Python', 'Pygame', 'Godot'],
            'image': 'images/game.png',
        },
    }

    project = projects.get(project_name)

    if project is None:
        return render(
            request,
            'portfolio/project_not_found.html',
            status=404
        )

    return render(
        request,
        'portfolio/project_detail.html',
        {'project': project}
    )


def skills_view(request):
    return render(request, 'portfolio/skills.html')


def polls(request):
    return HttpResponse("Polls page")