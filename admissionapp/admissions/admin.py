from django import forms
from django.contrib import admin
from .models import Admission, AdmissionType, Banner, Faculty, Livestream, Question, Video

from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.utils.safestring import mark_safe

# Form
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
        
# AdmissionType Admin
class AdmissionTypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'type', 'updated_date', 'active', 'slug']
    
# Admission Admin
class AdmissionAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content', 'updated_date', 'active', 'slug']
    search_fields = ['title']
    list_filter = ['id', 'title', 'created_date']
    form = AdmissionForm

# Faculty Admin
class FacultyAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'website', 'updated_date', 'active', 'slug']
    search_fields = ['name']
    list_filter = ['id', 'name', 'created_date']
    form = FacultyForm

# Livestream Admin
class LivestreamAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'updated_date', 'active', 'slug']
    search_fields = ['title']
    list_filter = ['id', 'title', 'created_date']
    form = LiveStreamForm

# Video admin
class VideoAdmin(admin.ModelAdmin):
    list_display = ['id', 'url', 'faculty', 'updated_date', 'active', 'slug']
    list_filter = ['id', 'created_date']

# Livestream Admin
class LivestreamAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'time']
    
# Banner Admin
class BannerAdmin(admin.ModelAdmin):
    list_display = ['id', 'image']
    readonly_fields = ['image']
    
    def image_display(self, obj):
        if obj:        
            return mark_safe("<img src='/static/{}' width='120' />".format(obj.image.name))
# Question Admin
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    
# Register your models here.
admin.site.register(AdmissionType, AdmissionTypeAdmin)
admin.site.register(Admission, AdmissionAdmin)
admin.site.register(Faculty, FacultyAdmin)
admin.site.register(Livestream, LivestreamAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(Banner, BannerAdmin)
admin.site.register(Question, QuestionAdmin)