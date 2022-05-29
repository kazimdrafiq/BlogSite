from django.forms import ModelForm
from .models import DataBlog


# class BloogForm(ModelForm):
#     class Meta:
#         fields='__all__'

class ShowForm(ModelForm):
    class Meta:
        model = DataBlog
        fields = '__all__'

