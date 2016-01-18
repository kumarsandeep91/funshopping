from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext
from .models import CartItem
from . import cart
from django.contrib.auth.decorators import login_required

@login_required
def show_cart(request, template_name="cart/cart.html"):
	page_title = 'Shopping Cart'
	c = CartItem.objects.all()
	if request.method == 'POST':
		postdata = request.POST.copy()
		if postdata['submit'] == 'Remove':
			cart.remove_from_cart(request)
		if postdata['submit'] == 'Update':
			cart.update_cart(request)
	cart_items = cart.get_cart_items(request)
	subtotal = cart.cart_subtotal(request)

	return render_to_response(template_name, locals(),
		context_instance=RequestContext(request))