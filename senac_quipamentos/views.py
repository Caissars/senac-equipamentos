from django.shortcuts import render
def Homepage(request):
        return render(request, 'home.html', {})
def proof(request):
        return render(request, 'equipments.html', {})
