from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import TopLiked
import json
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@csrf_exempt
def home(request):
    if request.method == 'POST':
        title = request.POST['title']
        amount = request.POST['amount']

        TopLiked.objects.create(
            title = title,
            amount = amount
        )
    if TopLiked.objects.all().count() < 5:
        data0 = ""
        data1 = ""
        data2 = ""
        data3 = ""
        data4 = ""
    else:
        data0 = TopLiked.objects.all()[0]
        data1 = TopLiked.objects.all()[1]
        data2 = TopLiked.objects.all()[2]
        data3 = TopLiked.objects.all()[3]
        data4 = TopLiked.objects.all()[4]
    show = {'data0': data0, 'data1': data1, 'data2': data2, 'data3': data3, 'data4': data4,}
    return render(request, 'index.html', show)

