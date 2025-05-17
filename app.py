
import json
import os
import time
import shutil
import requests

ENDPOINT = "https://be.heardleitalia.com/api"

def sendArtist(artista,key):

  with open("./ArtistiSongExtracted/"+artista, "r", encoding="utf-8") as file:
    data = json.load(file)
    length = len(data)
    start_time = time.time()
    response = requests.post(f'{ENDPOINT}/heardle/insert/song',headers={'Authorization': f'Bearer {key}', 'Content-Type': 'application/json', 'x-api-key': 'key'}, json=data)
    end_time = time.time()
    duration = end_time - start_time
    if(response.status_code == 200):
      file.close()
      if os.path.exists("./ArtistiSongSent/")==False:
        os.mkdir("./ArtistiSongSent/")    
      shutil.move("./ArtistiSongExtracted/"+artista, "./ArtistiSongSent/"+artista)
    else:
      print(response.status_code)
  return duration, length



def main():
  artistList = os.listdir("./ArtistiSongExtracted/")
  totaleDuration = 0
  totaleCanzoniInviate = 0
  for index,artista in enumerate(artistList): 
    response = requests.get(f'{ENDPOINT}/refresh')
    response_data = response.json()
    key = response_data["data"]
    print(f"------------------------------------------------------------------------------------")
    print(f'{index} of {len(artistList)} - {artista}')
    duration, canzoniInviate = sendArtist(artista,key=key)
    totaleDuration += duration
    totaleCanzoniInviate += canzoniInviate
    print(f'Canzoni inserite per {artista} n: {canzoniInviate}')
    print(f'Tempo impiegato per {artista} n: {duration:.2f} secondi')
    print(f"Tempo totale: {totaleDuration:.2f} secondi - Canzoni inviate: {totaleCanzoniInviate}")
    print(f"Tempo medio: {totaleDuration / totaleCanzoniInviate:.2f} secondi per canzone")


if __name__ == "__main__":
  main()