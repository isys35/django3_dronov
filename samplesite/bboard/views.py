from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic.edit import CreateView
from django.http.response import HttpResponseRedirect

from .forms import BbForm
from .models import Bb, Rubric

# def index(request):
#     s = "Список объявлений\r\n\r\n\r\n"
#     for bb in Bb.objects.order_by('-published'):
#         s += bb.title + '\r\n' + bb.content + '\r\n\r\n'
#     return HttpResponse(s, content_type='text/plain; charset=utf-8')


# def index(request):
#     template = loader.get_template('bboard/index.html')
#     bbs = Bb.objects.order_by('-published')
#     context = {'bbs': bbs}
#     return HttpResponse(template.render(context, request))

"""
    Пример использования пагинатора
    Листинг 12.1
"""
from django.core.paginator import Paginator


def index(request):
    bbs = Bb.objects.all()
    rubrics = Rubric.objects.all()
    paginator = Paginator(bbs, 2)
    if 'page' in request.GET:
        page_num = request.GET['page']
    else:
        page_num = 1
    page = paginator.get_page(page_num)
    context = {'bbs': page.object_list, 'page': page, 'rubrics': rubrics}
    return render(request, 'bboard/index.html', context)


def by_rubric(request, rubric_id):
    bbs = Bb.objects.filter(rubric=rubric_id)
    rubrics = Rubric.objects.all()
    current_rubric = Rubric.objects.get(pk=rubric_id)
    context = {'bbs': bbs, 'rubrics': rubrics, 'current_rubric': current_rubric}
    return render(request, 'bboard/by_rubric.html', context)


# class BbCreateView(CreateView):
#     template_name = 'bboard/create.html'
#     form_class = BbForm
#     success_url = reverse_lazy('bboard:index')
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['rubrics'] = Rubric.objects.all()
#         return context


"""
    Контроллер-функция add()
    Листинг 9.1
"""

# def add(request):
#     bbf = BbForm()
#     context = {'form': bbf}
#     return render(request, 'bboard/create.html', context)


"""
    Контроллер-функции add_save()
    Листинг 9.2
"""

# from django.http import HttpResponseRedirect
# from django.urls import reverse
#
#
# def add_save(request):
#     bbf = BbForm(request.POST)
#     if bbf.is_valid():
#         bbf.save()
#         return HttpResponseRedirect(reverse('by_rubric',
#                                             kwargs={'rubric_id': bbf.cleaned_data['rubric'].pk}))
#     else:
#         context = {'form': bbf}
#         return render(request, 'bboard/create.html', context)

"""
    Контроллер-функции add_and_save()
    Листинг 9.3
"""
# from django.http import HttpResponseRedirect
# from django.urls import reverse
#
#
# def add_and_save(request):
#     if request.method == 'POST':
#         bbf = BbForm(request.POST)
#         if bbf.is_valid():
#             bbf.save()
#             return HttpResponseRedirect(reverse('by_rubric',
#                                                 kwargs={'rubric_id': bbf.cleaned_data['rubric'].pk}))
#     else:
#         bbf = BbForm()
#         context = {'form': bbf}
#         return render(request, 'bboard/create.html', context)


"""
    Использование низкоуровневых средств формирования ответа
    Листинг 9.4
"""

# def index(request):
#     resp = HttpResponse("Здесь будет",
#                         content_type='text/plain; charset=utf-8')
#     resp.write(' главная')
#     resp.writelines((' страница', ' сайта'))
#     resp['keywords'] = 'Python, Django'
#     return resp

"""
    Применение метода render() для рендеринга шаблона
    Листинг 9.5
"""

# def index(request):
#     bbs = Bb.objects.all()
#     rubrics = Rubric.objects.all()
#     context = {'bbs': bbs, 'rubrics': rubrics}
#     template = loader.get_template('bboard/index.html')
#     return HttpResponse(template.render(context=context, request=request))


