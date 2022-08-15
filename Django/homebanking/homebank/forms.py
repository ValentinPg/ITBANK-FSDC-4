from django import forms

prestamos = (("Hipotecario", "Hipotecario" ), ("Prendario","Prendario"), ("Personal","Personal"))

class SolicitudPrestamo(forms.Form):
    monto = forms.DecimalField(required=True, label="Monto")
    fecha_inicio = forms.DateField(required=True, help_text="YYYY-mm-dd", label="Fecha de inicio")
    tipo_prestamo = forms.ChoiceField( required=True, choices=prestamos)