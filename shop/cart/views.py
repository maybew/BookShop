from django.http import HttpResponse
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from conf.static import INDEX_PAGE, SEARCH_PAGE
from item.models import Item
import models

def add_to_cart(request):
    if request.method == 'GET':
        item_id = request.GET.get('item_id', '')
        quantity = int(request.GET.get('quantity', ''))
        if request.session.get('account'):
            account = request.session.get('account')
            cart = models.Cart.objects.get(id=account.cart.id)
            item = Item.objects.get(id=item_id)
            models.CartItem(cart=cart, item=item, quantity=quantity).save()         
            request.session['cart'] = models.CartItem.objects.filter(cart=cart)
            return redirect('/item/' + item_id)
        else:
            return redirect('/login')
    else:
        return redirect('/index')
