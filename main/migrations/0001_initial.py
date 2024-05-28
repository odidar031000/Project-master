# Generated by Django 5.0.4 on 2024-05-28 06:38

import ckeditor.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('file', models.FileField(blank=True, upload_to='books/')),
            ],
            options={
                'verbose_name': 'Book',
                'verbose_name_plural': 'Books',
                'db_table': 'books',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(default='test@gmail.com', max_length=254)),
                ('title', models.CharField(max_length=255)),
                ('message', models.TextField()),
            ],
            options={
                'verbose_name': 'contact',
                'verbose_name_plural': 'contacts',
                'db_table': 'Contact',
            },
        ),
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='courses/')),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Course',
                'verbose_name_plural': 'Courses',
                'db_table': 'courses',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='CyberAttackCategories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='img/cybercategories')),
            ],
            options={
                'verbose_name': 'Cyber_Attack_Category',
                'verbose_name_plural': 'Cyber_Attack_Categories',
                'db_table': 'cyber_attack_categories',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='CyberDefenseCategories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='img/cyberdefensecategories')),
            ],
            options={
                'verbose_name': 'Cyber_Defense_Category',
                'verbose_name_plural': 'Cyber_Defense_Categories',
                'db_table': 'cyber_defense_categories',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('context', ckeditor.fields.RichTextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(blank=True, upload_to='news/')),
            ],
            options={
                'verbose_name': 'News',
                'verbose_name_plural': 'News',
                'db_table': 'news',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='CyberAttacks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='img/cyber_attacks')),
                ('context', ckeditor.fields.RichTextField()),
                ('date', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.cyberattackcategories')),
            ],
            options={
                'verbose_name': 'Cyber_Attack',
                'verbose_name_plural': 'Cyber_Attacks',
                'db_table': 'cyber_attacks',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='CyberDefenseTools',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='img/cyber_defense_tools')),
                ('context', ckeditor.fields.RichTextField()),
                ('date', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.cyberdefensecategories')),
            ],
            options={
                'verbose_name': 'Cyber_Defense_Tool',
                'verbose_name_plural': 'Cyber_Defense_Tools',
                'db_table': 'cyber_defense_tools',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Lessons',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('context', ckeditor.fields.RichTextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(blank=True, upload_to='lessons/')),
                ('video', models.FileField(blank=True, upload_to='videos/')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.courses')),
            ],
            options={
                'verbose_name': 'Lesson',
                'verbose_name_plural': 'Lessons',
                'db_table': 'lessons',
                'ordering': ['name'],
            },
        ),
    ]
