""" Start with your program from Exercise 8-7. Write a while loop that allows users to enter an album’s artist and title. Once you have that information, call make_album() with the user’s input and print the dictionary that’s created. Be sure to include a quit value in the while loop. """

def make_album(nameStr, titleStr):
    """ Returns a dictionary of album infomation. """
    album = {'name' : nameStr, 'title' : titleStr }
    return album

while True:
    print("Enter the name and album of a artist you listen to:")
    print("enter 'q' at any time to quit")
    
    artist_name = input("What is the artist's name(s)?: ")
    if artist_name == 'q':
        print("Exit program.")
        break
    
    album_name = input("What is the name of the album?: ")
    if album_name == 'q':
        print("Exit program.")
        break

    album_info = make_album(artist_name, album_name)
    print(album_info)

