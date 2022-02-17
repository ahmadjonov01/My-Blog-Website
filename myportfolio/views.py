from django.shortcuts import render
from .models import Resume, About_me, SERVICES, EXPERIENCE, My_portfolio, Category, My_acconuts, my_blogs
import requests

# Create your views here.
from .form import ContactForm


def telegram_bot_sendtext(bot_message):
    bot_token = '2144135376:AAGg5rVpr7dhCR9NrafqjSoV69vYac9yPyk'
    bot_chatID = '1322649411'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()


def index(requets):
    form = ContactForm()

    data = Resume.objects.filter(active=1)
    data2 = About_me.objects.filter(activ=1)
    data3 = SERVICES.objects.filter(activ=1)
    data4 = EXPERIENCE.objects.filter(activ=1)
    data5 = My_portfolio.objects.filter(activ=1)
    data6 = Category.objects.filter(active=1)
    data7 = My_acconuts.objects.filter(active=1)
    data8 = my_blogs.objects.filter(actve=1)
    if requets.method == 'POST':
        form = ContactForm(requets.POST)
        if form.is_valid():
            message = form.data.get('message')
            email = form.data.get('email')
            name = form.data.get('name')
            phone = form.data.get('phone')
            bot_message = f"ISM:{name} ,\n  📞: {phone},\n   ✉ : {message},\n  📧 : {email}, "
            form.save()
            telegram_bot_sendtext(bot_message)

    context = {
        'data': data,
        'data2': data2,
        'data3': data3,
        'date4': data4,
        'date5': data5,
        'date6': data6,
        'data7': data7,
        'data8': data8,

        'form': form,

    }
    return render(requets, 'index.html', context)
