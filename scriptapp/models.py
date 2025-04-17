from django.db import models



# Create your models here.


class Chapter(models.Model):
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class ScriptEntry(models.Model):
    chapter = models.ForeignKey(Chapter, related_name='entries', on_delete=models.CASCADE)  # ✅ foreign key
    place = models.CharField(max_length=100)
    emotion = models.CharField(max_length=100)
    voice = models.CharField(max_length=100)
    context = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.voice} - {self.place} ({self.emotion})"
