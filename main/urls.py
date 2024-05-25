from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('cybercategories',views.cyber_categories,name='cybercategories'),
    path('cyberattacks/<int:id>',views.cyberattacks,name='cyberattacks'),
    path('contact/',views.contact,name='contact'),
    path('about/',views.about,name='about'),
    path('simulator',views.simulator,name='simulator'),
    path('cyber_detail/<int:category_id>/<int:id>',views.cyber_detail,name='cyber_detail'),
    path('defensecategories',views.defense_categories,name='defensecategories'),
    path('cyberdefense/<int:id>',views.cyberdefense,name='cyberdefense'),
    path('defense_detail/<int:category_id>/<int:id>',views.defense_detail,name='defense_detail'),
    path('courses/',views.courses,name='courses'),
    path('lessons/<int:course_id>/<int:lesson_id>',views.lessons,name='lessons'),
    path('mitm/',views.mitm,name='mitm'),
    path('dos/',views.dos,name='dos'),
    path('fishing/',views.fishing,name='fishing'),
    path('news',views.news,name='news'),
    path('news_detail/<int:news_id>',views.news_detail,name='news_detail'),
    path('books/',views.books,name='books'),
    path('arp',views.arp,name='arp'),
    path('switch/',views.switch,name='switch'),
]

