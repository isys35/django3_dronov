from django.contrib import admin
from django.urls import reverse
from .models import Bb, Rubric

"""
    Листинг 27.2. Пример создания действия в виде функции
"""
from django.db.models import F


def discount(modeladmin, request, queryset):
    f = F('price')
    for rec in queryset:
        rec.price = f / 2
        rec.save()
    modeladmin.message_user(request, 'Действие выполнено')


discount.short_description = 'Уменьшить цену вдвое'

"""
    Пример фильтра
"""


class PriceListFilter(admin.SimpleListFilter):
    title = 'Категория цен'
    parameter_name = 'price'

    def lookups(self, request, model_admin):
        return (
            ('low', 'Низкая цена'),
            ('medium', 'Средняя цена'),
            ('high', 'Высокая цена')
        )

    def queryset(self, request, queryset):
        if self.value() == 'low':
            return queryset.filter(price__lt=500)
        elif self.value() == 'medium':
            return queryset.filter(price__gte=500, price__lte=5000)
        elif self.value() == 'high':
            return queryset.filter(price__gt=5000)


class BbAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'price', 'published', 'rubric')
    list_editable = ('price',)
    list_display_links = ('title', 'content')
    search_fields = ('title', 'content',)
    list_filter = (PriceListFilter,)
    empty_value_display = '---'
    # fields = (('title', 'price'), 'content', 'published')
    # readonly_fields = ('published', )
    fieldsets = (
        (None, {
            'fields': (('title', 'rubric'), 'content'),
            'classes': ('wide',),
        }),
        ('Дополнительные сведения', {
            'fields': ('price',),
            'description': 'Параметры, необязвательные для указания',
        }
         )
    )
    actions = (discount,)

    # def get_fields(self, request, obj=None):
    #     f = ['title', 'content', 'price']
    #     if not obj:
    #         f.append('rubric')
    #     return f

    # def get_form(self, request, obj=None, change=False, **kwargs):
    #     if obj:
    #         return BbModelForm
    #     else:
    #         return BbAddModelForm

    def view_on_site(self, rec):
        return reverse('bboard:detail', kwargs={'pk': rec.pk})


"""
    Листинг 27.1 Пример использования встроенного редактора
"""

from django.contrib import admin
from .models import Bb, Rubric


class BbInline(admin.StackedInline):
    model = Bb


class RubricAdmin(admin.ModelAdmin):
    inlines = [BbInline]


admin.site.register(Bb, BbAdmin)
admin.site.register(Rubric, RubricAdmin)
