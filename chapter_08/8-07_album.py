""" Write a function called make_album() that builds a dictionary describing a music album. The function should take in an artist name and an album title, and it should return a dictionary containing these two pieces of information. Use the function to make three dictionaries representing different albums. Print each return value to show that the dictionaries are storing the album information correctly. """

def make_album(nameStr, titleStr):
    """ Returns a dictionary of album infomation. """
    album = {'name' : nameStr, 'title' : titleStr }
    return album


album_info = make_album('future and metro boomin', "we still don't trust you")
album_info0 = make_album('beyonce', 'cowboy carter')
album_info1 = make_album('taylor swift', 'lover')

print(album_info)
print(album_info1)
print(album_info0)
