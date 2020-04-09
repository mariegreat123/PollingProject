from django.shortcuts import render
from django.http import JsonResponse, HttpResponse


def test_view(request):
    id_ = request.GET.get('id', None)
    print (id_)
    if id_:
        print ('yes')
    else:
        print('no')
    return JsonResponse(data={'data':'response'}, safe=False)
    # return HttpResponse('hello')