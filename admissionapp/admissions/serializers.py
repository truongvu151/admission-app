from rest_framework import serializers
from .models import Admission, AdmissionType, Faculty, Video



# Write serializers 
class ImageSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField(source='image')

    def get_image(self, obj):
        if obj.image:
            request = self.context.get('request')
            return request.build_absolute_uri('/static/%s' % obj.image.name) if request else ''
        
        
class AdmissionTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdmissionType
        fields = ['id', 'type']


class AdmissionSerializer(ImageSerializer):
    class Meta:
        model = Admission
        fields = ['id', 'title', 'content', 'image']
        
class FacultySerializer(ImageSerializer):
    class Meta:
        model = Faculty
        fields = ['id', 'name', 'description', 'website']
        
class VideoSerializer(ImageSerializer):
    model = Video
    fields = ['id', 'url']