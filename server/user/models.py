from django.db import models


class User(models.Model):
    first_name = models.CharField()
    last_name = models.CharField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["first_name", "last_name"], name="unique_user"
            )
        ]
        ordering = ["-created_at"]
