from django.db import models


class News(models.Model):
    title = models.CharField(max_length=150, verbose_name='Article')
    content = models.TextField(blank=True, verbose_name='Content')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Date')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Update Date')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, verbose_name='Image')
    is_published = models.BooleanField(default=True, verbose_name='Published')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name='Category')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'news'
        verbose_name_plural = 'news'
        ordering = ['-created_at']


class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Category')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['id']
