from django.utils import timezone
from rest_framework import serializers

from tasks.models import Task

INVALID_DATE = 'Дата не может быть раньше сегодняшнего дня'


class TaskSerializer(serializers.ModelSerializer):
    """Сериализатор для задач."""

    deadline = serializers.DateField(
        input_formats=('%d.%m.%Y',),
        format='%d.%m.%Y',
    )
    date_created = serializers.DateTimeField(
        format='%d.%m.%Y %H:%M',
        read_only=True,
    )

    class Meta:
        model = Task
        fields = '__all__'

    def validate_deadline(self, deadline):
        """Проверка даты дедлайна."""
        if deadline < timezone.now().date():
            raise serializers.ValidationError(INVALID_DATE)
        return deadline
