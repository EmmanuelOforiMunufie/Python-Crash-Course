def make_album(artist_name, album_title):
    """Dictionary describing album"""
    artist = {"name":artist_name.title(), "title":album_title.title()}
    return artist

performer = make_album("m.anifest", "no where cool")
print(performer)

performer = make_album("kojo cue","for my brothers")
print(performer)

performer = make_album("j cole", "2015 forest hills drive")
print(performer)


#With Tracks
def make_album(artist_name, album_title,tracks =0):
    """Dictionary describing album"""
    artist = {"name":artist_name.title(), "title":album_title.title()}
    
    if tracks:
        artist["tracks"] = tracks
    return artist

performer = make_album("m.anifest", "no where cool", tracks=14)
print(performer)

performer = make_album("kojo cue","for my brothers")
print(performer)

performer = make_album("j cole", "2015 forest hills drive")
print(performer)
