from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from app.models import Horse
from app.models import Owner
from app.models import Jockey
from app.models import Games
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def Hourse(request):
    if 'add' in request.GET:
        if 'submit' in request.POST:
            h = Horse(
                name = request.POST['name'],
                male = request.POST['male'],
                age = request.POST['age'],
              )
            h.save()
        return render_to_response('app/horse-add.html')
    if 'edit' in request.GET:
        if 'submit' in request.POST:
            Horse.objects.filter(horse_id = request.GET['edit']).update(
                name = request.POST['name'],
                male = request.POST['male'],
                age = request.POST['age'],
                )
        fields = Horse.objects.get(horse_id = request.GET['edit'])
        return render_to_response('app/horse-edit.html', {'item': fields})
    if 'delete' in request.GET:
         Horse.objects.filter(horse_id = request.GET['delete']).delete()
    data = Horse.objects.all()
    return render_to_response('app/main.html',{'data': data})


@csrf_exempt
def Owners(request):
    if 'add' in request.GET:
        if 'submit' in request.POST:
            h = Owner(
                name = request.POST['name'],
                address = request.POST['address'],
                rate = request.POST['rate'],
                age = request.POST['age'],
              )
            h.save()
        return render_to_response('app/owner-add.html')
    if 'edit' in request.GET:
        if 'submit' in request.POST:
            Owner.objects.filter(owner_id = request.GET['edit']).update(
                name = request.POST['name'],
                address = request.POST['address'],
                rate = request.POST['rate'],
                age = request.POST['age'],
                )
        fields = Owner.objects.get(owner_id = request.GET['edit'])
        return render_to_response('app/owner-edit.html', {'item': fields})
    if 'delete' in request.GET:
         Owner.objects.filter(owner_id = request.GET['delete']).delete()
    data = Owner.objects.all()
    return render_to_response('app/owner.html',{'data': data})

@csrf_exempt
def Jockeys(request):
    if 'add' in request.GET:
        if 'submit' in request.POST:
            h = Jockey(
                name = request.POST['name'],
                address = request.POST['address'],
                age = request.POST['age'],
                rate = request.POST['rate'],
              )
            h.save()
        return render_to_response('app/jockeys-add.html')
    if 'edit' in request.GET:
        if 'submit' in request.POST:
            Jockey.objects.filter(jockey_id = request.GET['edit']).update(
                name = request.POST['name'],
                address = request.POST['address'],
                age = request.POST['age'],
                rate = request.POST['rate'],
                )
        fields = Jockey.objects.get(jockey_id = request.GET['edit'])
        return render_to_response('app/jockeys-edit.html', {'item': fields})
    if 'delete' in request.GET:
         Jockey.objects.filter(jockey_id = request.GET['delete']).delete()
    data = Jockey.objects.all()
    return render_to_response('app/jockeys.html',{'data': data})

@csrf_exempt
def Game(request):
    if 'add' in request.GET:
        if 'submit' in request.POST:
            h = Games(
                date = request.POST['date'],
                time = request.POST['time'],
                place = request.POST['place'],
                game_name = request.POST['game_name'],
              )
            h.save()
        return render_to_response('app/games-add.html')
    if 'edit' in request.GET:
        if 'submit' in request.POST:
            Games.objects.filter(game_id = request.GET['edit']).update(
                date = request.POST['date'],
                time = request.POST['time'],
                place = request.POST['place'],
                game_name = request.POST['game_name'],
                )
        fields = Games.objects.get(game_id = request.GET['edit'])
        return render_to_response('app/games-edit.html', {'item': fields})
    if 'delete' in request.GET:
         Games.objects.filter(game_id = request.GET['delete']).delete()
    data = Games.objects.all()
    return render_to_response('app/games.html',{'data': data})