import spotipy
import sys, getopt, taglib
from spotipy.oauth2 import SpotifyClientCredentials
from os import walk
# from os import listdir
from subprocess import Popen, PIPE, call
from os.path import isfile, join
from re import sub

try:
  opts, args = getopt.getopt(sys.argv[1:], "", ['dir=', 'help'])
except getopt.GetoptError:
  usage()
  sys.exit(2)

for opt, arg in opts:
  if opt in ("", '--dir'):
    dir_to = arg
  elif opt in ("", '--help'):
    usage()
    sys.exit(2)
  else:
    usage()
    sys.exit(2)

for root, dirs, files in walk(dir_to):
  for file in [f for f in files]:
    if file.endswith('.flac'):
      song = taglib.File(join(root, file))
      if "ORIGINAL_FLAC" not in list(song.tags):
        print(file)