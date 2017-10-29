import sys, getopt, taglib
from os import walk
from os import listdir
from os.path import isfile, join

def usage():
  print('''
  "--dir" The directory that you want to have all the unwanted tags removed.
  "--type" The type of file to effect e.g mp3, flac, etc.
  ''')

try:
  opts, args = getopt.getopt(sys.argv[1:], "ty:dr:h", ['type=', 'dir=', 'help'])
except getopt.GetoptError:
  usage()
  sys.exit(2)

for opt, arg in opts:
  if opt in ("-dr", '--dir'):
    dir_to = arg
  elif opt in ("-ty", '--type'):
    type_file = arg
  elif opt in ('h', '--help'):
    usage()
    sys.exit(2)
  else:
    usage()
    sys.exit(2)

for root, dirs, files in walk(dir_to):
  for file in [f for f in files]:
    if file.endswith(type_file):
      song = taglib.File(join(dir_to, file))
      liked_attr = ['ALBUM', 'ALBUMARTIST', 'YEAR', 'DATE','TITLE', 'GENRE', 'ARTIST', 'TRACKNUMBER']
      for attr in list(song.tags):
        if attr not in liked_attr:
          del song.tags[attr]
      song.save()