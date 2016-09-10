from django.http import Http404
# from django.template import loader
from django.shortcuts import render
from .models import Album, Song


def index(request):
    all_albums = Album.objects.all()
    # template = loader.get_template('music/index.html')
    context = {
        'all_albums': all_albums,
    }
    # for album in all_albums:
    #     url = "/music/{0}".format(album.id)
    #     html += "<a href=\"{0}\">{1}</a><br />".format(url, album.album_title)
    # return HttpResponse(template.render(context, request))
    return render(request, 'music/index.html', context)

def detail(request, album_id):
    try:
        album = Album.objects.get(pk=album_id)
    except Album.DoesNotExist:
        raise Http404("Album doesn't exist")

    return render(request, 'music/detail.html', { 'album': album })
