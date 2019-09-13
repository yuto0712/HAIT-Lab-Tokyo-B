from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView
from .forms import TextForm
from .main import recipe
from django.conf import settings
# Create your views here.
class MyappView2(TemplateView):
   def __init__(self):
       self.params={'pred': 'idx',
                    'form': TextForm()}
   def get(self, req):
       return render(req, 'recipe_app2/index2.html', self.params)

   def post(self, req):

       text_path = settings.BASE_DIR + r'/save_data/text.txt'
       self.params['pred'] = recipe(text_path)
       return render(req, 'recipe_app2/index2.html', self.params)
