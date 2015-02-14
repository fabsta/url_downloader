import sys
import os
from urllib2 import Request, urlopen, URLError

from FileDownloader import FileDownloader;

if len(sys.argv) < 2:
	print "Please provide a file with urls to download"
	sys.exit(0)

file_dl = FileDownloader()
file_dl.read_file(sys.argv[1])
urls_array = file_dl.urls

for source in urls_array:
	print "downloading %s." %source
	file_dl.download_image(source, os.path.basename(source))