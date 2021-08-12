# _*_ codingL utf-8 _*_

"""
simple chat server 
"""

from __future__ import print_function
# imports
import logging
import sys
# logger
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s [%(levelname)s] %(name)s - %(filename)s - %(message)s', 
                    datefmt='%Y-%m-%d %H:%M:%S',
                    stream=sys.stdout)
logger = logging.getLogger('chatBox')

from cfg import Config

__author__ = 'Matthew Finch'
__maintainer__ = 'Matthew Finch'
__email__ = 'finchrmatthew@gmail.com'