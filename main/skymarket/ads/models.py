
from django.db import models


class Ad(models.Model):
    title = models.CharField(max_length=150)
    price = models.PositiveIntegerField()
    description = models.TextField()
    author = models.ForeignKey('users.User', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="ad_images/", null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"
        ordering = ['-created_at']


class Comment(models.Model):
    text = models.TextField()
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE)
    author = models.ForeignKey('users.User', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
        ordering = ['-created_at']
