from django.conf.urls import patterns, url
from django.views.generic import ListView

class Plugin(object):
	"""Abstract class for plugin"""
	
	def __init__(self, config):
		"""Set config"""
		self.config = config
	
	def get_config(self):
		"""Override to set defaults"""
		return self.config

	def get_model_name(self):
		"""Returns model name"""
		return self.config['queryset'].model._meta.object_name

	def get_app_label(self):
		"""Get app label"""
		return self.config['queryset'].model._meta.app_label

	def get_view_name(self):
		_class = self.__class__.__name__
		return '%s_%s_%s' % (self.get_app_label().lower(),
							 self.get_model_name().lower(),
							 _class.lower())

	def get_urls(self):
		pass


class Listview(Plugin):
	"""Implements list view"""
	
	def get_config(self):
		"""Overriding to set defaults"""
		defaults = {'template_name': 'djamin/listview.html'}
		self.config.update(defaults)
		return self.config

	def listview_factory(self):
		"""Creates list view"""
		return type('%s%s' % (self.get_model_name(), 
							  self.__class__.__name__),
					(ListView,),
					self.get_config())

	def get_urls(self):
		"""Returns list view urls"""
		return patterns('',
			url(r'^%s/$' % self.get_model_name().lower(),
				self.listview_factory().as_view(),
				name=self.get_view_name()))
