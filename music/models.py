from django.db import models

class Album(models.Model):
    artist = models.CharField(max_length=250)
    album_title = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    album_logo = models.CharField(max_length=1000)
    is_favourite = models.BooleanField(default=False)

    def __str__(self):
        return "name: {0} , album_title: {1}".format(self.artist, self.album_title)

class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10)
    song_title = models.CharField(max_length=250)
    is_favourite = models.BooleanField(default=False)

    def __str__(self):
        return "song_title: {0} file_type: {1}".format(self.song_title, self.file_type)
