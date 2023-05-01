from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField
from autoslug import AutoSlugField


# Create your models here.
# Model Base
class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    
    class Meta:
        abstract = True
        ordering = ["id"]
# Model User
class UserAccount(AbstractUser):
    avatar = models.ImageField(upload_to='users/%Y/%m', null=True)
    is_online = models.DateTimeField(default=timezone.now)

class UserProfile(BaseModel):
    user = models.OneToOneField(UserAccount, related_name="user_profile", on_delete=models.CASCADE)
    about = models.TextField()

    def __str__(self):
        return self.user.username
        
###########################################################################
# Model groups

# Model Admission
class Admission(BaseModel):
    title = models.CharField(max_length=255)
    content = RichTextField()
    image = models.ImageField(upload_to='admissions/%Y/%m/', null=True, blank=True)
    admission_type = models.ForeignKey('AdmissionType', on_delete=models.CASCADE, related_name='admissions') # 1 admission type - n admission
    slug = AutoSlugField(populate_from='title', unique=True, null=True, blank=True)
    
    def __str__(self):
        return self.title

# Model AdmissionType
class AdmissionType(BaseModel):
    type = models.CharField(max_length=100, unique=True)
    slug = AutoSlugField(populate_from='type', unique=True, null=True, blank=True)

    def __str__(self):
        return self.type    
    
# Model Faculty
class Faculty(BaseModel):
    name = models.CharField(max_length=100, unique=True)
    description = RichTextField() # nội dung, điểm trung bình, ảnh khoa (nếu có)
    website = models.URLField(blank=True)
    slug = AutoSlugField(populate_from='name', unique=True, null=True, blank=True)

    
    class Meta:
        ordering = ["name"]
        
    def __str__(self):
        return self.name

# Model Major
class Major(BaseModel):
    code = models.CharField(max_length=50)
    name = models.CharField(max_length=255)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, related_name="majors")
    
    def __str__(self):
        return self.name
    
# Model Video
class Video(BaseModel):
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, related_name="videos")
    url = models.URLField(blank=True)
    
    class Meta:
        ordering = ['faculty']
        
    def __str__(self):
        return self.url
    
# Model Comment
# class Comment(BaseModel):
#     content = models.CharField(max_length=255)
#     admission = models.ForeignKey(Admission, on_delete=models.CASCADE)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     consultant = models.ForeignKey(Consultant, on_delete=models.CASCADE)
    
#     def __str__(self):
#         return self.content
# Model Livestream
class Livestream(BaseModel):
    title = models.TextField(max_length=100)
    description = RichTextField()
    time = models.DateTimeField()
    slug = AutoSlugField(populate_from='title', unique=True, null=True, blank=True)

    def __str__(self):
        return self.title
# Model Banner
class Banner(BaseModel):
    name = models.CharField(max_length=255, null=True)
    image = models.ImageField(upload_to='banners/%Y/%m/', null=True)

    
# Model Question
class Question(BaseModel):
    title = models.CharField(max_length=255)
    content = RichTextField()
    livestream = models.ForeignKey(Livestream, on_delete=models.PROTECT, related_name='questions')
    
    def __str__(self):
        return self.title
    
