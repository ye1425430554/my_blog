from django.contrib import admin
from article.models import Articles,Category,Tag


# Register your models here.
class ArticlePostAdmin(admin.ModelAdmin):
	list_display = ('title','date_time','category')		#list_display决定了视图的格式
 
#向管理界面注册模型
admin.site.register(Articles,ArticlePostAdmin)
admin.site.register(Category)
admin.site.register(Tag)
