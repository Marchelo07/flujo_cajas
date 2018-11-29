from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views import generic

from apps.flujo import models
from apps.flujo import forms
from django.contrib import messages


class Home(generic.TemplateView):
    template_name = 'home/login.html'

######### MOVIMIENTOS #########
class MovimientosView(generic.ListView):
    template_name = 'movimientos/listar_movimientos.html'  # la ruta donde se encuentra la vista carpeta(activo-> listar_activos.html)
    model = models.Movimiento  ##importamos el modelos que vamos a llamar para traer la lista
    context_object_name = 'movimientos'
    paginate_by = 4

class MovimientosCreateView(generic.CreateView):
    template_name = 'movimientos/form_movimientos.html'
    form_class = forms.FrmMovimientos
    model = models.Movimiento

    def form_invalid(self, form):
        messages.error(self.request, 'Lo sentimos no se ha podido procesar la solicitud.')
        return self.render_to_response(self.get_context_data(form=form))

    def form_valid(self, form):
        self.object = form.save()
        messages.success(self.request, 'Su Movimiento se ha guardado correctamente.')
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('view_movimientos')

class MovimientosUpdateView(generic.UpdateView):
    template_name = 'movimientos/form_movimientos.html'
    form_class = forms.FrmMovimientos
    model = models.Movimiento

    def form_valid(self, form):
        self.object = form.save()
        messages.success(self.request, 'Su movimientos se ha actualizado correctamente.')
        return super().form_valid(form)

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))

    def get_success_url(self):
        return reverse('view_movimientos')

class MovimientosDeleteView(generic.DeleteView):
    model =  models.Movimiento
    template_name = 'movimientos/delete_movimientos.html'

    def get_success_url(self):
        return reverse('view_movimientos')

######### OBLIGACIONES #########
class ObligacionesView(generic.ListView):
    template_name = 'obligaciones/listar_obligaciones.html'  # la ruta donde se encuentra la vista carpeta(activo-> listar_activos.html)
    model = models.Obligaciones  ##importamos el modelos que vamos a llamar para traer la lista
    context_object_name = 'obligaciones'
    paginate_by = 4

class ObligacionesCreateView(generic.CreateView):
    template_name = 'obligaciones/form_obligaciones.html'
    form_class = forms.FrmObligaciones
    model = models.Obligaciones

    def form_invalid(self, form):
        messages.error(self.request, 'Lo sentimos no se ha podido procesar la solicitud.')
        return self.render_to_response(self.get_context_data(form=form))

    def form_valid(self, form):
        self.object = form.save()
        messages.success(self.request, 'Su Obligacion se ha guardado correctamente.')
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('view_obligaciones')

class ObligacionesUpdateView(generic.UpdateView):
    template_name = 'obligaciones/form_obligaciones.html'
    form_class = forms.FrmObligaciones
    model = models.Obligaciones

    def form_valid(self, form):
        self.object = form.save()
        messages.success(self.request, 'Su registro se ha actualizado correctamente.')
        return super().form_valid(form)

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))

    def get_success_url(self):
        return reverse('view_obligaciones')

class ObligacionesDeleteView(generic.DeleteView):
    template_name = 'obligaciones/delete_obligaciones.html'
    model =  models.Obligaciones

    def get_success_url(self):
        return reverse('view_obligaciones')

######### ACTIVO #########
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
        messages.success(self.request, 'Su registro se ha actualizado correctamente.')
        self.object = form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('view_activo')

class ActivoDeleteView(generic.DeleteView):
    template_name = 'activo/delete_activos.html'
    model = models.Activo

    def get_success_url(self):
        return reverse('view_activo')


######## CATEGORIA #########
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
        self.object = form.save()
        messages.success(self.request, 'Su registro se ha actualizado correctamente.')
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('view_categoria')

class CategoriaDeleteView(generic.DeleteView):
    template_name = 'categoria/delete_categorias.html'
    model = models.Categoria

    def get_success_url(self):
        return reverse('view_categoria')


######### ACREEDOR #########
class AcredorView(generic.ListView):
    template_name = 'acredor/listar_acredor.html'
    context_object_name = "acredores"
    model = models.Acredor
    paginate_by = 10

class AcredorCreate(generic.CreateView):
    template_name = 'acredor/form_acredor.html'
    form_class = forms.FrmAcredor
    models = models.Acredor

    def form_valid(self, form):
        self.object = form.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))

    def get_success_url(self):
        return reverse('view_acredor_listar')

class AcredorUpdateView(generic.UpdateView):
    template_name = 'acredor/form_acredor.html'
    form_class = forms.FrmAcredor
    model = models.Acredor

    def form_valid(self, form):
        self.object = form.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))

    def get_success_url(self):
        return reverse('view_acredor_listar')
