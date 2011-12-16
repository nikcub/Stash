#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:ts=4:sw=4:expandtab
"""
  stash - cache_tests.py

  A python object persistance and caching module

  This source file is subject to the new BSD license that is bundled with this
  package in the file LICENSE.txt. The license is also available online at the
  URL: <http://nikcub.appspot.com/bsd-license.txt>

  :copyright: Copyright (C) 2011 Nik Cubrilovic and others, see AUTHORS
  :license: new BSD, see LICENSE for more details.
"""

__version__ = '0.0.1'
__author__ = 'Nik Cubrilovic <nikcub@gmail.com>'

import sys
import os
import logging
import unittest

class CacheTests(unittest.TestCase):

  cache_dir = 'cache'

  cache_strings = (
    "TEST",
    "TEST ONE",
    "TEST TWO",
    "TEST THREE",
  )

  cache_dict = {
    "Diffbot": {
      "debug": True,
      "apikey": "0000010000111",
    },
    "debug": False,
    "apikey": "apikey"
  }

  handlers = (
    "FileCacheHandler",
    "GlobalCacheHandler",
    "NullCacheHandler",
    "MemcacheHandler",
    "GAEMemcacheHandler",
  )


  def setup_cache(self, filename):
    conf_file_path = os.path.join(self.config_dir, filename)
    if not os.path.isfile(conf_file_path):
      raise Exception, "Could not load config file: %s" % conf_file_path
    return config.Config(conf_file_path)

  def test_cache_handler_str(self):
    """1. Test that each of the cache handlers returns the right object type"""
    for hnd in self.handlers:
      reth = cache.handler(handler = hnd)
      self.assertIsInstance(reth, hnd())

  def test_cache_handler_obj(self):
    pass

  def test_nonexistant_handler(self):
    """Test that a non-existant handler fails"""
    self.assertRaises(cache.CacheException, cache.handler, 'zzz')

  def test_filehander_non_existant_dir(self):
    """Passing a non-existant file should raise an error"""
    reth = cache.handler(handler = "FileCacheHandler")
    self.assertRaises(cache.CacheException, reth, set_cache_dir, 'zzz')




def init_logger(level, debug = False):
  """Sets the logging level for both the command line client and the
  client library
  """
  if debug:
    log_level = logging.DEBUG
  elif level:
    log_level = level
  else:
    log_level = logging.WARNING

  try:
    return logging.basicConfig(level=log_level)
  except Exception:
    return False

def setup_paths():
  """Setup the path to the stash module so that we can import it and run
  tests against it.
  """
  # This is a weird way of setting up the path, but we do it so that tests
  # can be run prior to the module being installed properly and fully
  db_path = os.path.join(os.path.dirname(__file__), '..')
  sys.path.insert(0, db_path)

if __name__ == '__main__':

  setup_paths()

  try:
    import stash
  except ImportError:
    logging.exception("Can not find the stash module in order to test it. \
                      Please run tests from the ./tests folder, or specify \
                      the path to the stash module by using the --path or -p \
                      command line option.")

  from stash import cache
  unittest.main()
