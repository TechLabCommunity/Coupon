from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Coupon
import string
import random

# Create your views here.
def randomString(stringLength=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

def register(request):
    if request.method == 'POST':
        email_inserita = request.POST.get("email", "")
        new_coupon = Coupon()
        new_coupon.code = randomString()
        new_coupon.already_used = False
        new_coupon.save()
        print(f'Sto salvando il coupon {new_coupon.code}, email {email_inserita}')
        template = loader.get_template('thanks.html')
        return HttpResponse(template.render({}, request))
    template = loader.get_template('registrati.html')
    return HttpResponse(template.render({}, request))