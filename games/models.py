from django.db import models

# Create your models here.
class Game(models.Model):
    title = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    release_date = models.CharField(max_length=50)
    preview_url = models.TextField()
    rating = models.IntegerField()
    owner = models.ForeignKey('users.User', related_name='games', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Review(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    game = models.ForeignKey(
        Game, on_delete=models.CASCADE, related_name='reviews')
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey('users.User', related_name='reviews', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


