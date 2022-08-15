from django import forms

prestamos = (("1", "Hipotecario"), ("2","Prendario"), ("3","Personal"))

class SolicitudPrestamo(forms.Form):
    monto = forms.DecimalField(required=True, label="Monto")
    fecha_inicio = forms.DateField(required=True, help_text="mm/dd/YYYY", label="Fecha de inicio")
    tipo_prestamo = forms.ChoiceField(choices= prestamos, required=True)
    