from mutagen.easyid3 import EasyID3
from mutagen.mp4 import MP4


def tags(fname, nome, autor, genre, album,ano):
    audio = MP4(fname)

    audio['©nam'] = nome
    audio['©ART'] = autor
    audio['©gen'] = genre
    audio['©alb'] = album
    audio['\xa9day'] = ano
    audio.save()
