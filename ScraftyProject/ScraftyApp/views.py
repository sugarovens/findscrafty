from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse

def find_scrafty(request):
    input_text = request.GET.get('input_text', '')
    response_data = {'message': f'Hlo World, {input_text}!'}
    return JsonResponse(response_data)
