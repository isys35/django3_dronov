from django.shortcuts import render
from django.http import HttpResponse
from .models import Bb, Rubric
from django.template import loader
from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from .forms import BbForm


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


def index(request):
    bbs = Bb.objects.all()
    rubrics = Rubric.objects.all()
    context = {'bbs': bbs, 'rubrics': rubrics}
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



