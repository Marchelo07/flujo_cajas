from django.shortcuts import render
from django.urls import reverse
from django.views import generic

from apps.flujo import models
from apps.flujo import forms
from django.contrib import messages

class Home(generic.TemplateView):
    template_name = 'home/login.html'


class ActivoDeleteView(generic.DeleteView):
    template_name = 'activo/delete_activos.html'
    model = models.Activo

    def get_success_url(self):
        return reverse('view_activo')


class ActivoView(generic.ListView):
    template_name = 'activo/listar_activos.html'  # la ruta donde se encuentra la vista carpeta(activo-> listar_activos.html)
    model = models.Activo  ##importamos el modelos que vamos a llamar para traer la lista
    context_object_name = 'activos'
    paginate_by = 4


class ActivoCreateView(generic.CreateView):
    template_name = 'activo/form_activos.html'
    form_class = forms.FrmActivo
    model = models.Activo

    def form_invalid(self, form):
        messages.error(self.request, 'Lo sentimos no se ha podido procesar la solicitud.')
        return self.render_to_response(self.get_context_data(form=form))

    def form_valid(self, form):
        self.object = form.save()
        messages.success(self.request, 'Su Activo se ha guardado correctamente.')
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('view_activo')


class ActivoUpdateView(generic.UpdateView):
    template_name = 'activo/form_activos.html'
    form_class = forms.FrmActivo
    model = models.Activo

    def form_invalid(self, form):
        """If the form is invalid, render the invalid form."""
        return self.render_to_response(self.get_context_data(form=form))

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        self.object = form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('update_activo')


# CATEGORIA#
class CategoriaView(generic.ListView):
    template_name = 'categoria/listar_categorias.html'  # la ruta donde se encuentra la vista carpeta(activo-> listar_activos.html)
    model = models.Categoria  ##importamos el modelos que vamos a llamar para traer la lista
    context_object_name = 'categorias'
    paginate_by = 4


class CategoriaCreateView(generic.CreateView):
    template_name = 'categoria/form_categoria.html'
    form_class = forms.FrmCategoria
    model = models.Categoria

    def form_valid(self, form):
        self.object = form.save()
        messages.success(self.request, 'Su Activo se ha guardado correctamente.')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Lo sentimos no se ha podido procesar la solicitud.')
        return self.render_to_response(self.get_context_data(form=form))

    def get_success_url(self):
        return reverse('view_categoria')


class CategoriaUpdateView(generic.UpdateView):
    template_name = 'categoria/form_categoria.html'
    form_class = forms.FrmCategoria
    model = models.Categoria

    def form_invalid(self, form):
        """If the form is invalid, render the invalid form."""
        return self.render_to_response(self.get_context_data(form=form))

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        self.object = form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('view_categoria')
