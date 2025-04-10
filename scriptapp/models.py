from django.db import models

# Create your models here.

class ScriptEntry(models.Model):
    place = models.CharField(max_length=100)
    emotion = models.CharField(max_length=100)
    voice = models.CharField(max_length=100)
    context = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.voice} - {self.place} ({self.emotion})"    
    
class Chapter(models.Model):
    title = models.CharField(max_length=100)
    entries = models.ManyToManyField(ScriptEntry)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title