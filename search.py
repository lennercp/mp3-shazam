import asyncio

from shazamio import Shazam

from tags import tags


def search(fname):
  shazam = Shazam()
  async def main():
    out = await shazam.recognize_song(fname)
    nome = (out['track']['title'])
    autor = (out['track']['subtitle'])
    genre = (out['track']['genres']['primary'])
    album = (out['track']['sections'][0]['metadata'][0]['text'])
    ano = out['track']['sections'][0]['metadata'][2]['text']

    nome = nome.lower().replace('(ao vivo)', '').title()
    album = album.lower().replace('(ao vivo)', '').title()

    if '- single' in album.lower():
      album = ''

    tags(fname, nome, autor, genre, album, str(ano))

  loop = asyncio.get_event_loop()
  loop.run_until_complete(main())
