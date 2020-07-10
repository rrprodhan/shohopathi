from django.views.generic import TemplateView

class TestPage(TemplateView):
    template_name = 'test.html'    #shows this page after logging in

class ThanksPage(TemplateView):
    template_name = 'thanks.html'  #shows this page after logging out

class HomePage(TemplateView):
    template_name = 'index.html'   #Contains only home page content
