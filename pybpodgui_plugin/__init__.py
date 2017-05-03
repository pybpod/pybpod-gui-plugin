# !/usr/bin/python3
# -*- coding: utf-8 -*-

__version__ = "1.3.4.beta"
__author__ = "Carlos Mao de Ferro"
__credits__ = ["Carlos Mao de Ferro", "Ricardo Ribeiro"]
__license__ = "Copyright (C) 2007 Free Software Foundation, Inc. <http://fsf.org/>"
__maintainer__ = ["Carlos Mao de Ferro", "Ricardo Ribeiro"]
__email__ = ["cajomferro@gmail.com", "ricardojvr@gmail.com"]
__status__ = "Development"

import logging
import loggingbootstrap

from pysettings import conf

conf += 'pybpodgui_plugin.settings'
conf += 'pybpodgui_plugin.resources'

# setup different loggers but output to single file
loggingbootstrap.create_double_logger("pybpodgui_plugin", conf.BPODGUI_LOG_HANDLER_CONSOLE_LEVEL,
                                      conf.APP_LOG_FILENAME,
                                      conf.BPODGUI_LOG_HANDLER_FILE_LEVEL)

loggingbootstrap.create_double_logger("pybranch", conf.APP_LOG_HANDLER_CONSOLE_LEVEL,
                                      conf.APP_LOG_FILENAME,
                                      conf.APP_LOG_HANDLER_FILE_LEVEL)

if conf.USE_MULTIPROCESSING:
	# https://docs.python.org/3.5/library/multiprocessing.html#multiprocessing.freeze_support
	from multiprocessing import freeze_support  # @UnresolvedImport

if conf.USE_MULTIPROCESSING:
	freeze_support()
