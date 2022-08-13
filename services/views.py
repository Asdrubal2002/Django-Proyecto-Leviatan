from django.shortcuts import render
from django.views import View

from services.models import Empresa
# Create your views here.


class ServicesView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'services/services.html')






class chooseView(View):
    def get(self, request, *args, **kwargs):
        #empresa = Empresa.objects.get(user=self.request.user)
        company = Empresa.objects.filter(user=self.request.user)
       
        company_validation = len(company)
        
        if company_validation == 0:
            return render(request, 'services/createCompany.html')
        else:
           return render(request, 'services/my-company.html')
        
        



   
        



