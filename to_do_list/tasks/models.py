from django.db import models


class Task(models.Model):
    """Модель задачи."""

    PRIORITY_CHOICES = (
        ('low', 'низкий'),
        ('middle', 'средний'),
        ('high', 'высокий')
    )

    STATUS_CHOICES = (
        ('done', 'выполнено'),
        ('not_done', 'не выполнено')
    )

    title = models.CharField('Заголовок', max_length=255)
    description = models.TextField('Описание')
    date_created = models.DateTimeField('Дата создания', auto_now_add=True)
    deadline = models.DateField('Дедлайн')
    priority = models.CharField(
        'Приоритет', choices=PRIORITY_CHOICES,
        default='middle', max_length=10
    )
    status = models.CharField(
        'Статус', choices=STATUS_CHOICES,
        max_length=10, default='not_done'
    )

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
        ordering = ('-priority',)

    def __str__(self):
        return self.title
