from django.http import HttpResponse
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from conf.static import INDEX_PAGE, SEARCH_PAGE
import models

def index(request):
    sort = request.GET.get('sort', '-time')
    page = int(request.GET.get('page', 1))
    item = models.Item.objects.filter(status__in=[0, 1], inventory__gt=0).order_by(sort)
    category = models.Category.objects.all()
    total_page = range(1, len(item) / INDEX_PAGE + 1)
    
    item = item[INDEX_PAGE*(page-1):INDEX_PAGE*page]
    return render(request, 'test_index.html', { 'item':item, 'category':category, 'total_page':total_page, 'page':page, 'sort':sort })
    
def search(request):
    sort = request.GET.get('sort', '-time')
    page = int(request.GET.get('page', 1))
    category = request.GET.get('category', 'all')
    keyword = request.GET.get('keyword', '')
    item = models.Item.objects.filter(status__in=[0, 1], inventory__gt=0).order_by(sort)
    if category != 'all':
        item = item.filter(category_name=category)
    if keyword != '':
        item = item.filter(Q(title__contains=keyword) | Q(author__contains=keyword) | Q(description__contains=keyword))
    total_page = range(1, len(item) / SEARCH_PAGE + 1)
    
    item = item[SEARCH_PAGE*(page-1):SEARCH_PAGE*page]
    return render(request, 'test_search.html', { 'item':item, 'category':category, 'total_page':total_page, 'page':page, 'sort':sort, 'keyword':keyword })

def item(request, item_id):
    item = get_object_or_404(models.Item, id=item_id)
    return render(request, 'test_item.html', { 'item':item })