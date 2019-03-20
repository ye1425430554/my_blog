#现在你的views.py应该是这样
from django.shortcuts import render
from article.models import Articles
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Hello World, Django")
def detail(request,my_args):
    post = Articles.objects.all()[int(my_args)]
    str = ("title = %s, category = %s, date_time = %s, content = %s" % (post.title, post.category, post.date_time, post.content))
    return HttpResponse(str)
