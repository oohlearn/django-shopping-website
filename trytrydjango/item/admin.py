from django.contrib import admin

# Register your models here.
from .models import Category, Item
# .是因為models.py和admin.py在在同一個資料夾


# 把製作出來的資料庫給註冊到進去
admin.site.register(Category)
admin.site.register(Item)
