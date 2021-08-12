# _*_ codingL utf-8 _*_

"""
simple chat server 
"""

from __future__ import print_function
# imports
import logging
import socket
import threading
import sys
# logger
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s [%(levelname)s] %(name)s - %(filename)s - %(message)s', 
                    datefmt='%Y-%m-%d %H:%M:%S',
                    stream=sys.stdout)
logger = logging.getLogger('chatBox')

from chatBox.cfg import Config
from chatBox.server.server import Server
from chatBox.client.client import Client

__author__ = 'Matthew Finch'
__maintainer__ = 'Matthew Finch'
__email__ = 'finchrmatthew@gmail.com'