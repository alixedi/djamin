from django.core.exceptions import ImproperlyConfigured
from django.conf.urls import patterns

class ModelDjamin(object):
    """A la ModelAdmin"""

    # This is necessary!
    queryset = None
    # This is optional
    plugins = None

    def __init__(self):
        if self.queryset is None:
            raise ImproperlyConfigured(("Queryset attribute undefined!"))
        if self.plugins is None:
            self.plugins =  {

                    'detail':   {'module':  'djamin',
                                 'class':   'Detail',
                                 'config':  {'queryset': self.queryset}},
                    
                    'list':     {'module':  'djamin',
                                 'class':   'List',
                                 'config':  {'queryset': self.queryset}},
                    
                    'create':   {'module':  'djamin',
                                 'class':   'Create',
                                 'config':  {'queryset': self.queryset}},
                    
                    'update':   {'module':  'djamin',
                                 'class':   'Update',
                                 'config':  {'queryset': self.queryset}},

                    'delete':   {'module':  'djamin',
                                 'class':   'Delete',
                                 'config':  {'queryset': self.queryset}},
                    }

    def load_plugin(self, plugin_name):
        """Loads the given plugin and returns the urls"""
        try:
            plugin = self.plugins[plugin_name]
            module = __import__(plugin['module']+'.plugins')
            library = getattr(module, 'plugins')
            _class = getattr(library, plugin['class'])
        except:
            raise ImproperlyConfigured(("Cannot load plugin."))
        plugin['object'] = _class(plugin['config'])
        return plugin['object'].get_urls()

    def get_urls(self):
        """Returns urls"""
        urls = patterns('')
        for plugin in self.plugins:
            urls += self.load_plugin(plugin)
        return urls