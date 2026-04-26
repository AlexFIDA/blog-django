from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField("Заголовок", max_length=100)
    content = models.TextField()
    author = models.CharField("Автор", max_length=50)
    date_create = models.DateTimeField("Дата создания", auto_now_add=True)
    
    def __str__(self):
        formatted_date = self.date_create.strftime("%Y-%m-%d %H:%M")
        return f'{self.title} by {self.author}, created at {formatted_date}'
    
    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
        

