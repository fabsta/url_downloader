import unittest;
import sys, os
testdir = os.path.dirname(__file__)
srcdir = '../src/'
sys.path.insert(0, os.path.abspath(os.path.join(testdir, srcdir)))

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
		with self.assertRaises(IOError) as context:
			self.file_dl.read_file('')
		self.assertTrue('Cannot open file' in context.exception)

	'''
        Should return empty list of urls if empty file given
    '''
	def test_read_empty_file(self):
		self.file_dl.read_file('download/empty.txt')
		self.assertEqual(self.file_dl.urls,[])


	'''
		Should read a file with urls
	'''
	def test_read_url_file(self):
		self.file_dl.read_file('input.txt')
		urls_array = self.file_dl.urls
		self.assertEqual(len(urls_array), 3)
		self.assertEqual(urls_array, 
					['http://thumb1.shutterstock.com/display_pic_with_logo/766909/144037588/stock-vector-grunge-rubber-red-stamp-with-word-example-inside-vector-illustration-144037588.jpg',
					'https://assets.crowdsurge.com/datacapture/example/img/example_logo.png',
					'http://genesis-theme-aestetics.esy.es/wp-content/uploads/2014/10/example.jpg'])
	
	'''
        Should return 'not a valid image file extension' if url doesn't end with a image extension
    '''
	def test_no_image_extension_url(self):
		with self.assertRaises(TypeError) as context:
			self.file_dl.has_valid_image_extension("www.internet.com/image.txt")
		self.assertTrue('not a valid image file extension' in context.exception)

	'''
       checking for valid url
    '''
	def test_error_on_invalid_url(self):
		with self.assertRaises(ValueError) as context:
			self.file_dl.valid_url('a')
		self.assertTrue('url has no schema' in context.exception)



	'''
       Should raise a ValueError for url not in url format
    '''
	def test_download_throws_http_error(self):
		with self.assertRaises(ValueError) as context:
			self.file_dl.download_file('a','b')
		self.assertTrue('url has no schema' in context.exception)


	'''
       Should raise a value error for missing url 
    '''
	def test_no_url_give(self):
		with self.assertRaises(ValueError) as context:
			self.file_dl.download_image('','')
		self.assertTrue('no url provided' in context.exception)
	'''
        Should raise a ValueError 'not a valid destination' if no destination has been specified
    '''
	def test_no_destination(self):
		with self.assertRaises(ValueError) as context:
			self.file_dl.download_image("http://phfwc.org/wp-content/uploads/2015/01/example",'')
		self.assertTrue('not a valid destination' in context.exception)
	
	'''
        Should return 'not a valid image file extension' if url doesn't end with a image extension
    '''
	def test_download_success(self):
		#self.assertEqual(self.file_dl.download_image("https://assets.crowdsurge.com/datacapture/example/img/example_logo.png",'download.txt'), 'success')	
		self.assertTrue(self.file_dl.download_image("https://assets.crowdsurge.com/datacapture/example/img/example_logo.png",'download/example_logo.png'))
	'''
        Should raise an IOError if file could not be downloaded
    '''
	def test_download_failed(self):
		with self.assertRaises(IOError) as context:
			self.file_dl.save_file("http://phfwc.org/wp-content/uploads/2015/01/example.jpg",'/download.txt')
		self.assertTrue('could not save file' in context.exception)
	
	'''
        Check if file was saved
    '''
	def test_file_not_exists(self):
		with self.assertRaises(IOError) as context:
			self.file_dl.has_saved_file('/download.txt')
		self.assertTrue('file does not exist' in context.exception)

	'''
        Check if file is empty
    '''
	def test_is_empty(self):
		with self.assertRaises(IOError) as context:
			self.file_dl.has_saved_file('download/empty.txt')
		self.assertTrue('file is empty' in context.exception)
		
	'''
        Check if file exists
    '''
	def test_is_empty(self):
		self.assertTrue(self.file_dl.has_saved_file('download/example.jpg'))
	
	
	'''
        Checking a real image should work
    '''
	def test_is_real_image(self):
		self.assertTrue(self.file_dl.is_real_image('download/example.jpg'))
		
	'''
        Should raise an TypeError for non-image file
    '''
	def test_is_real_image(self):
		with self.assertRaises(ValueError) as context:
			self.file_dl.is_real_image('download/newsletter1.pdf')
		self.assertTrue('not an image format' in context.exception)
	

