from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'ninja2_app/index.html')

def ninja(request):
    return render(request, 'ninja2_app/ninja.html')


def ninjas(request, word):
    context = {
        'word': word
        }
    return render(request, 'ninja2_app/ninjas.html', context)
