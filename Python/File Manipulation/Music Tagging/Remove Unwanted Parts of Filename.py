import sys, getopt
from os import walk
from os import listdir
from os import rename
from os.path import isfile, join

def usage():
  print('''
  "--dir" is the location of where all the files that you want to do the action to.
  "--type" is the file extension so that it will only affect those certain files.
  "--split" is the character to split the file name in order to remove the digits from the beginning of the file name.
  ''')

try:
  opts, args = getopt.getopt(sys.argv[1:], "d:t:s:h", ['dir=', 'type=', 'split=', 'help'])
except getopt.GetoptError:
  usage()
  sys.exit(2)

for opt, arg in opts:
  if opt in ('-d', '--dir'):
    root_dir = arg
  elif opt in ('-t', '--type'):
    file_type = arg
  elif opt in ('-s', '--split'):
    char_to_split_on = arg
  elif opt in ('-h', '--help'):
    usage()
    sys.exit(2)
  else:
    usage()
    sys.exit(2)

for root, dirs, files in walk(root_dir):
  for file in [f for f in files]:
    if file.endswith(file_type):
      old_filepath = (join(root, file))
      _, new_filepath = file.split(char_to_split_on, 1)
      new_filepath = (join(root, new_filepath))
      rename(old_filepath, new_filepath)