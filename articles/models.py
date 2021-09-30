from django.db import models


class Word(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class Tag(models.Model):
    is_main = models.BooleanField(default=False)
    tag = models.ForeignKey(Word, on_delete=models.CASCADE)

    def __str__(self):
        return self.tag.name

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'




class Article(models.Model):
    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True,
                              blank=True,
                              verbose_name='Изображение'
                              )
    scopes = models.ManyToManyField(Tag, through='Scopeship')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title


class Scopeship(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Тематика статьи'
        verbose_name_plural = 'Тематики Статьи'
