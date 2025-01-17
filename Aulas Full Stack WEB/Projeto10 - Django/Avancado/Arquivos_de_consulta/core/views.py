from django.views.generic import FormView
from django.urls import reverse_lazy
from django.contrib import messages

from .models import Servico, Funcionario
from .forms import ContatoForm

#Criar contxt para serviços e funcionários

class IndexView(FormView):
    template_name = 'index.html'
    form_class = ContatoForm
    success_url = reverse_lazy('index')  # Após dar certo o envio abrirá a página index

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['servicos'] = Servico.objects.order_by('?').all()  # order_by('?') vai embaralhar apresentação a cada acesso, se tirar ele e deixar apenas .all() ficam todos estáticos.
        context['funcionarios'] = Funcionario.objects.order_by('?').all()
        return context

    def form_valid(self, form, *args, **kwargs):
        form.send_mail()
        messages.success(self.request, 'E-mail enviado com sucesso')
        return super(IndexView, self).form_valid(form, *args, **kwargs)

    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, 'Erro ao enviar e-mail')
        return super(IndexView, self).form_invalid(form, *args, **kwargs)



"""
# Página teste
class TesteViews (TemplateView):
	template_name = 'teste.html'


class Teste404 (TemplateView):
	template_name = '404.html'

class Teste500(TemplateView):
	template_name = '500.html'
"""