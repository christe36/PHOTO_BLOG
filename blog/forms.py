from django import forms
from django.contrib.auth import get_user_model

from .import models

class PhotoForm(forms.ModelForm):
    class Meta:
        model = models.Photo
        fields = ['image', 'caption']

class BlogForm(forms.ModelForm):
    # ajout d'un champ caché pour indiquer qu'il s'agit d'une édition
    edit_blog = forms.BooleanField(widget=forms.HiddenInput, initial=True)
    class Meta:
        model = models.Blog
        fields = ['title', 'content']
  
  
# nous avons attaché un champ edit_blog  et un champ delete_blog  aux formulaires   BlogForm et   DeleteBlogForm  respectivement.
        
class DeleteBlogForm(forms.Form):
    delete_blog = forms.BooleanField(widget=forms.HiddenInput, initial=True)
    
    


User = get_user_model()
class FollowUsersForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['follows']