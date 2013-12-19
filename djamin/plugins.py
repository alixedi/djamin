from django.conf.urls import patterns, url
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy


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

	def get_view_name(self, _class=None):
		if _class is None:
			_class = self.__class__.__name__
		return '%s_%s_%s' % (self.get_app_label().lower(),
							 self.get_model_name().lower(),
							 _class.lower())

	def get_urls(self):
		pass


class List(Plugin):
	"""Implements list"""
	
	def get_config(self):
		"""Overriding to set defaults"""
		defaults = {'template_name': 'djamin/list.html'}
		self.config.update(defaults)
		return self.config

	def listview_factory(self):
		"""Creates list"""
		return type('%s%s' % (self.get_model_name(), 
							  self.__class__.__name__),
					(ListView,),
					self.get_config())

	def get_urls(self):
		"""Returns list urls"""
		return patterns('',
			url(r'^%s/$' % self.get_model_name().lower(),
				self.listview_factory().as_view(),
				name=self.get_view_name()))


class Detail(Plugin):
	"""Implements detail"""
	
	def get_config(self):
		"""Overriding to set defaults"""
		defaults = {'template_name': 'djamin/detail.html'}
		self.config.update(defaults)
		return self.config

	def detailview_factory(self):
		"""Creates detail"""
		return type('%s%s' % (self.get_model_name(), 
							  self.__class__.__name__),
					(DetailView,),
					self.get_config())

	def get_urls(self):
		"""Returns detail urls"""
		return patterns('',
			url(r'^%s/(?P<pk>[a-zA-Z0-9_]+)/$' % self.get_model_name().lower(),
				self.detailview_factory().as_view(),
				name=self.get_view_name()))

class Create(Plugin):
	"""Implements create"""
	
	def get_config(self):
		"""Overriding to set defaults"""
		defaults = {'template_name': 'djamin/create.html',
					'success_url': reverse_lazy(self.get_view_name('List'))}
		self.config.update(defaults)
		return self.config

	def createview_factory(self):
		"""Creates create"""
		return type('%s%s' % (self.get_model_name(), 
							  self.__class__.__name__),
					(CreateView,),
					self.get_config())

	def get_urls(self):
		"""Returns craete urls"""
		return patterns('',
			url(r'^%s/create/$' % self.get_model_name().lower(),
				self.createview_factory().as_view(),
				name=self.get_view_name()))


class Update(Plugin):
	"""Implements update"""
	
	def get_config(self):
		"""Overriding to set defaults"""
		defaults = {'template_name': 'djamin/update.html',
					'success_url': reverse_lazy(self.get_view_name('List'))}
		self.config.update(defaults)
		return self.config

	def updateview_factory(self):
		"""Creates update"""
		return type('%s%s' % (self.get_model_name(), 
							  self.__class__.__name__),
					(UpdateView,),
					self.get_config())

	def get_urls(self):
		"""Returns update urls"""
		return patterns('',
			url(r'^%s/(?P<pk>[a-zA-Z0-9_]+)/update/$' % self.get_model_name().lower(),
				self.updateview_factory().as_view(),
				name=self.get_view_name()))


class Delete(Plugin):
	"""Implements delete"""
	
	def get_config(self):
		"""Overriding to set defaults"""
		defaults = {'template_name': 'djamin/delete.html',
					'success_url': reverse_lazy(self.get_view_name('List'))}
		self.config.update(defaults)
		return self.config

	def deleteview_factory(self):
		"""Creates delete"""
		return type('%s%s' % (self.get_model_name(), 
							  self.__class__.__name__),
					(DeleteView,),
					self.get_config())

	def get_urls(self):
		"""Returns delete urls"""
		return patterns('',
			url(r'^%s/(?P<pk>[a-zA-Z0-9_]+)/delete/$' % self.get_model_name().lower(),
				self.deleteview_factory().as_view(),
				name=self.get_view_name()))
