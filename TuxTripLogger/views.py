from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def index(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render())

@login_required
def demo(request):
  template = loader.get_template('demo.html')
  return HttpResponse(template.render())