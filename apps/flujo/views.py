from django.shortcuts import render
from django.views import generic


class Home(generic.TemplateView):
    template_name = 'home/login.html'

    #class Home1(generic.TemplateView):
        #template_name = 'home/prueba.html'


     #def get_context_data(self, **kwargs):
      #  context = super().get_context_data()
      #  return context

