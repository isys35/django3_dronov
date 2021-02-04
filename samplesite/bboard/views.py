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


class BbCreateView(CreateView):
    template_name = 'bboard/create.html'
    form_class = BbForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context


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
        return reverse('bboard: by_rubric',
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
        return reverse_lazy('detail',
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

# def edit(request, pk):
#     bb = Bb.objects.get(pk=pk)
#     if request.method == 'POST':
#         bbf = BbForm(request.POST, instance=bb)
#         if bbf.is_valid():
#             bbf.save()
#             return HttpResponseRedirect(reverse('bboard:by_rubric'),
#                                         kwargs={'rubric_id':bbf.cleaned_data['rubric'].pk})
#         else:
#             context = {'form': bbf}
#             return render(request, 'bboard/bb_form.html', context)
#     else:
#         bbf = BbForm(instance=bb)
#         context = {'form': bbf}
#         return render(request, 'bboard/bb_form.html', context)

