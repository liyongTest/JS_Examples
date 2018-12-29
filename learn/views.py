# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from .forms import AddForm

def home(request):
    return render(request,'Home.html')

def index(request):
    if request.method == 'POST':
        form = AddForm(request.POST)
        if form.is_valid():
            a = form.cleaned_data['a']
            b = form.cleaned_data['b']
            return HttpResponse(str(int(a) + int(b)))
    else:
        form = AddForm()
    return render(request,'Form/index.html')
#淡入淡出
def fadeIn(request):
    return render(request,'FadeInOut.html')
#滑动效果
def slide(request):
    return render(request,'Slide.html')
#动画效果
def animate(request):
    return render(request,'Animate.html')
# 链式方法
def chaining(request):
    return render(request,'Chaining.html')
#捕获与设置
def jquery_html(request):
    return render(request,'jQueryHTML.html')
#添加元素
def appendElement(request):
    return render(request,'AppendElement.html')
#jQueryCSS类
def jQueryCSS(request):
    return render(request,'jQueryCSS.html')
#Ajax测试
def jQueryAjax(request):
    return render(request,'Ajax.html')

#PHP学习
def phpExample(request):
    return  render(request,'PHP_Example/HelloWorld.php')

# Create your views here.
