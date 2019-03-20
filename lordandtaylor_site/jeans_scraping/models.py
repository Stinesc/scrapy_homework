from django.db import models


class Garment(models.Model):
    title = models.CharField(max_length=32, blank=True, default="")
    image_url = models.URLField()
    price = models.FloatField()
    color = models.CharField(max_length=32, blank=True, default="")
    description = models.CharField(max_length=256, blank=True, default="")

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']


class Size(models.Model):
    size_content = models.CharField(max_length=32, blank=True, default="")
    garment = models.ForeignKey(Garment, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.size_content