"""
    Применение функции render_to_string() для рендеринга шаблона
    Листинг 9.6
"""

# def index(request):
#     bbs = Bb.objects.all()
#     rubrics = Rubric.objects.all()
#     context = {'bbs': bbs, 'rubrics': rubrics}
#     return HttpResponse(loader.render_to_string('bboard/index.html',
#                                                 context,
#                                                 request))


"""
    Использование класса TemplateResponse
    Листинг 9.7
"""

# from django.template.response import TemplateResponse
#
#
# def index(request):
#     bbs = Bb.objects.all()
#     rubrics = Rubric.objects.all()
#     context = {'bbs': bbs, 'rubrics': rubrics}
#     return TemplateResponse(request, 'bboard/index.html',
#                             context=context)

"""
    Отправка потокового ответа
    Листинг 9.8
"""

# from django.http import StreamingHttpResponse
#
#
# def index(request):
#     resp_content = ('Здесь будет', ' главная', ' страница', ' сайта')
#     resp = StreamingHttpResponse(resp_content, content_type='text/plain; charset=utf-8')
#     return resp


"""
    Использование котнтроллера класса TemplateView
    Листинг 10.1
"""

# from django.views.generic.base import TemplateView
#
#
# class BbByRubric(TemplateView):
#     template_name = 'bboard/by_rubric.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['bbs'] = Bb.objects.filter(rubric=context['rubric_id'])
#         context['rubrics'] = Rubric.objects.all()
#         context['current_rubric'] = Rubric.objects.get(pk=context['rubric_id'])
#         return context


"""
    Использование котнтроллера класса DetailView
    Листинг 10.2
"""

from django.views.generic.detail import DetailView


class BbDetailView(DetailView):
    model = Bb

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context


"""
    Использование котнтроллера класса ListView
    Листинг 10.4
"""

from django.views.generic.list import ListView


