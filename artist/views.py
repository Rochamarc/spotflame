from django.shortcuts import render

from .models import Band, Album, Song

from .lib import most_rated_artists, list_check, take_top

def index(request):
    song_list = Song.objects.all()
    band_list = Band.objects.all()

    short_song_list = list_check(song_list, 5) # return a list with 5 random songs

    rated_artists = most_rated_artists(band_list)
    band_list = list_check(rated_artists, 4) # return a list with 4 random rated bands

    context = {'songs': short_song_list, 'bands': band_list}
    return render(request,'artist/index.html', context) # busca pelo template na pasta template

def bands_index(request):
    band_list = Band.objects.all()
    context = { 'bands': band_list }
    return render(request, 'artist/bands.html', context)

def band_detail(request, pk):
    # filter band by id
    band = Band.objects.filter(id=pk)
    
    song_band_detail = Song.objects.filter(artist = band[0])
    album_band_detail = Album.objects.filter(band = band[0])
    
    context = { 
        'pk': pk, 
        'band_detail': band, 
        'songs': song_band_detail, 
        'albums': album_band_detail 
    }
    return render(request, 'artist/band_detail.html', context)

def album_detail(request, pk):
    album = Album.objects.filter(id=pk)
    songs = Song.objects.filter(album = album[0])

    context = {
        'pk': pk,
        'album_detail': album,
        'songs': songs
    }

    return render(request, 'artist/album_detail.html', context)

# Page of the most rated album and bands
def top_index(request):
    top_bands_list = list(Band.objects.all())
    top_albums_list = list(Album.objects.all())
    
    # sort album and bands by votes
    top_bands_list.sort(key=take_top, reverse=True) 
    top_albums_list.sort(key=take_top, reverse=True) 

    top_bands = []
    top_albums = []

    try:
        for i in range(4):
            top_bands.append(top_bands_list[i]) # 4 most rated bands
            top_albums.append(top_albums_list[i]) # 4 most rates albums
    except:
        pass

    context = {
        'top_bands': top_bands,
        'top_albums': top_albums
    }

    return render(request, 'artist/top.html', context)