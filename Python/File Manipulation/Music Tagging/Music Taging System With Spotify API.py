import spotipy
import sys, getopt, taglib
from spotipy.oauth2 import SpotifyClientCredentials
from os import walk
# from os import listdir
from subprocess import Popen, PIPE, call
from os.path import isfile, join
from re import sub


def usage():
  print('''
  "--album-uri" The uri of an album on Spotify
  "--dir" The directory that contains the album of music that you want to set the genre of.
  "--type" The file extension of the files that you want to effect
  ''')

try:
  opts, args = getopt.getopt(sys.argv[1:], "", ['album-uri=', 'dir=', 'type=', 'album-art-dir=', 'help'])
except getopt.GetoptError:
  usage()
  sys.exit(2)

for opt, arg in opts:
  if opt in ("", '--album-uri'):
    album_uri = arg
  elif opt in ("", '--dir'):
    dir_to = arg
  elif opt in ("", '--type'):
    file_extention = arg
  elif opt in ("", '--album-art-dir'):
    album_art_dir = arg
  elif opt in ("", '--help'):
    usage()
    sys.exit(2)
  else:
    usage()
    sys.exit(2)

for root, dirs, files in walk(dir_to):
  for file in [f for f in files]:
    if file.endswith(file_extention):
      song = taglib.File(join(dir_to, file))
      liked_attr = ['ALBUM', 'ARTIST', 'DATE', 'TITLE', 'GENRE', 'TRACKNUMBER', 'TRACKTOTAL', 'COPYRIGHT']
      for attr in list(song.tags):
        if attr not in liked_attr:
          del song.tags[attr]
      song.save()

sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

# month_relation = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}

album_dict = sp.album(album_uri)
artist = sp.artist(album_dict['artists'][0]['uri'])
track_total = album_dict['tracks']['total']
album_name = album_dict['name']
album_cover = album_dict['images'][0]['url']
album_type = album_dict['album_type']
release_year = album_dict['release_date'].split('-')[0]
copyright = album_dict['copyrights'][0]['text']
copyright = sub("^\s+","", copyright)
copyright = sub('^[(A-Za-z)|\u00A9|\u2117]+', '', copyright)
copyright = sub("^\s+","", copyright)
year = album_dict['release_date'].split('-')[0]
# release_date = album_dict['release_date']
genre = artist['genres']

i = 0
for x in genre:
  genre[i] = genre[i].title()
  i+=1

i = 0
for x in range(track_total):
  track_uri = album_dict['tracks']['items'][i]['uri']
  track_dict = sp.track(track_uri)
  album_artist = []
  track_number = track_dict['track_number']
  track_name = album_dict['tracks']['items'][x]['name']
  valid_track_file = sub('[\/\\\?\*\:\"\<\>]+', '', track_name)
  valid_track_file = sub('\s+',' ', valid_track_file)
  file_name = valid_track_file.rsplit('.',1)[0]
  file_path = dir_to + valid_track_file + file_extention

  for t in range(16):
    try:
      if t == 0:
        album_artist.append(track_dict['artists'][t]['name'])
    except:
      continue
  i+=1
  try:
    song = taglib.File(file_path)
  except:
    continue
  song.tags['TRACKNUMBER'] = [str(track_number)]
  song.tags['TRACKTOTAL'] = [str(track_total)]
  song.tags['COPYRIGHT'] = [copyright]
  song.tags['GENRE'] = genre
  song.tags['DATE'] = [year]
  song.tags['ARTIST'] = album_artist
  song.tags['TITLE'] = [track_name]
  # song.tags['ALBUMARTIST'] = album_artist
  song.tags['ALBUM'] = album_name
  song.save()

invalid_album_name = album_name
invalid_artist_name = track_dict['artists'][0]['name']
valid_album_name = sub('[\/\\\?\*\:\"\<\>]+', '', invalid_album_name)
valid_artist_name = sub('[\/\\\?\*\:\"\<\>]+', '', invalid_artist_name)
call(['wget', "--directory-prefix={0}".format(album_art_dir), "--output-document={a}{b} - {c}.jpg".format(a=album_art_dir, b=valid_artist_name, c=valid_album_name), album_cover])