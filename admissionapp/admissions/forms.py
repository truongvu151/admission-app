from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from .models import Admission, Faculty, Livestream

# forms
class AdmissionForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget)

    class Meta:
        model = Admission
        fields = '__all__'

class FacultyForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget)
    
    class Meta:
        model = Faculty
        fields = '__all__'
        
class LiveStreamForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget)
    
    class Meta:
        model = Livestream
        fields = '__all__'
        