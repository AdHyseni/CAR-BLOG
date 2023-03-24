from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

# Create your models here.
class Kategori(models.Model):
    emri = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f'{self.emri}'
    
class Autori(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    emri_i_punes = models.CharField(max_length=50, null=False)
    
    def __str__(self) -> str:
        return f'{self.emri_i_punes}'

class Blog(models.Model):
    titulli = models.CharField(max_length=255, null=False)
    tekst = models.TextField(max_length=300, null=False)
    foto = models.ImageField(upload_to='blog', null=True)

    autori = models.ForeignKey(Autori, on_delete=models.DO_NOTHING)
    kategori = models.ManyToManyField(Kategori)

    slug = models.SlugField(blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(f'{self.titulli}')
        super(Blog, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return f'{self.titulli}'
    
class Comments(models.Model):
    user_name = models.CharField(max_length=120)
    user_email = models.EmailField()
    text = models.TextField(max_length=400)
    post = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')

    def __str__(self) -> str:
        return f'{self.user_name} {self.post}'





