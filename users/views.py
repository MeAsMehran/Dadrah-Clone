from django.shortcuts import render


# Create your views here.

class NormalUserFunctions:

    def welcome(self, request):
        return render(request, 'welcome.html')









