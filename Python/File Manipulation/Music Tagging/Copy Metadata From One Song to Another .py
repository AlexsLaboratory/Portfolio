import sys, getopt, taglib
from os import walk
from os import listdir
from os.path import isfile, join

def usage():
  print('''
  "--dir-from" The directory that has the correct tags that you want to then copy to files in the other directory.
  "--dir-to" The directory that has the files that you want but does not have the correct tags.
  "--type-to" The type of file to effect e.g mp3, flac, etc.
  ''')

try:
  opts, args = getopt.getopt(sys.argv[1:], "df:dt:tt:h", ['dir-from=', 'dir-to=', 'type-to=','help'])
except getopt.GetoptError:
  usage()
  sys.exit(2)

for opt, arg in opts:
  if opt in ("-df", '--dir-from'):
    dir_from = arg
  elif opt in ("-dt", '--dir-to'):
    dir_to = arg
  elif opt in ('-tt', '--type-to'):
    extention_to = arg
    if extention_to.startswith(".") == False:
      extention_to = "." + extention_to
  elif opt in ('h', '--help'):
    usage()
    sys.exit(2)
  else:
    usage()
    sys.exit(2)

for root, dirs, files in walk(dir_from):
  for file in [f for f in files]:
    from_file_loc = join(root, file)
    song_from = taglib.File(from_file_loc)
    file_name_from_only = file.rsplit('.',1)[0]
    song_to = taglib.File(join(dir_to, file_name_from_only + extention_to))

    liked_attr = ['ALBUM', 'ARTIST', 'DATE', 'TITLE', 'GENRE', 'TRACKNUMBER', 'TOTALTRACKS', 'COPYRIGHT']

    for attr in list(song_to.tags):
      if attr not in liked_attr:
        del song_to.tags[attr]

    song_to.tags["TRACKNUMBER"] = song_from.tags["TRACKNUMBER"]
    song_to.tags["GENRE"] = song_from.tags["GENRE"]
    song_to.tags['DATE'] = song_from.tags['DATE']
    song_to.tags['ARTIST'] = song_from.tags['ARTIST']
    song_to.tags['TITLE'] = song_from.tags['TITLE']
    song_to.tags['ALBUM'] = song_from.tags['ALBUM']
    song_to.tags['TOTALTRACKS'] = song_from.tags['TOTALTRACKS']
    song_to.tags['COPYRIGHT'] = song_from.tags['COPYRIGHT']
    song_to.save()