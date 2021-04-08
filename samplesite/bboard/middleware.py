# def my_middleware(next):
#     # Здесь можно выполнить какую-либо инициализацию
#
#     def core_middleware(request):
#         # Здесь выпоняется обработка клиентского  запроса
#         response = next(request)
#         # Здесь выполняется обработка ответа
#         return response
#
#     return core_middleware


"""

    Листинг 22.1. Посредник, добавляющий в контекст шаблона дополнительные данные

"""

from .models import Rubric


class RubricsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)

    def process_template_response(self, request, response):
        response.context_data['rubrics'] = Rubric.objects.all()
        return response


"""
    Листинг 22.2. Пример обработчика контекста
"""


def rubrics(requests):
    return {'rubrics': Rubric.objects.all()}
