def make_album(singer, album, song_number = 0) :
    ret = {
        'Singer': singer,
        'Album': album,
        'number_of_song': song_number
    }
    return ret

def main() :
    while True :
        singer, album = input("Enter a singer and his or her album: ").split()
        print(make_album(singer, album))
        is_continue = input("Keep inputting?(y/n) > ")
        if is_continue == 'n' :
            break

# =============================================

main()