from django.views.generic import TemplateView

class PaginaInicial(TemplateView):
    template_name = 'modelo.html'
    
class CatalogoTarefas(TemplateView):
    template_name = 'catalogo.html'