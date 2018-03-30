import difflib 
import sys 

fromfile = sys.argv[0];
tofile = sys.argv[1];
out_file_name =sys.argv[2];

out_file = open(out_file_name,"w+");
fromlines = open(fromfile, 'U').readlines();
tolines = open(tofile, 'U').readlines();

for line in  difflib.unified_diff(fromlines, tolines, fromfile, tofile):
    out_file.write(line)

out_file.close()