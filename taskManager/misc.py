import os

def store_uploaded_file(title, f):
	with open('%s/uploads/%s' % (os.path.dirname(os.path.realpath(__file__)), title), 'wb+') as destination:
		for chunk in f.chunks():
			destination.write(chunk)
	return '%s/uploads/%s' % (os.path.dirname(os.path.realpath(__file__)), title)