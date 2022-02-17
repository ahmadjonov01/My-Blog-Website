from django.contrib import admin
from .models import Resume, About_me, SERVICES, Category, EXPERIENCE, My_portfolio, Contact, My_acconuts, my_blogs, \
    EmailSubscriber

admin.site.register(Category)
admin.site.register(EXPERIENCE)
admin.site.register(Contact)
admin.site.register(My_portfolio)
admin.site.register(My_acconuts)

from .models import EmailSubscriber


@admin.register(EmailSubscriber)
class EmailSubscriberAdmin(admin.ModelAdmin):
    list_display = ("id", "email", "created_at")  # display these table columns in the list view
    ordering = ("-created_at",)  # sort by most recent subscriber


# admin.site.register(EmailSubscriberAdmin)


class adminBlog(admin.ModelAdmin):
    list_display = ['id', 'title']
    list_display_links = ['id', 'title', ]


admin.site.register(my_blogs, adminBlog)


class adminResume(admin.ModelAdmin):
    list_display = ['id', 'name', 'phone']
    list_display_links = ['id', 'name', ]


class adminAbout_me(admin.ModelAdmin):
    list_display = ['id', 'title']
    list_display_links = ['id', 'title', ]


class adminServices(admin.ModelAdmin):
    list_display = ['id', 'title']
    list_display_links = ['id', 'title', ]


admin.site.register(Resume, adminResume)
admin.site.register(About_me, adminAbout_me)
admin.site.register(SERVICES, adminServices)
