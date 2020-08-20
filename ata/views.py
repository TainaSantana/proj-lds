from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.contrib import messages
from django.core.mail import send_mail, EmailMessage
from django.conf import settings


@login_required
def ataslist(request):
    return render(request,'atas/atalist.html', {})

"""
@login_required
def ataNew(request):
    if request.method == 'POST':
        pass

        if form.is_valid():
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
def ataEdit(request, id):
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
def ataDelete(request, id):
    reuniao = get_object_or_404(Reuniao, pk=id)
    reuniao.delete()
    messages.info(request, 'Reunião deletada com sucesso!')
    return redirect('/')

"""
