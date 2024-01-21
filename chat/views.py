from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from chat.models import Room


def index(request):
    if request.method == 'POST':
        name = request.POST.get('name', None)
        if name:
            room = Room.objects.create(name=name, host=request.user)
            return HttpResponseRedirect(
                reverse(
                    'room',
                    kwargs={'pk': room.pk},
                )
            )
    return render(request, 'chat/index.html')


def room(request, pk):
    room: Room = get_object_or_404(Room, pk=pk)
    return render(request, 'chat/room.html', {
        'room': room,
    })
