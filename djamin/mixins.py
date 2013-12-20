class PluginMixin(object):
	"""Holds some comon utility functions"""

	def get_model_name(self):
		"""Returns model name"""
		return self.config['queryset'].model._meta.object_name

	def get_app_label(self):
		"""Get app label"""
		return self.config['queryset'].model._meta.app_label


class ConfigMixin(object):
	"""Defines the default confog policy"""

	def get_config(self):
		"""Override to change default config policy"""
		defaults = {'template_name': self.get_template_name()}
		defaults.update(self.config)
		return defaults


class ViewFactoryMixin(object):
	"""Defines the default factory for views"""

	def get_view_class(self, _class=None):
		"""Returns appropriate view class"""
		_class = _class or self.__class__.__name__
		module = __import__('django.views.generic')
		views = getattr(module, 'views')
		generic = getattr(views, 'generic')
		return (getattr(generic, '%sView' % _class),)

	def view_factory(self, _class=None):
		"""Override to change default view factory"""
		_class = _class or self.__class__.__name__
		return type('%s%s' % (self.get_model_name(), _class),
					self.get_view_class(_class), 
					self.get_config())


class TemplateNameMixin(object):
	"""Defines the policy in force for naming default templates"""

	def get_template_name(self, _class=None):
		"""Override this to change default template name policy"""
		_class = _class or self.__class__.__name__
		return 'djamin/%s.html' % _class.lower()


class ViewNameMixin(object):
	"""Defines the policy in force for naming view in urls"""	

	def get_view_name(self, _class=None):
		"""Override this to change view naming policy"""
		_class = _class or self.__class__.__name__
		return '%s_%s_%s' % (self.get_app_label().lower(),
							 self.get_model_name().lower(),
							 _class.lower())


class PermissionNameMixin(object):
	"""Defined the policy in force for naming permissions"""

	def get_permission_name(self, perm_type):
		"""Override this to change permission naming policy"""
		return '%s.%s_%s' % (self.get_app_label().lower(),
							 perm_type,
							 self.get_model_name())
