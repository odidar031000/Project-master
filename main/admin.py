from django.contrib import admin
from . import models

admin.site.register(models.CyberAttackCategories)
admin.site.register(models.CyberAttacks)
admin.site.register(models.CyberDefenseCategories)
admin.site.register(models.CyberDefenseTools)
admin.site.register(models.Courses)
admin.site.register(models.Lessons)
admin.site.register(models.News)
admin.site.register(models.Books)
