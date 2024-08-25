from django.shortcuts import render, redirect

def Homepage(request):
    if request.method == 'POST':
        return render(request, 'equipments.html')  # Assuming 'home.html' is a template name
    return render(request,'home.html')