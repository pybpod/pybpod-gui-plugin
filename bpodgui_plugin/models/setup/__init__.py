# !/usr/bin/python3
# -*- coding: utf-8 -*-

from pysettings import conf

from bpodgui_plugin.models.setup.setup_uibusy import SetupUIBusy

Setup = type(
	'Setup',
	tuple(conf.GENERIC_EDITOR_PACKAGES_FINDER.find_class('models.setup.Setup') + [SetupUIBusy]),
	{}
)