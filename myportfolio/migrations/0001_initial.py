# Generated by Django 4.0.1 on 2022-02-02 08:34

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='About_me',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20000, verbose_name='SAHIFA')),
                ('content', ckeditor.fields.RichTextField(verbose_name='TEXT')),
                ('photo', models.FileField(upload_to='static/about_image')),
                ('activ', models.BooleanField(verbose_name='ACTIVE')),
                ('date', models.DateField(auto_now_add=True, verbose_name='ACTIV')),
            ],
            options={
                'verbose_name': 'SIZ HAQIZDA MALUMOTLAR',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='NOMI')),
                ('date', models.DateField(auto_now_add=True, verbose_name='SANA')),
                ('active', models.BooleanField(verbose_name='ACTIVE')),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='ISM')),
                ('email', models.EmailField(max_length=254, verbose_name='EMAIL')),
                ('phone', models.CharField(max_length=200, verbose_name='PHONE')),
                ('message', ckeditor.fields.RichTextField(verbose_name='MESSAGE')),
                ('views', models.BooleanField(blank=True, verbose_name='BU XABAR O`QILDIMI?')),
            ],
            options={
                'verbose_name': 'CONTACT',
            },
        ),
        migrations.CreateModel(
            name='EXPERIENCE',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Nomi')),
                ('years', models.CharField(max_length=200, verbose_name='YILI')),
                ('color', models.CharField(max_length=200, verbose_name='RANGI')),
                ('icon', models.CharField(max_length=200, verbose_name='ICON')),
                ('content', ckeditor.fields.RichTextField(verbose_name='CONTENT')),
                ('activ', models.BooleanField(verbose_name='ACTIVE')),
                ('date', models.DateField(auto_now_add=True, verbose_name='Saqlangan Sana')),
            ],
            options={
                'verbose_name': 'EXPERIENCE',
            },
        ),
        migrations.CreateModel(
            name='My_acconuts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(max_length=200, verbose_name='Aloqa vositasi')),
                ('link_name', models.CharField(max_length=200, verbose_name='Aloqa vositasi tegishli joy (masalan:SHAXSIY) ')),
                ('tpy', models.CharField(choices=[('email', 'email'), ('phone', 'phone'), ('adress', 'adress')], max_length=200, verbose_name='TUR')),
                ('active', models.BooleanField(verbose_name='Active')),
            ],
            options={
                'verbose_name': 'Menig (TEL,ADRESS,MAIL)larim',
            },
        ),
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='ISM')),
                ('tug', models.CharField(max_length=200, verbose_name='TUG`ILGAN YILI')),
                ('phone', models.CharField(max_length=200, verbose_name='TELEFON NOMER')),
                ('address', models.TextField(verbose_name='ADDRESS')),
                ('email', models.EmailField(max_length=254, verbose_name='E-MAIL')),
                ('my_website', models.CharField(max_length=2000, verbose_name='SIZNING MAXSUS WEB SAYTIZ')),
                ('photo', models.FileField(upload_to='static/my_image', verbose_name='SIZNING RASMINGIZ')),
                ('my_job', models.CharField(max_length=200, verbose_name='SIZNING HOZIRGI KASBINGIZ')),
                ('date', models.DateField(auto_now_add=True, verbose_name='SAQLANGAN SANA')),
                ('active', models.BooleanField(verbose_name='BU POST ACTIVMI?')),
            ],
            options={
                'verbose_name': 'RESUME',
            },
        ),
        migrations.CreateModel(
            name='SERVICES',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Sarlafhasi')),
                ('content', ckeditor.fields.RichTextField(verbose_name='Services haqida')),
                ('icon', models.CharField(max_length=2000, verbose_name='Icon tashlang')),
                ('activ', models.BooleanField(verbose_name='ACTVE')),
                ('date', models.DateField(auto_now_add=True, verbose_name='Saqlangan sana')),
            ],
            options={
                'verbose_name': 'Men qila oladigan servic hizmatlar',
            },
        ),
        migrations.CreateModel(
            name='My_portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='SARLAVHASI')),
                ('content', ckeditor.fields.RichTextField(verbose_name='CONTENT')),
                ('photo', models.FileField(upload_to='static/portfolio_img')),
                ('link', models.CharField(blank=True, max_length=200, null=True, verbose_name='LINK BERILIADI LEYKIN BU MAJBURIY EMAS ')),
                ('date', models.DateField(auto_now_add=True, verbose_name='Saqlangan sana')),
                ('activ', models.BooleanField(verbose_name='ACTIVE')),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myportfolio.category', verbose_name='CATAGORY ID')),
            ],
            options={
                'verbose_name': 'PORTFOLIO',
            },
        ),
        migrations.CreateModel(
            name='my_blogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=2000, verbose_name='Sarlavha')),
                ('content', ckeditor.fields.RichTextField(verbose_name='Content')),
                ('image', models.FileField(upload_to='static/image_blogs')),
                ('actve', models.BooleanField(verbose_name='Actve')),
                ('location', models.CharField(choices=[('chap', 'chap'), ('o`ng', 'o`ng')], max_length=20)),
                ('auther', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'MY BLOG',
            },
        ),
    ]
