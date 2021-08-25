from tortoise import fields, models

class Author(models.Model):
    """
    Model for Authors
    """
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=1024)
