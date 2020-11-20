from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpResponseNotAllowed
from ..models import Service
from datetime import datetime
import os
import simplejson as json
from django.views.decorators.csrf import csrf_exempt

BASE_DIR = '/Users/jangjuhyeon/IdeaProjects/djangoprj/mytest/render'
BASE_IMAGE_DIR = '/static/ServiceImage/'

def home(request):
    return render(request, 'render/home.html')


def detail(request, service_id):
    try:
        service_item = Service.objects.filter(id=service_id).filter(data_status='SUCC')
        if service_item.exists():
            filename = BASE_IMAGE_DIR + '%d' % service_id + '/result.ply'
        else:
            raise Http404("Not Valid Service Number")
    except Service.DoesNotExist:
        raise Http404("Service does not exist")
    return render(request, 'render/detail.html', {'filename': filename})

@csrf_exempt
def makenstart(request):
    if request.method == 'POST':
        try:
            new_service = Service.objects.create(
                date_requested=datetime.now(),
                data_status='QUIT',
                email_address=request.POST['email']
            )
            new_service.save()
            dirname = BASE_DIR + BASE_IMAGE_DIR + '%d' % new_service.id
            os.mkdir(dirname)
            file = request.FILES['zip_file']
            with open(os.path.join(dirname, 'input.zip'), 'wb+') as dest:
                for chunk in file.chunks():
                    dest.write(chunk)

            new_service.data_status = 'WAIT'
            new_service.save()
            context = {'message': 'Uploaded Successfully'}
        except Exception as e:
            context = {'errors': e}
        return HttpResponse(json.dumps(context), content_type="application/json")
    elif request.method == 'GET':
        return render(request, 'render/service.html')
    else:
        return HttpResponseNotAllowed
