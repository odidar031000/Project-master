
from django.shortcuts import render
from . import models

def index(request):
    return render(request, 'index.html')

def cyber_categories(request):
    categories=models.CyberAttackCategories.objects.all()
    
    context={
        'categories':categories
    }
    return render(request, 'cybercategories.html',context)

def cyberattacks(request,id):
    cyberattacks = models.CyberAttacks.objects.filter(category__id=id)

    print(cyberattacks)
    context={
        'id':id,
        'cyberattacks':cyberattacks
    }
    
    return render(request, 'cyberattacks.html',context)


def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')

def simulator(request):
    return render(request, 'simulator.html')


def cyber_detail(request,category_id,id):
    cyberattacks = models.CyberAttacks.objects.filter(category__id=category_id)
    cyber_detail = models.CyberAttacks.objects.get(id=id)
    context={
        'cyber_detail':cyber_detail,
        'cyberattacks':cyberattacks,
        'category_id':category_id
    }
    return render(request, 'cyberdetail.html',context)


def defense_categories(request):
    categories=models.CyberDefenseCategories.objects.all()
    
    context={
        'categories':categories
    }
    return render(request, 'defensecategories.html',context)

def cyberdefense(request,id):
    cyberdefense = models.CyberDefenseTools.objects.filter(category__id=id)
    
    context={
        'id':id,
        'cyberdefense':cyberdefense
    }
    
    return render(request, 'cyberdefnsetools.html',context)


def defense_detail(request,category_id,id):
    cyberdefense = models.CyberDefenseTools.objects.filter(category__id=category_id)
    defense_detail = models.CyberDefenseTools.objects.get(id=id)
    context={
        'defense_detail':defense_detail,
        'cyberdefense':cyberdefense,
        'category_id':category_id
    }
    return render(request, 'defensedetail.html',context)

    
def courses(request):
    courses=models.Courses.objects.all()
    context={'courses':courses}
    return render(request, 'courses.html',context)

def lessons(request, course_id,lesson_id):
    lessons=models.Lessons.objects.filter(course__id=course_id)
    lesson=models.Lessons.objects.filter(course__id=course_id,id=lesson_id)
    

    context={'lessons':lessons, "lesson":lesson}
    return render(request, 'lessons.html',context)

def mitm(request):
    return render(request, 'mitm.html')

def dos(request):
    return render(request, 'dos.html')

def fishing(request):
    return render(request, 'fishing.html')

def news(request):
    news=models.News.objects.all()
    context={
        'news':news
    }

    return render(request, 'news.html', context)
    
def news_detail(request,news_id=None):
    all_news=models.News.objects.all()
    news=models.News.objects.get(id=news_id)
    context={
        'news':news,
        'all_news':all_news,
    }
    return render(request, 'news_detail.html', context)


def books(request):
    books=models.Books.objects.all()
    context={
        'books':books
    }
    return render(request, 'books.html', context)


def arp(request):
    return render(request, 'arp.html')


def switch(request):
    return render(request, 'switch.html')