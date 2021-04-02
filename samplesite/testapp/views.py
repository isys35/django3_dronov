from django.shortcuts import render, redirect


def index(request):
    imgs = Img.objects.all()
    context = {'imgs': imgs}
    return render(request, 'testapp/index.html', context)


"""
Листинг 20.3 Контроллер, сохраняющий выгруженный файл
"""

from django.shortcuts import render, redirect

from .models import Img
from .forms import ImgForm


def add(request):
    if request.method == 'POST':
        form = ImgForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('testapp:index')
    else:
        form = ImgForm()
    context = {'form': form}
    return render(request, 'testapp/add.html', context)


"""
Листинг 20.4 Контроллер, удаляющий выгруженный файл вместе с записью модели,
 в которой он хранится
"""


def delete(request, pk):
    img = Img.objects.get(pk=pk)
    img.img.delete()
    return redirect('testapp:index')


"""
Листинг 20.5 Контроллер, сохраняющий выгруженный файл
низкоуровневыми средствами Django
"""
# from samplesite.settings import BASE_DIR
# from datetime import datetime
# import os
#
# from .forms import ImgForm
#
# FILES_ROOT = os.path.join(BASE_DIR, 'files')
#
#
# def add(request):
#     if request.method == 'POST':
#         form = ImgForm(request.POST, request.FILES)
#         print(request.FILES)
#         if form.is_valid():
#             uploaded_file = request.FILES['img']
#             fn = '%s%s' % (datetime.now().timestamp(),
#                            os.path.splitext(uploaded_file.name)[1])
#             fn = os.path.join(FILES_ROOT, fn)
#             with open(fn, 'wb+') as destination:
#                 for chunk in uploaded_file.chunks():
#                     destination.write(chunk)
#             return redirect('testapp:index')
#     else:
#         form = ImgForm()
#     context = {'form': form}
#     return render(request, 'testapp/add.html', context)


"""
Листинг 20.6 Контроллер,выводящий список выгруженных файлов
"""

# from samplesite.settings import BASE_DIR, MEDIA_ROOT
# import os
#
# FILES_ROOT = os.path.join(BASE_DIR, MEDIA_ROOT)
#
#
# def index(request):
#     imgs = []
#     for entry in os.scandir(FILES_ROOT):
#         imgs.append(os.path.basename(entry))
#     context = {'imgs': imgs}
#     return render(request, 'testapp/index.html', context)


"""
Листинг 20.7 Контроллер, отправляющий выгруженный файл клиенту
"""
from django.http import FileResponse
import os

FILES_ROOT = os.path.join(BASE_DIR, MEDIA_ROOT)


def get(request, filename):
    fn = os.path.join(FILES_ROOT, filename)
    return FileResponse(open(fn, 'rb'), content_type='application/octet-stream')


"""
Листинг 21.1 Пример валидатора паролей
"""

from django.core.exceptions import ValidationError


class NoForbiddenCharsValidator:
    def __init__(self, forbidden_chars=(' ',)):
        self.forbidden_chars = forbidden_chars

    def validate(self, password, user=None):
        for fc in self.forbidden_chars:
            if fc in password:
                raise ValidationError(
                    'Пароль не должен содержать недопустимые символы %s' % ', '.join(self.forbidden_chars),
                    code='forbidden_chars_present')

    def get_help_text(self):
        return 'Пароль не должен содержать недопустимые символы %s' % ', '.join(self.forbidden_chars)