class BbByRubricView(ListView):
    template_name = 'bboard/by_rubric.html'
    context_object_name = 'bbs'

    def get_queryset(self):
        return Bb.objects.filter(rubric=self.kwargs['rubric_id'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.all()
        context['current_rubric'] = Rubric.objects.get(pk=self.kwargs['rubric_id'])
        return context


"""
    Использование котнтроллера класса FormView
    Листинг 10.5
"""

from django.views.generic.edit import FormView


class BbAddView(FormView):
    template_name = 'bboard/create.html'
    form_class = BbForm
    initial = {'price': 0.0}

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_form(self, form_class=None):
        self.object = super().get_form(form_class)
        return self.object

    def get_success_url(self):
        return reverse('bboard:by_rubric',
                       kwargs={'rubric_id': self.object.cleaned_data['rubric'].pk})


"""
    Использование котнтроллера класса UpdateView
    Листинг 10.6
"""

from django.views.generic.edit import UpdateView


class BbEditView(UpdateView):
    model = Bb
    form_class = BbForm

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context

    def get_success_url(self):
        return reverse_lazy('bboard:detail',
                            kwargs={'pk': self.object.pk})


"""
    Использование котнтроллера класса DeleteView
    Листинг 10.7
"""

from django.views.generic.edit import DeleteView


class BbDeleteView(DeleteView):
    model = Bb
    success_url = '/'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context


"""
    Применение котнтроллера класса ArchiveIndexView
    Листинг 10.9
"""
# from django.views.generic.dates import ArchiveIndexView
#
#
# class BbIndexView(ArchiveIndexView):
#     model = Bb
#     date_field = 'published'
#     date_list_period = 'year'
#     template_name = 'bboard/index.html'
#     context_object_name = 'bbs'
#     allow_empty = True
#
#     def get_context_data(self, *args, **kwargs):
#         context = super().get_context_data(*args, **kwargs)
#         context['rubrics'] = Rubric.objects.all()
#         return context


"""
    Использование контроллера класса DateDetailView
    Листинг 10.10
"""
# from django.views.generic.dates import DateDetailView
#
#
# class BbDetailView(DateDetailView):
#     model = Bb
#     date_field = 'published'
#     montf_format = '%m'
#
#     def get_context_data(self, *args, **kwargs):
#         context = super().get_context_data(*args, **kwargs)
#         context['rubrics'] = Rubric.objects.all()
#         return context

"""
    Использование контроллера класса RedirectView
    Листинг 10.11
"""
from django.views.generic.base import RedirectView


class BbRedirectView(RedirectView):
    url = '/detail/%(pk)d/'


"""
    Использование контроллера-класса смешанной функциональности
    Листинг 10.12
"""

# from django.views.generic.detail import SingleObjectMixin
#
#
# class BbByRubricView(SingleObjectMixin, ListView):
#     template_name = 'bboard/by_rubric.html'
#     pk_url_kwarg = 'rubric_id'
#
#     def get(self, request, *args, **kwargs):
#         self.object = self.get_object(queryset=Rubric.objects.all())
#         return super().get(request, *args, **kwargs)
#
#     def get_queryset(self):
#         return self.object.bb_set.all()
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['rubrics'] = Rubric.objects.all()
#         context['current_rubric'] = self.object
#         context['bbs'] = context['object_list']
#         return context


"""
    Контроллер-функция, исправляющий запись
    Листинг 13.6
"""

from django.contrib import messages


def edit(request, pk):
    bb = Bb.objects.get(pk=pk)
    if request.method == 'POST':
        bbf = BbForm(request.POST, instance=bb)
        if bbf.is_valid():
            bbf.save()
            messages.add_message(request, messages.SUCCESS, 'Объявление исправлено')
            return HttpResponseRedirect(reverse('bboard:index'))
        else:
            context = {'form': bbf}
            return render(request, 'bboard/bb_form.html', context)
    else:
        bbf = BbForm(instance=bb)
        context = {'form': bbf}
        return render(request, 'bboard/bb_form.html', context)


"""
    Обработка набора форм, связанного с моделью
    Листинг 14.1
"""

# from django.shortcuts import render, redirect
# from django.forms import modelformset_factory
# from .models import Rubric
#
#
# def rubrics(request):
#     RubricFormSet = modelformset_factory(Rubric, fields=('name',), can_delete=True)
#     if request.method == 'POST':
#         formset = RubricFormSet(request.POST)
#         if formset.is_valid():
#             formset.save()
#             return redirect('bboard:index')
#     else:
#         formset = RubricFormSet()
#     context = {'formset': formset}
#     return render(request, 'bboard/rubrics.html', context)


"""
    Обработка набора форм, озволяющего переупорядочить записи
    Листинг 14.2
"""

from django.shortcuts import render, redirect
from django.forms import modelformset_factory
from django.forms.formsets import ORDERING_FIELD_NAME
from .models import Rubric


def rubrics(request):
    RubricFormSet = modelformset_factory(Rubric, fields=('name',), can_order=True, can_delete=True)
    if request.method == 'POST':
        formset = RubricFormSet(request.POST)
        if formset.is_valid():
            for form in formset:
                if form.cleaned_data:
                    rubric = form.save(commit=False)
                    rubric.order = form.cleaned_data[ORDERING_FIELD_NAME]
                    rubric.save()
            return redirect('bboard:index')
    else:
        formset = RubricFormSet()
    context = {'formset': formset}
    return render(request, 'bboard/rubrics.html', context)


"""
    Применение встроенного набора форм
    Листинг 14.4
"""

from django.shortcuts import render, redirect
from django.forms import inlineformset_factory

from .models import Bb, Rubric
from .forms import BbForm


def bbs(request, rubric_id):
    BbsFormSet = inlineformset_factory(Rubric, Bb, form=BbForm, extra=1)
    rubric = Rubric.objects.get(pk=rubric_id)
    if request.method == 'POST':
        formset = BbsFormSet(request.POST, instance=rubric)
        if formset.is_valid():
            formset.save()
            return redirect('bboard:index')
    else:
        formset = BbsFormSet(instance=rubric)
    context = {'formset': formset, 'current_rubric': rubric}
    return render(request, 'bboard/bbs.html', context)


"""
    Контроллер, который использует форму, не связанную  с моделью
    Листинг 17.2
"""

from .forms import SearchForm
from django.http import HttpRequest


def search(request: HttpRequest):
    if request.method == 'POST':
        sf = SearchForm(request.POST)
        if sf.is_valid():
            keyword = sf.cleaned_data['keyword']
            rubric_id = sf.cleaned_data['rubric'].pk
            bbs = Bb.objects.filter(title__icontains=keyword, rubric=rubric_id)
            context = {'bbs': bbs}
            return render(request, 'bboard/search_results.html', context)
    else:
        sf = SearchForm()
    context = {'form': sf}
    return render(request, 'bboard/search.html', context)


"""
    Контроллер, который обрабатывает набор форм, не связанный с моделью
    Листинг 17.3
"""
from django.forms import formset_factory


def formset_processing(request: HttpRequest):
    FS = formset_factory(SearchForm, extra=3, can_order=True, can_delete=True)
    if request.method == 'POST':
        formset = FS(request.POST)
        if formset.is_valid():
            for form in formset:
                if form.changed_data and not form.changed_data['DELETE']:
                    keyword = form.cleaned_data['keyword']
                    rubric_id = form.cleaned_data['rubric'].pk
                    order = form.cleaned_data['ORDER']
                    # Выполняем какие-либо действия над полученными
                    # данными
            return render(request, 'bboard/process_result.html')

    else:
        formset = FS()
    context = {'formset': formset}
    return render(request, 'bboard/formset.html', context)


"""
    Листинг 23.1. Использование примеси SuccessMessageMixin
"""

from django.views.generic.edit import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from .models import Bb
from .forms import BbForm


class BbCreateView(SuccessMessageMixin, CreateView):
    template_name = 'bboard/create.html'
    form_class = BbForm
    success_url = '/{rubric_id}'
    success_message = 'Объявление о продаже товара создано'


"""
    Отправка электронных писем
"""

# from django.core.mail import EmailMessage
#
# em = EmailMessage(subject='Test', body='Test', to=['isysbas@gmail.com'])
# em = EmailMessage(subject='Ваш новый пароль', body='Ваш новый пароль во вложении',
#                   attachments=[('password.txt', '123456789', 'text/plain')],
#                   to=['isysbas@gmail.com'])
# em = EmailMessage(subject='Запрошенный вами файл', body='Получите запрошенный вами файл',
# # #                   to=['isysbas@gmail.com'])
# # # em.attach_file(r'C:\work\file.txt')
# # # em.send()s


""" 
    Формирование писем на основе шаблонов
"""

# from django.core.mail import EmailMessage
# from django.template.loader import render_to_string
# context = {'user': 'Вася Пупкин'}
# s = render_to_string('email/letter.txt', context)
# em = EmailMessage(subject='Оповещение', body=s, to=['isysbas@gamil.com'])
# em.send()

""" 
    Пример отправки письма, которое помимо текстовой части, содержит и фрагмент
    написанный на HTML
"""

# from django.core.mail import EmailMultiAlternatives
# em = EmailMultiAlternatives(subject='Test', body='Test', to=['isysbas@gamil.com'])
# em.attach_alternative('<h1>Test</h1>', 'text/html')
# em.send()

"""
    Массовая отправка писем
"""

# from django.core.mail import send_mass_mail
# msg1 = ('Подписка', 'Подтвердите, пожалуйста, подписку', 'subscribe@supersite.ru', ['user@othersite.ru', 'user2@thirdsite.ru'])
# msg2 = ('Подписка', 'Ваша подписка подтвержена', 'subscribe@supersite.ru', ['megauser@megasite.ru'])
# send_mass_mail((msg1, msg2))

"""
    Листинг 28.2. Контроллер, использующий сериализатор для вывода рубрик
"""

from django.http import JsonResponse
from .models import Rubric
from .serializers import RubricSerializer

# def api_rubrics(request):
#     if request.method == 'GET':
#         rubrics = Rubric.objects.all()
#         serializer = RubricSerializer(rubrics, many=True)
#         return JsonResponse(serializer.data, safe=False)


"""
    Листинг 28.3. Пример контроллера, реализующего веб-представление
"""

from rest_framework.response import Response
from rest_framework.decorators import api_view

# @api_view(['GET'])
# def api_rubrics(requst):
#     if requst.method == 'GET':
#         rubrics = Rubric.objects.all()
#         serializer = RubricSerializer(rubrics, many=True)
#         return Response(serializer.data)


"""
    Листинг 28.4. Контроллер, выдающий сведения об отдельной рубрике
"""

# @api_view(['GET'])
# def api_rubric_detail(requst, pk):
#     if requst.method == 'GET':
#         rubric = Rubric.objects.get(pk=pk)
#         serializer = RubricSerializer(rubric)
#         return Response(serializer.data)


"""
    Листинг 28.7. Контроллеры api_rubrics() и api_rubric_detail(), 
    поддерживающие добавление, правку м удаление рубрик
"""

from rest_framework import status

# @api_view(['GET', 'POST'])
# def api_rubrics(request):
#     if request.method == 'GET':
#         rubrics = Rubric.objects.all()
#         serializer = RubricSerializer(rubrics, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = RubricSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
# def api_rubric_detail(requst, pk):
#     rubric = Rubric.objects.get(pk=pk)
#     if requst.method == 'GET':
#         serializer = RubricSerializer(rubric)
#         return Response(serializer.data)
#     elif requst.method == 'PUT' or requst.method == 'PATCH':
#         serializer = RubricSerializer(rubric, data=requst.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     elif requst.method == 'DELETE':
#         rubric.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


"""
    Листинг 28.8. Пример использования APIView
"""

# from rest_framework.views import APIView
#
#
# class APIRubrics(APIView):
#     def get(self, request):
#         rubrics = Rubric.objects.all()
#         serializer = RubricSerializer(rubrics, many=True)
#         return Response(serializer.data)
#
#     def post(self, request):
#         serializer = RubricSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# class APIRubricsDetail(APIView):
#     def get(self, request, pk):
#         rubric = Rubric.objects.get(pk=pk)
#         serializer = RubricSerializer(rubric)
#         return Response(serializer.data)
#
#     def put(self, request, pk):
#         rubric = Rubric.objects.get(pk=pk)
#         serializer = RubricSerializer(rubric, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk):
#         rubric = Rubric.objects.get(pk=pk)
#         rubric.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#


"""
    Листинг 28.9. Пример использования классов ListCreateAPIView и RetrieveUpdateDestroyAPIView
"""

from rest_framework import generics


class APIRubrics(generics.ListCreateAPIView):
    queryset = Rubric.objects.all()
    serializer_class = RubricSerializer


class APIRubricsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rubric.objects.all()
    serializer_class = RubricSerializer


"""
    Листинг 28.10. Метаконтроллер APIRubricViewSet, работающий со списком рубрик
"""

# from rest_framework.viewsets import ModelViewSet
#
#
# class APIRubricViewSet(ModelViewSet):
#     queryset = Rubric.objects.all()
#     serializer_class = RubricSerializer


"""
    Листинг 28.11. Метаконтроллер, реализующий только выдачу рубрик
"""

from rest_framework.viewsets import ReadOnlyModelViewSet

class APIRubricViewSet(ReadOnlyModelViewSet):
    queryset = Rubric.objects.all()
    serializer_class = RubricSerializer