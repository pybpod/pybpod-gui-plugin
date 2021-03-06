# !/usr/bin/python3
# -*- coding: utf-8 -*-

SETTINGS_PRIORITY = 0

import logging

############ LOGGERS SETTINGS ############

# GUI logger
#APP_LOG_HANDLER_FILE_LEVEL = logging.WARNING
#APP_LOG_HANDLER_CONSOLE_LEVEL = logging.WARNING

# Other libraries logger
#APP_LOG_HANDLER_CONSOLE_LEVEL = logging.WARNING
#APP_LOG_HANDLER_FILE_LEVEL = logging.WARNING

############ PYFORMS GENERIC EDITOR SETTINGS ############

GENERIC_EDITOR_WINDOW_GEOMETRY = 100, 100, 1200, 800

GENERIC_EDITOR_TITLE = "PyBpod GUI"

PYFORMS_MAINWINDOW_MARGIN = 0
PYFORMS_STYLESHEET = ''
PYFORMS_STYLESHEET_DARWIN = ''
PYFORMS_SILENT_PLUGINS_FINDER = True

PYFORMS_MATPLOTLIB_ENABLED = True
PYFORMS_WEB_ENABLED = True
PYFORMS_GL_ENABLED = False
PYFORMS_VISVIS_ENABLED = False

############ INSTALLED PLUGINS ############

GENERIC_EDITOR_PLUGINS_PATH = None
GENERIC_EDITOR_PLUGINS_LIST = [
	'pybpodgui_plugin',
	'pybpodgui_plugin_timeline',
	'pybpodgui_plugin_session_history',
	'pge_welcome_plugin',
]

WELCOME_PLUGIN_URL = 'http://pybpod.readthedocs.io'


############ BPODGUI PLUGIN SETTINGS ############

# DEFAULT_PROJECT_PATH = ''

BOARD_LOG_WINDOW_REFRESH_RATE = 0.2 # s
SESSIONLOG_PLUGIN_REFRESH_RATE = 0.2 # s

PYBOARD_COMMUNICATION_THREAD_REFRESH_TIME  = 0.1 # timer for thread look for events (seconds)
PYBOARD_COMMUNICATION_PROCESS_REFRESH_TIME = 0.1 # timer for process look for events (seconds)
PYBOARD_COMMUNICATION_PROCESS_TIME_2_LIVE = 5 # wait before killing process (seconds)
