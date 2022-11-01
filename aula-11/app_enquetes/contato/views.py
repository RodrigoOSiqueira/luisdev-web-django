from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms.contato import FormContato
from .models import Contato


class ViewContato(CreateView):
    model = Contato
    form_class = FormContato
    template_name = "contato/enviar_contato.html"
    success_url = reverse_lazy("home:home")

    def form_invalid(self, form):
        return super().form_invalid(form)

    def form_valid(self, form):
        contato = form.save(commit=False)
        contato.user = self.request.user
        messages.success(self.request, 'Mensagem enviada com sucesso!')

        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'contexto_novo': 'contexto_novo'})

        return context
