
from django.db import models
from ckeditor.fields import RichTextField

class CyberAttackCategories(models.Model):
    name = models.CharField(max_length=100)
    image=models.ImageField(upload_to='img/cybercategories')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Cyber_Attack_Categories"
        verbose_name = "Cyber_Attack_Category"
        ordering = ['name']
        db_table = 'cyber_attack_categories'

class CyberAttacks(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(CyberAttackCategories, on_delete=models.CASCADE)
    img=models.ImageField(upload_to='img/cyber_attacks')
    context = RichTextField()
    date=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Cyber_Attacks"
        verbose_name = "Cyber_Attack"
        ordering = ['name']
        db_table = 'cyber_attacks'

class CyberDefenseCategories(models.Model):
    name = models.CharField(max_length=100)
    img=models.ImageField(upload_to='img/cyberdefensecategories')
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Cyber_Defense_Categories"
        verbose_name = "Cyber_Defense_Category"
        ordering = ['name']
        db_table = 'cyber_defense_categories'

class CyberDefenseTools(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(CyberDefenseCategories, on_delete=models.CASCADE)
    img=models.ImageField(upload_to='img/cyber_defense_tools')
    context = RichTextField()
    date=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Cyber_Defense_Tools"
        verbose_name = "Cyber_Defense_Tool"
        ordering = ['name']
        db_table = 'cyber_defense_tools'

class Courses(models.Model):
    name = models.CharField(max_length=100)
    image=models.ImageField(upload_to='courses/')
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Courses"
        verbose_name = "Course"
        ordering = ['name']
        db_table = 'courses'


class Lessons(models.Model):
    name = models.CharField(max_length=100)
    context=RichTextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    image=models.ImageField(upload_to='lessons/',blank=True)
    video=models.FileField(upload_to='videos/',blank=True)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Lessons"
        verbose_name = "Lesson"
        ordering = ['name']
        db_table = 'lessons'


class News(models.Model):
    title = models.CharField(max_length=100)
    context=RichTextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    image=models.ImageField(upload_to='news/',blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "News"
        verbose_name = "News"
        ordering = ['-created_at']
        db_table = 'news'


class Books(models.Model):
    name=models.CharField(max_length=255)
    file=models.FileField(upload_to='books/',blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Books"
        verbose_name = "Book"
        ordering = ['name']
        db_table = 'books'



    