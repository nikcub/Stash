from distutils.core import setup

# TODO add json or simplejson requirement
# simplejson for python < 2.6

setup(
  name = 'stash',
  packages = ['stash'],
  version = '0.0.2',
  description = 'object caching and persistence module for Python applications',
  author = 'Nik Cubrilovic',
  author_email = 'nikcub@gmail.com',
  url = 'http://bitbucket.org/nik/stash',
  download_url = 'https://bitbucket.org/nik/stash/get/tip.zip',
  keywords = ['cache', 'memcached'],
  classifiers = [
    'Programming Language :: Python',
    'Development Status :: 4 - Beta',
    'Environment :: Other Environment',
    'Intended Audience :: Developers',
  ],
  long_description = """\
stash is an object caching and persistence module for Python applications.

Support for Google App Engine, web applications, terminal apps and a number of
cache handlers such as file and directory, memcached, redis, mongodb, etc.

Supports multi-tier collating cache between handlers and is easy to setup and
use. Cache objects by decorating getters and setters, using the mixins provided
or inheriting the core cache object.

Features:

* Simple object caching for all types of Python applications, specifically web
applications
* Support for Google App Engine cache stores (memcache, db, global variable)
* Default handlers are File store, memcache, global var, redis.
* Will auto-detect available cache store options
* Easy to cache objects by decorating methods or inheriting the default storage
types
"""
)