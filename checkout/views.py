from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


# Create your views here.

def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your shopping bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51MoRDbCzlbf1Kdw1JCuapoaxuOivNf6zZ6QC60SD2rKrHPdcyBFtXctyuNK57PKCA4XADYhup4LJ8uPokCakvZXw00dfYFUSFV',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)



