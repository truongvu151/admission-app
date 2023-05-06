from rest_framework import serializers
from .models import FAQ, Admission, AdmissionType, Banner, Comment, Livestream, Question, ReplyComment, Faculty, UserAccount, Video



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
        
# This is a serializer class for a user account model that includes a method to get the user's avatar
# image and overrides the create method to set the user's password and save the user account.
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
        
class ReplyCommentSerializer(serializers.ModelSerializer):
    user = UserAccountSerializer()
    class Meta:
        model = ReplyComment
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    user = UserAccountSerializer()
    replies = ReplyCommentSerializer(many=True, read_only=True)

    class Meta:
        model = Comment
        fields = ["id", "content", "created_date", "user", "replies"]
        
class LivestreamSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Livestream
        fields = ['__all__']

class QuestionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Question
        fields = ['__all__']

class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = ['id', 'question', 'answer']
