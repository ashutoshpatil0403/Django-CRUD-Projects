from django.contrib import admin
from.models import UPSC_Books

# Register your models here.

@admin.register(UPSC_Books)

class UPSC_BooksAdmin(admin.ModelAdmin):
    list_display=['subject','bookname','authorname','price']