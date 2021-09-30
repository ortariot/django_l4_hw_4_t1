from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Scopeship, Tag


class ScopeshipInlineFormset(BaseInlineFormSet):
    def clean(self):
        for form in self.forms:
            # В form.cleaned_data будет словарь с данными
            # каждой отдельной формы, которые вы можете проверить
            print('__1__')
            print(form)
            form.cleaned_data
            # вызовом исключения ValidationError можно указать админке о наличие ошибки
            # таким образом объект не будет сохранен,
            # а пользователю выведется соответствующее сообщение об ошибке
            raise ValidationError('Тут всегда ошибка')
        return super().clean()  # вызываем базовый код переопределяемого метода


class ScopeshipInline(admin.TabularInline):
    model = Scopeship
    formset = ScopeshipInlineFormset

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopeshipInline]

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass