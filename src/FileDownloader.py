from urllib2 import urlopen, URLError, HTTPError
from urlparse import urlparse
import os.path
import imghdr

class FileDownloader:
	'FileDownloader class that handles file downloads'
	
	def __init__(self):
		"""
			constructor method for FileDownloader. Initiates an empty array of urls
			Defines allowed image types
	
		"""

		self._urls = []
		self._allowed_image_types =   {'png': 1, 'jpg':1, 'gif':1, 'jpeg':1,'svg':1, 'img':1}

	@property
	def urls(self):
		"""
			gets the current urls
	
			@rtype:   array
			@return:  list of urls.
		"""
		return self._urls

	@urls.setter
	def urls(self,urls):
		"""
			sets the urls
	
			@type  urls: array
			@param urls: list of urls
    		
		"""
		self._urls  = urls
	

	def add_url(self,url):
		"""
			adds a url to the list of urls
	
			@type  url: string
			@param url: url of file to be downloaded
    		
		"""
		self._urls.append(url)
	

	def read_file(self,file):
		"""
			Reads urls from a given file `file`.	
	
			@type  file: string
			@param file: file containing urls.
    		
			@rtype:   IOError
			@return:  error message in case the file could not be opened.
		"""
		try:
	 		f = open(file)
			for line in iter(f):
				self.add_url(line.rstrip("\r\n"))
			f.close()	
		except IOError:
			raise IOError('Cannot open file')

	def valid_url(self,source):
		"""
			Reads urls from a given file `file`.	
	
			@type  source: string
			@param source: url.
    		
			@rtype:   ValueError
			@return:  error message in case the url has no scheme like 'http' or 'ftp'.
		"""
		o = urlparse(source)
		if(not o.scheme):
			raise ValueError('url has no schema')
		else:
			return 1	

	def download_image(self,source,destination):
		"""
    		Downloads an image given by `source` and saves it into `destination`.	
	
			@type  source: string
			@param source: url.
    		
    		@type  destination: string
			@param destination: download location.
    		
			@rtype:   IOError
			@return:  error message in case the file could not be downloaded.
    	"""
		if source == '':
			raise ValueError('no url provided')
		if destination == '':
			raise ValueError('not a valid destination')
		if self.has_valid_image_extension(source):
			if(self.download_file(source, destination)):
				return self
			else:
				raise IOError('could not download file')
		else:	
			raise ValueError('not a valid image file extension')
	

	def save_file(self,f, destination):
		"""
    		Downloads an file given by `source` and saves it into `destination`.	
	
			@type  f: opened url
			@param f: downloaded url content.
    		
    		@type  destination: string
			@param destination: download location.

			@rtype:   IOError
			@return:  error message in case it could not be saved
		"""
		try:
			with open(destination, "wb") as local_file:
				local_file.write(f.read())
				if(self.has_saved_file(destination)):
					return 1
				else:
					raise IOError("could not save file")
		except IOError:
			raise IOError("could not save file")
			

	def download_file(self,source,destination):
		"""
    		Downloads an file given by `source` and saves it into `destination`.	
	
			@type  source: string
			@param source: url.
    		
    		@type  source: string
			@param source: download location.

			@rtype:   TypeError
			@return:  error message in case the url seems invalid.
    	"""
		try:
			if self.valid_url(source):
				f = urlopen(source)
				if(self.save_file(f,destination)):
					return 1
				else:
					return "error"		
			else:
				raise TypeError('url has no schema')

		except HTTPError, e:
			return e.code
		except URLError, e:
			return e.args		
		else:
			return 1	
		
	def has_valid_image_extension(self,source):
		"""
    		Checks whether a provided url looks like a image file by 
    		checking it's file extension
	
			@type  source: string
			@param source: url.
			
			@rtype:   TypeError
			@return:  error message in case the url does not have a valid image extension.
    	"""
		file_name = source.split('/')[-1]
		extension = file_name.split('.')[-1]
		if not extension in self._allowed_image_types:
			raise TypeError('not a valid image file extension')
		else:
			return 1

	def has_saved_file(self,destination):
		"""
    		Checks whether a file was successfully saved
	
			@type  destination: string
			@param destination: the file location.
			
			@rtype:   IOError
			@return:  error message in case the file was not saved.
    	"""
		if(os.path.exists(destination)):
			if(os.stat(destination).st_size != 0):
				return 1
			else:
				raise IOError ("file is empty")
		else:
			raise IOError ("file does not exist")

	def is_real_image(self, destination):
		"""
    		Checks whether a downloaded file is a real image file
	
			@type  destination: string
			@param destination: the file location.
			
			@rtype:   ValueError
			@return:   if it is not an image
    	"""
		if(imghdr.what(destination) in self._allowed_image_types):
			return 1
		else:
			raise ValueError("not an image format")
		