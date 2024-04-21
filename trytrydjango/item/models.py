from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)

    # django會自己把class名稱加s變複數，下面可以修改成正確拼音
    class Meta:
        ordering = ("name",)  #按照名稱排列
        verbose_name_plural = "categories"

    # 將預設的欄位名稱變成name
    def __str__(self):
        return self.name


class Item(models.Model):
    category = models.ForeignKey(Category, related_name="items", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    image = models.ImageField(upload_to="item_images", blank=True, null=True)
    is_sold = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    # 將Item跟Category 之間建立關係，屬性名稱取名叫做item，之後就可以使用Category.items.all()這類的用法
    # ondelete=models.CASCADE 代表在某個資料時會自動刪除相關資料，如刪除某使用者後，某使用者建立的item就會一起刪除   

    class Meta:
        ordering = ("name",)
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name
