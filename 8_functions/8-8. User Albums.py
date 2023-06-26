def make_album(artist, album, number_of_songs=None):
    artist_info = {'artist': artist, 'album': album}
    if number_of_songs:
        artist_info['number_of_songs'] = number_of_songs
    return artist_info

while True:
    print("Please enter artist and album")
    print("Type 'q' to quit")
    inp_artist = input("Artist: ")
    if inp_artist == 'q':
        break
    inp_album = input("Album: ")
    if inp_album == 'q':
        break

    artist_and_album = make_album(inp_artist, inp_album)
    print(artist_and_album)