# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView
from .forms import PhotoForm
from .main import pred

class MyappView(TemplateView):
   def __init__(self):
       self.params={'pred': 'idx',
                    'form': PhotoForm()}
   def get(self, req):
       return render(req, 'recipe_app/index.html', self.params)

   def post(self, req):
       form = PhotoForm(req.POST, req.FILES)
       if not form.is_valid():
           raise ValueError('invalid form')

       image = form.cleaned_data['image']
       self.params['pred'] = pred(image)
       return render(req, 'recipe_app/index.html', self.params)
