from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def index(request):
  return render(request, 'index.html', {})

@login_required
def demo(request):
  return render(request, 'demo.html', {})
