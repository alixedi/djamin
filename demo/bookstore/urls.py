from django.conf.urls import patterns

from djamin.core import ModelDjamin

from .models import Publisher, Author, Book


class PublisherDjamin(ModelDjamin):
	"""Publisher admin"""
	queryset = Publisher.objects.all()

publisher_djamin = PublisherDjamin()


class AuthorDjamin(ModelDjamin):
	"""Author admin"""
	queryset = Author.objects.all()

author_djamin = AuthorDjamin()


class BookDjamin(ModelDjamin):
	"""Book admin"""
	queryset = Book.objects.all()

book_djamin = BookDjamin()


urlpatterns = patterns('')

urlpatterns += publisher_djamin.get_urls()
urlpatterns += author_djamin.get_urls()
urlpatterns += book_djamin.get_urls()