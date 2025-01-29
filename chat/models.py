"""Models."""

from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Message(models.Model):
    """Model."""

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Show string preview."""
        return f"{self.user.username}: {self.content[:30]}..."
