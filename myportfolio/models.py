from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User


class Resume(models.Model):
    class Meta:
        verbose_name = 'RESUME'

    name = models.CharField(max_length=200, verbose_name='ISM')
    tug = models.CharField(max_length=200, verbose_name='TUG`ILGAN YILI')
    phone = models.CharField(max_length=200, verbose_name='TELEFON NOMER')
    address = models.TextField(verbose_name='ADDRESS')
    email = models.EmailField(verbose_name="E-MAIL")
    my_website = models.CharField(max_length=2000, verbose_name='SIZNING MAXSUS WEB SAYTIZ')
    photo = models.FileField(upload_to='static/my_image', verbose_name='SIZNING RASMINGIZ')
    my_job = models.CharField(max_length=200, verbose_name='SIZNING HOZIRGI KASBINGIZ')
    date = models.DateField(auto_now_add=True, verbose_name='SAQLANGAN SANA')
    active = models.BooleanField(verbose_name='BU POST ACTIVMI?')

    def __str__(self):
        return str(self.id) + self.name


class About_me(models.Model):
    class Meta:
        verbose_name = 'SIZ HAQIZDA MALUMOTLAR'

    title = models.CharField(max_length=20000, verbose_name='SAHIFA')
    content = RichTextField(verbose_name='TEXT')
    photo = models.FileField(upload_to='static/about_image')
    activ = models.BooleanField(verbose_name='ACTIVE')
    date = models.DateField(auto_now_add=True, verbose_name='ACTIV')

    def __str__(self):
        return str(self.id) + self.title

class EmailSubscriber(models.Model):
    email = models.EmailField()
    created_at = models.DateTimeField()


class SERVICES(models.Model):
    class Meta:
        verbose_name = 'Men qila oladigan servic hizmatlar'

    title = models.CharField(max_length=200, verbose_name='Sarlafhasi')
    content = RichTextField(verbose_name='Services haqida')
    icon = models.CharField(max_length=2000, verbose_name='Icon tashlang')
    activ = models.BooleanField(verbose_name='ACTVE')
    date = models.DateField(auto_now_add=True, verbose_name='Saqlangan sana')

    # location = models.CharField(choices=data_choices, max_length=200)

    def __str__(self):
        return self.title


class EXPERIENCE(models.Model):
    class Meta:
        verbose_name = 'EXPERIENCE'

    name = models.CharField(max_length=200, verbose_name='Nomi')
    years = models.CharField(max_length=200, verbose_name='YILI')
    color = models.CharField(max_length=200, verbose_name='RANGI')
    icon = models.CharField(max_length=200, verbose_name='ICON')
    content = RichTextField(verbose_name='CONTENT')
    activ = models.BooleanField(verbose_name='ACTIVE')
    date = models.DateField(auto_now_add=True, verbose_name='Saqlangan Sana')

    def __str__(self):
        return self.name


class Category(models.Model):
    title = models.CharField(max_length=200, verbose_name='NOMI')
    date = models.DateField(verbose_name='SANA', auto_now_add=True)
    active = models.BooleanField(verbose_name='ACTIVE')

    def __str__(self):
        return self.title


class My_portfolio(models.Model):
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="CATAGORY ID")
    title = models.CharField(max_length=200, verbose_name='SARLAVHASI')
    content = RichTextField(verbose_name='CONTENT')
    photo = models.FileField(upload_to='static/portfolio_img')
    link = models.CharField(max_length=200, verbose_name='LINK BERILIADI LEYKIN BU MAJBURIY EMAS ', blank=True,
                            null=True)
    date = models.DateField(verbose_name='Saqlangan sana', auto_now_add=True)
    activ = models.BooleanField(verbose_name="ACTIVE")

    class Meta:
        verbose_name = 'PORTFOLIO'

    def __str__(self):
        return self.title


class Contact(models.Model):
    class Meta:
        verbose_name = 'CONTACT'

    name = models.CharField(verbose_name='ISM', max_length=200)
    email = models.EmailField(verbose_name='EMAIL')
    phone = models.CharField(verbose_name="PHONE", max_length=200)
    message = RichTextField(verbose_name='MESSAGE')
    views = models.BooleanField(verbose_name='BU XABAR O`QILDIMI?', blank=True)

    # date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id) + self.name


class My_acconuts(models.Model):
    class Meta:
        verbose_name = 'Menig (TEL,ADRESS,MAIL)larim'

    # icon = models.CharField(max_length=200, verbose_name='ICON')
    link = models.CharField(max_length=200, verbose_name='Aloqa vositasi')
    link_name = models.CharField(max_length=200, verbose_name='Aloqa vositasi tegishli joy (masalan:SHAXSIY) ')
    data_choices = [
        ('email', 'email'),
        ('phone', 'phone'),
        ('adress', 'adress'),
    ]
    tpy = models.CharField(choices=data_choices, max_length=200, verbose_name='TUR')
    active = models.BooleanField(verbose_name='Active')

    def __str__(self):
        return f'{self.link}: tur : {self.tpy}'


class my_blogs(models.Model):
    class Meta:
        verbose_name = 'MY BLOG'

    auther = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=2000, verbose_name='Sarlavha')
    content = RichTextField(verbose_name='Content')
    image = models.FileField(upload_to='static/image_blogs')
    actve = models.BooleanField(verbose_name='Actve')
    data_choices = [
        ('chap', 'chap'),
        ('o`ng', 'o`ng'),
    ]
    location = models.CharField(choices=data_choices, max_length=20)

    def __str__(self):
        return f'{self.id}:{self.title}'
