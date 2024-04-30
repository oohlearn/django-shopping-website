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
        # 這行程式碼 verbose_name_plural = "categories" 是在 Item 模型的內部 Meta class 中定義的。
        # 這是一個特殊的類，用於存放模型的一些元資料，例如模型的順序、命名、以及其他一些配置選項。
        # verbose_name_plural 屬性用於指定模型的複數名稱。
        # 當Django需要顯示模型的複數名稱時，它將使用這個屬性的值。
        # 在這個例子中，verbose_name_plural 被設置為 "categories"，
        # 這意味著當Django需要引用 Item 模型的複數名稱時，它將使用 "categories"。
        # 例如，當您在管理介面中查看 Item 模型時，Django 將會使用 verbose_name_plural 的值來標題該模型的列表。

    def __str__(self):
        return self.name
