from tortoise import fields, models


class Publication(models.Model):
    """Model for Publications"""
    id = fields.IntField(pk=True)
    title = fields.CharField(max_length=1024)
    publish_year = fields.IntField()
    authors = fields.ManyToManyField(model_name='models.Author')
