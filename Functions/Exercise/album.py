def make_album(aritst_name, album_title, songs=None):
    """Return a dictionary of information about the album."""
    album = {'name': aritst_name, 'title': album_title}
    if songs:
        album['song'] = songs
    return album

musician = make_album('drake', 'take care', songs=17)
print(musician)

musician = make_album('jcole', 'the fall off')
print(musician)

musician = make_album('giveon', 'beloved', songs=14)
print(musician)

# Using while loop to allow a user to enter an album's artist and title.
def make_album(aritst_name, album_title):
    """Return a dictionary of information about the album."""
    album = {'name': aritst_name, 'title': album_title}
    return album

while True:
    print("\nPlease tell me the name of the artist and album:")
    print("(enter 'q' at any time to quit)")

    a_name = input("Artist name: ")
    if a_name == 'q':
        break
    
    a_title = input("Album title: ")
    if a_title == 'q':
        break

    formatted_album = make_album(a_name, a_title)
    print(f"\nAlbum info: {formatted_album}")
