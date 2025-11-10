from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm 
from django import forms

# formulaire d'inscription personnalisé
class SignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()  # nous permet d'obtenir le modèle User personnalisé
        fields = ('username', 'email', 'first_name', 'last_name', 'role')

# formulaire pour téléverser une photo de profil
class UploadProfilePhotoForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ('profile_photo', )















# class LoginForm(forms.Form):
#     username = forms.CharField(label='Nom d\'utilisateur', max_length=150)
#     password = forms.CharField(label='Mot de passe', widget=forms.PasswordInput)