from django.db import models

# Create your models here.
class BaseSettings(models.Model):
    title = models.CharField(
        max_length = 255,
        verbose_name="Заголовок сайта"
    )
    logo = models.ImageField(
        upload_to = "logo/",
        verbose_name = 'Логотип сайта'
    )
    facebook = models.URLField(
        verbose_name='Ссылка на Facebook'
    )
    twitter = models.URLField(
        verbose_name='Ссылка на twitter'
    )
    github = models.URLField(
        verbose_name='Ссылка на Github'
    )
    google = models.URLField(
        verbose_name='Ссылка на Google+'
    )
    

    def __str__(self)->str:
        return self.title

    class Meta:
        verbose_name = 'Основная настройка сайта'
        verbose_name_plural = 'Основные настройки сайта '

    