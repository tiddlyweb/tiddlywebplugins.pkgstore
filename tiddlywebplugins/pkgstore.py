"""
Use package resources of a package as a place to store
tiddlers etc.
"""

try:    
        from pkg_resources import resource_filename
except ImportError:
        from tiddlywebplugins.utils import resource_filename

from tiddlyweb.store import StoreMethodNotImplemented
from tiddlyweb.stores.text import Store as TextStore

class Store(TextStore):
    """
    A store which keeps entities inside a package.
    """

    def __init__(self, store_config=None, environ=None):
        package = store_config['package']
        self.read_only = store_config.get('read_only', True)
        store_root_base = resource_filename(package, 'resources')
        store_config['store_root'] = '%s/store' % store_root_base
        super(Store, self).__init__(store_config, environ)

    def _init_store(self):
        if self.read_only:
            return
        super(Store, self)._init_store()

    def recipe_put(self, recipe):
        if self.read_only:
            raise StoreMethodNotImplemented('store is read only')
        super(Store, self).recipe_put(recipe)

    def bag_put(self, bag):
        if self.read_only:
            raise StoreMethodNotImplemented('store is read only')
        super(Store, self).bag_put(bag)

    def tiddler_put(self, tiddler):
        if self.read_only:
            raise StoreMethodNotImplemented('store is read only')
        super(Store, self).tiddler_put(tiddler)

    def user_put(self, user):
        raise StoreMethodNotImplemented('store does not handle users')

    def user_get(self, user):
        raise StoreMethodNotImplemented('store does not handle users')


def init(config):
    pass