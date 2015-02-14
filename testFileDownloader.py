import unittest;
from FileDownloader import FileDownloader;
import os.path

class TestFileDownloader(unittest.TestCase):
	
	def setUp(self):
		self.file_dl = FileDownloader()
	def tearDown(self):
		self.file_dl = ''

	'''
        Should fail if no file given
    '''
	def test_read_nonexisting_file(self):
		self.assertEqual(self.file_dl.read_file(''),'Cannot open file')
	'''
        Should return empty list of urls if empty file given
    '''
	def test_read_empty_file(self):
		print self.file_dl
		self.file_dl.read_file('empty.txt')
		self.assertEqual(self.file_dl.urls,[])
	'''
        Should return empty list of urls
    '''
	#def test_add_url(self):
	#	self.file_dl.add_url('www.google.de')
	#	urls_array = self.file_dl.get_urls()
	#	self.assertEqual(len(urls_array),1)
	#	self.assertEqual(urls_array, ['www.google.de'])

	def test_read_url_file(self):
		self.file_dl.read_file('input.txt')
		urls_array = self.file_dl.urls
		print urls_array
		self.assertEqual(len(urls_array), 3)
		self.assertEqual(urls_array, 
					['http://thumb1.shutterstock.com/display_pic_with_logo/766909/144037588/stock-vector-grunge-rubber-red-stamp-with-word-example-inside-vector-illustration-144037588.jpg',
					'https://assets.crowdsurge.com/datacapture/example/img/example_logo.png',
					'http://genesis-theme-aestetics.esy.es/wp-content/uploads/2014/10/example.jpg'])
	
	'''
        Should return 'not a valid image file extension' if url doesn't end with a image extension
    '''
	def test_no_image_extension_url(self):
		self.assertEqual(self.file_dl.has_valid_image_extension("www.internet.com/image.txt"), 'not a valid image file extension')	
	

	'''
        We should be able to download a file from the internet
    '''	
    #def test_valid_download(self):
	#	self.assertEqual(self.file_dl.download_file('',''), 'not a valid url')
	
	'''
        Should return 'not a valid url' for missing url
    '''
	def test_valid_url(self):
		self.assertEqual(self.file_dl.download_image('',''), 'not a valid url')
	
	'''
        Should return 'not a valid destination' if no destination has been specified
    '''
	def test_no_destination(self):
		self.assertEqual(self.file_dl.download_image("http://phfwc.org/wp-content/uploads/2015/01/example",''), 'not a valid destination')	
	
	'''
        Should return 'not a valid image file extension' if url doesn't end with a image extension
    '''
	def test_download_success(self):
		self.assertEqual(self.file_dl.download_image("https://assets.crowdsurge.com/datacapture/example/img/example_logo.png",'download.txt'), 'success')	
	

	def test_download_failed(self):
		self.assertEqual(self.file_dl.download_image("http://phfwc.org/wp-content/uploads/2015/01/example.jpg",'/download.txt'), 'could not download file')	
	
	def test_download_no_image_failed(self):
		self.assertEqual(self.file_dl.download_image("http://www.google.de",'download.txt'), 'downloaded file is not an image')	
	
