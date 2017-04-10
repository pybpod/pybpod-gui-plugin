# # !/usr/bin/python3
# # -*- coding: utf-8 -*-

import logging

SETTINGS_PRIORITY = 100

# THESE SETTINGS ARE NEEDED FOR PYSETTINGS
APP_LOG_FILENAME = 'app.log'
APP_LOG_HANDLER_CONSOLE_LEVEL = logging.DEBUG
APP_LOG_HANDLER_FILE_LEVEL = logging.DEBUG
PYFORMS_USE_QT5 = True


# BPOD GUI PLUGIN SETTINGS

BPODGUI_LOG_HANDLER_FILE_LEVEL = logging.DEBUG
BPODGUI_LOG_HANDLER_CONSOLE_LEVEL = logging.INFO

CONTROL_EVENTS_GRAPH_DEFAULT_SCALE = 100
BOARD_LOG_WINDOW_REFRESH_RATE = 1000

USE_MULTIPROCESSING = True
