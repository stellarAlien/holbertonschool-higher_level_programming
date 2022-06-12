from email.policy import default
from msilib.schema import Class
from pyexpat import model
from django.db import models
from django_countries.fields import CountryField

# Create your models here.


class Article(models.Model):
    
    title = models.CharField(max_length=500)
    description = models.TextField()
    link  = models.URLField()
    image = models.URLField()
    top_image = models.URLField()
    guid = models.CharField(max_length=50)
    pub_date = models.DateTimeField()

    def __str__(self):
        return "{}: {}.format(self.title, self.link.parse('.')[1])"

    def __unicode__(self):
        return u'%s'(self.title)
    
class User(models.Model):   
    email = models.oneToMa('email_address', max_length=255, unique=True)
    first_name = models.CharField('first name', max_length=30, blank=True)
    last_name = models.CharField('last name', max_length=30, blank=True)
    country = CountryField(default='Tunisia')

    def __str__(self):
        return "{self.email}"

    def __unicode__(self):
        return 
    
Class Interests(models.Model):
        """_summary_
        every user has many interests
        Args:
            self (_type_): _description_
        """
        user_email = models.EmailField(name = models.ForeignKey('User', related_name='email', on_delete=models.CASCADE))
        #interests = models.JSONField()
        interests = models.#use deferrabel field here ? https://pandafy.me/deferred-fields-in-django
        
