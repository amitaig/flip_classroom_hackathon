from django.db import models
import django.contrib.auth

class VideoPage(models.Model):
    youtube_movie_id = models.CharField(max_length=25)
    upload_date      = models.DateTimeField('date uploaded to our site')
    content          = models.TextField()
    video_title      = models.CharField(max_length=50)
    user             = models.ForeignKey(django.contrib.auth.get_user_model())
    def __unicode__(self):
        return self.video_title

class Review(models.Model):
    class Meta:
        abstract=True
    video   = models.ForeignKey(VideoPage)
    user = models.ForeignKey(django.contrib.auth.get_user_model())
    
class RatingReview(Review):
    context_choices = (
        ("rel",      "Relevancy"),
        ("quality",  "Technical quality")
    )
    context = models.CharField(max_length=10)
    rate    = models.PositiveSmallIntegerField()

class TextualReview(Review):
    textual_review  = models.CharField(max_length=500)
