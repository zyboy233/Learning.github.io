from django.contrib import admin
from .models import Publisher,Book
# Register your models here.


class PublisherAdmin(admin.ModelAdmin):
    list_display = ['pname','paddress']
class BookAdmin(admin.ModelAdmin):
    list_display = ['bname']

admin.site.site_header = "管理界面"
admin.site.register(Publisher,PublisherAdmin)
admin.site.register(Book,BookAdmin)
