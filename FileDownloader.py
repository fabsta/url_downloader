from urllib2 import urlopen, URLError, HTTPError
#import re
import os.path
import imghdr

class FileDownloader:
	'FileDownloader class that handles file downloads'
	
	
	
	def __init__(self):
		self._urls = []
		self._allowed_image_types =   {'png': 1, 'jpg':1, 'gif':1, 'jpeg':1,'svg':1}
	

	@property
	def urls(self):
		return self._urls

	@urls.setter
	def urls(self,urls):
		self._urls  = urls
	

	def add_url(self,url):
		self._urls.append(url)
	

	'''
        Returns an array with urls read from a file

        :Parameters:
        -`file`: The input file
    '''
	def read_file(self,file):
		
		try:
	 		f = open(file)
			for line in iter(f):
				#self.urls.append(line.rstrip("\r\n"))
				self.add_url(line.rstrip("\r\n"))
			f.close()	
		except IOError:
			return 'Cannot open file'	



	def download_image(self,source,destination):
		if source == '':
			return 'not a valid url'
		if destination == '':
			return 'not a valid destination'	
		if self.has_valid_image_extension(source):
			if(self.download_file(source, destination)):
				if(self.is_real_image(destination)):
					return "success"
				else:
					return "downloaded file is not an image"	
			else:
				return "could not download file"
		else:	
			return 'not a valid image file extension'


	def download_file(self,source,destination):
		try:
			f = urlopen(source)
			print "downloading " + source
			# Open our local file for writing
			try:
				with open(destination, "wb") as local_file:
					local_file.write(f.read())
					print "saved file?"
			except IOError:
				return 0
			saved = self.has_saved_file(destination)
			print saved
				
			return "success"
		except HTTPError, e:
			return e.code
		except URLError, e:
			return e.args		
		else: 
			'everything fine'	

	def has_valid_image_extension(self,source):
		file_name = source.split('/')[-1]
		extension = file_name.split('.')[-1]
		if not extension in self._allowed_image_types:
			return 'not a valid image file extension'
		else:
			return 1

	def has_saved_file(self,destination):
		print "checking saved file"
		if(os.path.exists(destination)):
			print "file exists"
			if(os.stat(destination).st_size != 0):
				print "was successful"
				return "success"
			else:
				print "but is empty"
				return FALSE
		else:
			print "file does not exist"
			return FALSE

	def is_real_image(self, file):
		if(imghdr.what(file) in self._allowed_image_types):
			return "good"
		else:
			return	0
		