from django.db import models

# Create your models here.

class Renren(models.Model):
    # m_review: 影评 m_recom: 片单推荐
    type = models.CharField(null=False,max_length=20)
    media_id = models.CharField(null=False,max_length=100)
    class Meta:
        db_table = 'renren'