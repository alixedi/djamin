from django.conf.urls import patterns, url

from .mixins import PluginMixin, ConfigMixin, ViewFactoryMixin, \
					TemplateNameMixin, ViewNameMixin, PermissionNameMixin


class Plugin(PluginMixin,
			 ConfigMixin,
			 ViewFactoryMixin,
			 TemplateNameMixin,
			 ViewNameMixin,
			 PermissionNameMixin):
	"""Abstract class for plugin"""
	
	def __init__(self, config):
		"""Set config"""
		self.config = config		

	def get_urls(self):
		"""Let subclasses implement this"""
		pass


class List(Plugin):
	"""Implements list"""
	
	def get_urls(self):
		"""Returns list urls"""
		return patterns('',
			url(r'^%s/$' % self.get_model_name().lower(),
				self.view_factory().as_view(),
				name=self.get_view_name()))


class Detail(Plugin):
	"""Implements detail"""
	
	def get_urls(self):
		"""Returns detail urls"""
		return patterns('',
			url(r'^%s/(?P<pk>[a-zA-Z0-9_]+)/$' % self.get_model_name().lower(),
				self.view_factory().as_view(),
				name=self.get_view_name()))

class Create(Plugin):
	"""Implements create"""
	
	def get_urls(self):
		"""Returns craete urls"""
		return patterns('',
			url(r'^%s/create/$' % self.get_model_name().lower(),
				self.view_factory().as_view(),
				name=self.get_view_name()))


class Update(Plugin):
	"""Implements update"""
	
	def get_urls(self):
		"""Returns update urls"""
		return patterns('',
			url(r'^%s/(?P<pk>[a-zA-Z0-9_]+)/update/$' % self.get_model_name().lower(),
				self.view_factory().as_view(),
				name=self.get_view_name()))


class Delete(Plugin):
	"""Implements delete"""
	
	def get_urls(self):
		"""Returns delete urls"""
		return patterns('',
			url(r'^%s/(?P<pk>[a-zA-Z0-9_]+)/delete/$' % self.get_model_name().lower(),
				self.view_factory().as_view(),
				name=self.get_view_name()))
