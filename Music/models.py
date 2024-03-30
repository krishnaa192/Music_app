from django.db import models
from django.contrib.auth.models import User
import os
from django.core.exceptions import ValidationError
# Create your models here.





def validate_mp3(value):

    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.mp3']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Only MP3 files are allowed.')
    
class Music(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    album = models.CharField(max_length=100)
    album_art = models.ImageField(upload_to='album_art/', default='album_art/default.jpg')
    file= models.FileField(upload_to='music/', validators=[validate_mp3])


    def __str__(self):
        return self.title
    
class Folder(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    music = models.ManyToManyField(Music,blank=True)

    class Meta:
        # Define a unique constraint for name and user together
        constraints = [
            models.UniqueConstraint(fields=['name', 'user'], name='unique_folder_per_user')
        ]

    def __str__(self):
        return self.name


class Add_to_playlist(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    music = models.ManyToManyField(Music,blank=True)
    folder=models.ForeignKey(Folder,on_delete=models.CASCADE)



   
    def __str__(self):
        return self.music.title+ " - " + self.folder.name
    
