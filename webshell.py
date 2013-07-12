#-*- coding:utf-8 -*-

import os, sys

curr_path = os.path.dirname(os.path.abspath(__file__)) + os.sep
sys.path.append(curr_path + 'bottle')

from bottle import *

WEBSHELL_PATH = '/'
WEBSHELL_NAME = 'ws'
WEBSHELL_INDEX_NAME = 'frames.html'

WEBSHELL_COMMAND_PATH = WEBSHELL_PATH + 'actions/'
WEBSHELL_COMMAND_VIEWFILE = 'viewfile'

@route(WEBSHELL_PATH + WEBSHELL_NAME)
def webshell():
	return static_file(WEBSHELL_INDEX_NAME, root=curr_path + 'webshell_static')

@route(WEBSHELL_COMMAND_PATH + WEBSHELL_COMMAND_VIEWFILE)
def viewfile():
	filename = request.query.get('file').strip()
	if (filename == None) or (filename == ""):
		return "Please enter a file name to view."
	try:
		return open(filename.decode("utf-8"), 'r')
	except:
		return "Error. Please check your input."

@route(WEBSHELL_PATH + '<filename:path>')
def webshell_res(filename=WEBSHELL_INDEX_NAME):
	return static_file(filename, root=curr_path + 'webshell_static')

run(host='localhost', port=8080)

