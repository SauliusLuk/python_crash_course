def make_album(artist, album, number_of_songs=None):
    artist_info = {'artist': artist, 'album': album}
    if number_of_songs:
        artist_info['number_of_songs'] = number_of_songs
    return artist_info

album1 = make_album('queen', 'greatest hits')
album2 = make_album('david bowie', 'station to station', 10)
print(album1)
print(album2)
