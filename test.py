from pygame import mixer

mixer.init()
song = "C:\\Users\\ofero\\Documents\\Ofer\\Barcelona Music\\Coldplay - Hymn For The Weekend (Official Video).mp3"
queue_song = "C:\\Users\\ofero\\Documents\\Ofer\\Barcelona Music\\Con Calma - Daddy Yankee & Snow (Lyrics).mp3"
mixer.music.load(song)
mixer.music.set_volume(0.8)
mixer.music.play()
mixer.music.queue(queue_song)
