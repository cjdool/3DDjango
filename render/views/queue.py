from mytest.render.models import Service
from datetime import datetime
from django.core.mail import EmailMessage
import os, subprocess


def send_email(service_id, sendflag):
    try:
        service_item = Service.objects.get(pk=service_id)
        if sendflag == 0:
            email_subject = 'Your Reconstruct Service is started'
            email_message = 'Your Reconstruct Service is started\n This message is sented by Server'
        elif sendflag == 1:
            email_subject = 'Your Reconstruct Service is success'
            email_message = 'Your Reconstruct Service is success\n You can Check your image at 127.0.0.1:8000/render/'\
                            + '%d\n' % service_id + 'This message is sented by Server'
        else:
            email_subject = 'Your Reconstruct Service is failed'
            email_message = 'Your Reconstruct Service is failed\n This message is sented by Server'
        email_list = [service_item.emailaddress]
        emailobj = EmailMessage(subject=email_subject, body=email_message, to=email_list)
        emailobj.send()
        return 0
    except:
        print('start_email error')
        return 1


def start():
    try:
        service_item_list = Service.objects.filter(data_status='WAIT')
        for service in service_item_list:
            service.date_started = datetime.now()
            processname = '/Users/jangjuhyeon/IdeaProjects/djangoprj/mytest/service.sh %d' % service_item_list.id
            subprocess.call([processname], shell=True)
            service.data_status = 'EXEC'
            service.save()
            send_email(service.id, 0)
        return 0
    except:
        print('start routine error')
        return 1


def exec():
    try:
        service_item_list = Service.objects.filter(data_status='EXEC')
        for service in service_item_list:
            filepath = '/static/ServiceImage/' + '%d' % service.id + '/result.ply'
            output = os.path.isfile(filepath)
            if output is True:
                service.date_ended = datetime.now()
                service.data_status = 'SUCC'
                service.save()
                send_email(service.id, 1)
            else:
                timediff = datetime.now() - service.start_time
                timediffhours = timediff.total_seconds() / 3600
                if timediffhours > 3:
                    service.data_ended = datetime.now()
                    service.data_status = 'FAIL'
                    service.save()
                    send_email(service.id, 2)
        return 0
    except:
        print('exec routine error')
        return 1


def scheduled_job():
    print("im running")
    start()
    exec()
    return
