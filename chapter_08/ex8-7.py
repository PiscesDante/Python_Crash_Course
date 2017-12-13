def make_album(singer, album, song_number = 0) :
    ret = {
        'Singer': singer,
        'Album': album,
        'number_of_song': song_number
    }
    return ret

print(make_album('Bryan Adam', 'Spirit: Stallion Of The Cimarron'))
print(make_album('Justin Timberlake', 'Inside Llewyn Davis', 14))