from django import forms

from apps.flujo import models


class FrmActivo(forms.ModelForm):

    class Meta:
        model = models.Activo
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

#MOVIMIENTOS#
class FrmMovimientos(forms.ModelForm):

    class Meta:
        model = models.Movimiento
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

#OBLIGACIONES#
class FrmObligaciones(forms.ModelForm):

    class Meta:
        model = models.Obligaciones
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

#CATEGORIA#
class FrmCategoria(forms.ModelForm):

    class Meta:
        model = models.Categoria
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

#ACREEDOR#
class FrmAcredor(forms.ModelForm):
    class Meta:
        model = models.Acredor
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'