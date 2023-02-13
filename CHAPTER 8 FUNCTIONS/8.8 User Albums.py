def make_album(artist_name, album_title,tracks =0):
    """Dictionary describing album"""
    artist = {"name":artist_name.title(), "title":album_title.title()}
    
    if tracks:
        artist["tracks"] = tracks
    return artist


#Prompt respondent 
prompt_artist =("\nGive name of artist:")
prompt_album = ("What is the album title?")   

print("Enter q to quit")

while True:
    artist = input(prompt_artist)
    if artist == "q":
        break
    
    
    album = input(prompt_album)
    if album == "q":
        break
        
        
    album = make_album(artist,album)
    print (album)   
        
        
        
       