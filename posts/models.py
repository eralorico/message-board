from django.db import models

# Create your models here.
# Models are tables on data base.
# Models are class-based.
"""
    CREATE TABLE POST(
        ID PRIMARY KER INTEGER,
        TEXT VARACHAR (50),
    );
"""

class Post(models.Model):
    text = models.TextField()

    def __str__(self) -> str:
        #index slicing in python
        return self.text[:50]