from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.http import HttpResponse
from .models import Reuniao
from .form import MeetForm
from django.contrib import messages
from django.core.mail import send_mail, EmailMessage
from django.conf import settings


def meetList(request):
    reunioes_list = Reuniao.objects.all().order_by('-created_at')

    paginator = Paginator(reunioes_list, 3)

    page = request.GET.get('page')

    reunioes = paginator.get_page(page)

    return render(request,'reunioes/list.html', {'reunioes': reunioes})

def meetPauta(request, id):
    reuniao = get_object_or_404(Reuniao, pk=id)
    return render(request, 'reunioes/pauta.html', {'reuniao': reuniao})

def meetAbout(request):
    about = Reuniao.objects.all()
    return render(request, 'reunioes/sobre.html', {'about': about})

def newMeet(request):
    if request.method == 'POST':
        form = MeetForm(request.POST)

        if form.is_valid():
            reuniao = form.save(commit=True)
            reuniao.save()
            return redirect('/')
    else:
        form = MeetForm
        return render(request, 'reunioes/newmeet.html', {'form': form})

def editMeet(request, id):
    reuniao = get_object_or_404(Reuniao, pk=id)
    form = MeetForm(instance=reuniao)

    if request.method == 'POST':
        form = MeetForm(request.POST, instance=reuniao)

        if form.is_valid():
            reuniao.save()
            return redirect('/')
        else:
            return render(request, 'reunioes/editmeet', {'form': form, 'reuniao': reuniao})
        
    else:
        return render(request, 'reunioes/editmeet.html', {'form': form, 'reuniao': reuniao})

def deleteMeet(request, id):
    reuniao = get_object_or_404(Reuniao, pk=id)
    reuniao.delete()
    messages.info(request, 'Reunião deletada com sucesso!')
    return redirect('/')


# esse funciona
def sendEmail(request):

    subject = request.POST.get('assunto')
    message = 'n funciona'
    sendfrom = 'settings.EMAIL_HOST_USER'
    toaddress = ['taisantis308@gmail.com']
    send_mail(subject, message, sendfrom, toaddress)


