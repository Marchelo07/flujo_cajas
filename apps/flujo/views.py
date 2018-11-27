from django.shortcuts import render
from django.urls import reverse
from django.views import generic

from apps.flujo import models
from apps.flujo import forms


class Home(generic.TemplateView):
    template_name = 'home/login.html'

class HomePrueba(generic.TemplateView):
    template_name = 'home/prueba.html'

class ActivoView(generic.ListView):
    template_name = 'activo/listar_activos.html' #la ruta donde se encuentra la vista carpeta(activo-> listar_activos.html)
    model = models.Activo  ##importamos el modelos que vamos a llamar para traer la lista
    context_object_name = 'activos'
    paginate_by = 18

class ActivoCreateView(generic.CreateView):
    template_name = 'activo/form_activos.html'
    form_class = forms.FrmActivo
    model =  models.Activo


    def form_invalid(self, form):
        """If the form is invalid, render the invalid form."""
        return self.render_to_response(self.get_context_data(form=form))

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        self.object = form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('view_activo')

     #def get_context_data(self, **kwargs):
      #  context = super().get_context_data()
      #  return context

