from django.db import models
from uuid import uuid4

# Create your models here.
class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=430)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    salt = models.BinaryField(max_length=128, default=bytes(0))

    links = models.IntegerField(default=0)

    def as_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "links": self.links,
        }

    def __str__(self):
        return self.name

class Link(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)

    url = models.URLField()
    short_url = models.CharField(max_length=10)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    clicks = models.IntegerField(default=0)

    nsfw = models.BooleanField(default=False)
    private = models.BooleanField(default=False)

    def as_dict(self):
        return {
            "id": self.id,
            "creator": self.creator.id,
            "url": self.url,
            "short_url": self.short_url,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "clicks": self.clicks,
            "nsfw": self.nsfw,
        }

    def __str__(self):
        return self.short_url