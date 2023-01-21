from django.db import models

class Localities(models.Model):
    title = models.CharField('Населенный пункт', max_length=255, default="")
    leader = models.CharField('Глава', max_length=255, default="")
    number_of_inhabitants = models.IntegerField('Население', default=0)
    budget = models.IntegerField('Бюджет', default=0)
    spending = models.IntegerField('Расходы', default=0)
    deficit = models.IntegerField('Дефицит', default=0)
    img_link = models.TextField('Ссылка на картинку', default="https://www.emetechnologies.com/blog/cse/images/python-web-framework-django.jpg")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/project/{self.id}'

    class Meta:
        verbose_name = 'Населенный пункт'
        verbose_name_plural = 'Населенные пункты'