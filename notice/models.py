from django.db import models

# Create your models here.
'''
   CREATE TABLE notice(name varchar2(34)....content CLOB,regdate DATE)
   ORM
'''
class Notice(models.Model):
    name=models.CharField(max_length=34)
    subject=models.CharField(max_length=500)
    content=models.TextField()
    regdate=models.DateTimeField()
    def __str__(self):  # toString
        return self.subject
