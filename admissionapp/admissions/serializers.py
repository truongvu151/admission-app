from rest_framework import serializers
from .models import Admission, AdmissionType, Banner, Faculty, UserAccount, Video



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

class VideoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Video
        fields = ['id', 'url']      
          
class FacultySerializer(ImageSerializer):
        
    class Meta:
        model = Faculty
        fields = ['id', 'name', 'created_date', 'updated_date']

class FacultyDetailSerializer(ImageSerializer):
    videos = VideoSerializer(many=True)
    
    class Meta:
        model = Faculty
        fields = ['id', 'slug', 'description', 'website', 'videos']
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }
        
class BannerSerializer(ImageSerializer):
    class Meta:
        model = Banner
        fields = ['id', 'name', 'image']
        
class UserAccountSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField(source='avatar')

    def get_image(self, user):
        if user.avatar:
            request = self.context.get('request')
            return request.build_absolute_uri('/static/%s' % user.avatar.name) if request else ''

    def create(self, validated_data):
        data = validated_data.copy()
        u = UserAccount(**data)
        u.set_password(u.password)
        u.save()
        return u

    class Meta:
        model = UserAccount
        fields = ['id', 'username', 'password', 'first_name', 'last_name', 'avatar', 'image']
        extra_kwargs = {
            'avatar': {'write_only': True},
            'password': {'write_only': True}
        }