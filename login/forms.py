from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class forms_login(forms.Form):
    
    # esto es para cuando inicie sesion lo pueda hacer por el correo y no el nombre de ususario que esta por defecto
    email = forms.EmailField(label="Correo electrónico")
    password = forms.CharField(widget=forms.PasswordInput, label="Contraseña")


class CustomUserCreationForm (UserCreationForm):#todo esto es para el registro de usuarios
    telefono = forms.CharField(
        max_length=15,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Teléfono'}),
        label="Teléfono"
    )
    fecha_nacimiento = forms.DateField(
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        label="Fecha de Nacimiento"
    )

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email','telefono','fecha_nacimiento','password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name not in ['telefono', 'fecha_nacimiento']:
                field.widget.attrs.update({'class': 'form-control'})
                field.widget.attrs['placeholder'] = field.label

        self.fields['first_name'].required = True#digo que los elementos sean obligatorios 
        self.fields['last_name'].required = True
        self.fields['email'].required = True

    def clean_email(self):# esto valida que si el correo existe entonces no se podra registrar
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("El correo electrónico ya está registrado. Por favor, utiliza otro.")
        return email


