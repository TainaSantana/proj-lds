from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponse
from .models import Reuniao
from .form import MeetForm
from django.contrib import messages
from django.core.mail import send_mail, EmailMessage, send_mass_mail
from django.conf import settings
from smtplib import SMTP


@login_required

def search(request):
    search = request.GET.get('search')

    if search:
        reunioes = Reuniao.objects.filter(titulo__icontains=search)

def meetList(request):

    reunioes_list = Reuniao.objects.all().order_by('-created_at')

    paginator = Paginator(reunioes_list, 3)

    page = request.GET.get('page')

    reunioes = paginator.get_page(page)

    return render(request,'reunioes/list.html', {'reunioes': reunioes})

@login_required
def meetPauta(request, id):
    reuniao = get_object_or_404(Reuniao, pk=id)
    return render(request, 'reunioes/pauta.html', {'reuniao': reuniao})

def meetAbout(request):
    about = Reuniao.objects.all()
    return render(request, 'reunioes/sobre.html', {'about': about})

@login_required
def newMeet(request):
    if request.method == 'POST':
        form = MeetForm(request.POST)

        if form.is_valid():
            """
            toaddress = form.cleaned_data['email']
            to = str(toaddress.split(", "))
            tot = to.replace("'", "")
            #to = tot.strip('"')
            #to = to.replace("'")
            send_mail(
                'Subject',
                'Message.',
                'taina.santana262@gmail.com',
                [tot],
)"""
            
            sendfrom = 'settings.EMAIL_HOST_USER'
            toaddress = form.cleaned_data['email']
            subject = form.cleaned_data['titulo']
            message = form.cleaned_data['descricao']
            send_mail(subject, message, sendfrom, [toaddress])
            reuniao = form.save(commit=True)
            reuniao.save()
            return redirect('/')
    else:
        form = MeetForm
        return render(request, 'reunioes/newmeet.html', {'form': form})

@login_required
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

@login_required
def deleteMeet(request, id):
    reuniao = get_object_or_404(Reuniao, pk=id)
    reuniao.delete()
    messages.info(request, 'Reunião deletada com sucesso!')
    return redirect('/')

@login_required
# funcão de teste de e-mail, ainda nao testado
def emailMeet(request, id):
    reuniao = get_object_or_404(Reuniao, pk=id)
    form = MeetForm(instance=reuniao)

    if request.method == 'POST':
        form = MeetForm(request.POST, instance=reuniao)

        if form.is_valid():
            sendfrom = 'settings.EMAIL_HOST_USER'
            toaddress = form.cleaned_data['email']
            subject = 'Convite'
            message = 'para reuniao'
            smtp.sendmail (subject, message, sendfrom, [toaddress])
            return redirect('/')
        else:
            return render(request, 'reunioes/list.html', {'form': form, 'reuniao': reuniao})
        
    #return render(request,"list.html")


"""
# esse funciona com a pagina email.html
def sendEmail(request):
    if request.method == "GET":
        form = MeetForm()
    else:
        form = MeetForm(request.POST)
        if form.is_valid():
            sendfrom = 'settings.EMAIL_HOST_USER'
            toaddress = form.cleaned_data['email']
            subject = form.cleaned_data['titulo']
            message = form.cleaned_data['descricao']
            send_mail(subject, message, sendfrom, [toaddress])
            # send_mail(subject, message, fromemail, ['taisantis308@gmail.com', fromemail])
    return render(request, 'reunioes/newmeet.html', {'form': form})



# funcionooooooooooooou - esse form enviar e-mail com informações do formulário
def sendEmail(request):
    if request.method == "GET":
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            sendfrom = 'settings.EMAIL_HOST_USER'
            toaddress = form.cleaned_data['toaddress']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            send_mail(subject, message, sendfrom, [toaddress])
            # send_mail(subject, message, fromemail, ['taisantis308@gmail.com', fromemail])
    return render(request, 'reunioes/email.html', {'form': form})
"""
"""
# esse funciona
def sendEmail(request):

    subject = request.POST.get('assunto')
    message = 'n funciona'
    sendfrom = 'settings.EMAIL_HOST_USER'
    toaddress = ['taisantis308@gmail.com']
    send_mail(subject, message, sendfrom, toaddress)
"""

