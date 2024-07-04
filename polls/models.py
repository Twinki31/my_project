from django.db import models


class Poll(models.Model):
    title = models.CharField('Название', max_length=200)
    start_date = models.DateField('Дата старта')
    end_date = models.DateField('Дата окончания')
    description = models.TextField('Описание')

    class Meta:
        verbose_name = 'Опрос'
        verbose_name_plural = 'Опросы'

    def __str__(self):
        return self.title


class Question(models.Model):
    TEXT = 'text'
    SINGLE_CHOICE = 'single_choice'
    MULTIPLE_CHOICE = 'multiple_choice'

    QUESTION_TYPES = [
        (TEXT, 'Ответ текстом'),
        (SINGLE_CHOICE, 'Выбор одного варианта'),
        (MULTIPLE_CHOICE, 'Выбор нескольких вариантов')
    ]

    poll = models.ForeignKey(
        Poll,
        related_name='questions',
        on_delete=models.CASCADE,
        verbose_name='Опрос',
        )

    text = models.CharField('Текст вопроса', max_length=200)

    question_type = models.CharField(
        'Тип вопроса', max_length=20, choices=QUESTION_TYPES)

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

    def __str__(self):
        return self.text
