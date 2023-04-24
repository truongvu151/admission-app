from django.db import models
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField

# Create your models here.
# Model Base
class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    slug = models.SlugField(default="", null=False, unique=True)
    
    class Meta:
        abstract = True
        ordering = ["id"]
# Model User
class User(AbstractUser):
    pass

# Model Consultant
class Consultant(User):
    pass

# Model Admission
class Admission(BaseModel):
    title = models.CharField(max_length=255)
    content = RichTextField()
    image = models.ImageField(upload_to='admissions/%Y/%m/', null=True, blank=True)
    admission_type = models.ForeignKey('AdmissionType', on_delete=models.CASCADE, related_name='admissions') # 1 admission type - n admission

    def __str__(self):
        return self.title

# Model AdmissionType
class AdmissionType(BaseModel):
    type = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.type    
    
# Model Faculty
class Faculty(BaseModel):
    name = models.CharField(max_length=100, unique=True)
    description = RichTextField() # nội dung, điểm trung bình, ảnh khoa (nếu có)
    website = models.URLField(blank=True)
    
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
    
    def __str__(self):
        return self.title
# Model Banner
class Banner(BaseModel):
    image = models.ImageField(upload_to='banners/%Y/%m/', null=True, blank=True)

    def __str__(self):
        return self.image
    
# Model Question
class Question(BaseModel):
    title = models.CharField(max_length=255)
    content = RichTextField()
    livestream = models.ForeignKey(Livestream, on_delete=models.PROTECT, related_name='questions')
    
    def __str__(self):
        return self.title
    