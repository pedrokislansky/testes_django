from django.shortcuts import render, HttpResponse

# Create your views here.
def hello(request):
    return HttpResponse('<h1>Oi mundo!</h1>')

def soma(request,num1,num2):
    resultado = num1+num2
    return HttpResponse('<h1>A soma de {} + {} = {}</h1>'.format(num1,num2,resultado))