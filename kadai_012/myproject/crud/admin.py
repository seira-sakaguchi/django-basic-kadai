from django.contrib import admin

from .models import Product,Category
from django.utils.safestring import mark_safe

class ProductAdmin(admin.ModelAdmin):
    #list_displayの値はmodels.pyの項目名と合わせる必要がある。
    list_display=("id","name","price","category","image","detail")
    search_fields=("name",)
    list_filter=("category",)

    def image(self, obj):
        # CSSで要素のサイズを指定する場合、widthとheightの間に半角スペースを入れて指定
        return mark_safe('<img src="{}" style="width: 150px; height: auto;">'.format(obj.img.url))

class CategoryAdmin(admin.ModelAdmin):
    list_display=("id","name")
    #search_fieldsの項目の横の,忘れやすいので注意。
    search_fields=("name",)

admin.site.register(Product,ProductAdmin)
admin.site.register(Category,CategoryAdmin)
