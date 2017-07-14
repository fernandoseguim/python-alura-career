from django.shortcuts import render, redirect
from perfis.models import Perfil, Invite


def index(request):
    perfis_list = Perfil.objects.all()
    return render(request, 'index.html', {'perfis' : perfis_list, 'current_user' : get_perfil_logged(request)})


def view(request, perfil_id):

    perfil = Perfil.objects.get(id=perfil_id)
    perfil_logged = get_perfil_logged(request)
    is_contact = perfil in perfil_logged.contacts.all()
    print(is_contact)
    return render(request, 'perfil.html', {'perfil' : perfil, 'is_contact' : is_contact })


def invite(request, perfil_id):
    perfil_invited = Perfil.objects.get(id=perfil_id)
    perfil_logged = get_perfil_logged(request)
    perfil_logged.to_invite(perfil_invited)
    return redirect('index')


def accept_invite(request, invite_id):
    invite = Invite.objects.get(id=invite_id)
    invite.accept()
    return redirect('index')

def get_perfil_logged(request):
    return Perfil.objects.get(id=1)




