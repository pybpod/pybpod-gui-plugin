# !/usr/bin/python3
# -*- coding: utf-8 -*-

import logging
import datetime

from pyforms import BaseWidget
from pyforms.Controls import ControlText

from bpodgui_plugin.api.models.session import Session

logger = logging.getLogger(__name__)


class SessionWindow(Session, BaseWidget):
	""" ProjectWindow represents the project entity as a GUI window"""

	def __init__(self, setup=None):
		BaseWidget.__init__(self, 'Session')
		self.layout().setContentsMargins(5,10,5,5)

		self._name = ControlText('Session name')
		self._path = ControlText('File path')
		self._setup_name = ControlText('Subject name')
		self._board_name = ControlText('Board name')
		self._task_name = ControlText('Task name')
		self._board_serial_port = ControlText('Serial port')
		self._started = ControlText('Started on')
		self._ended = ControlText('Ended on')

		Session.__init__(self, setup)

		self._formset = [
			'_name',
			('_started', '_ended'),
			('_setup_name', '_task_name'),
			'_board_name',
			'_board_serial_port',
			'_path',
			' '
		]

		self._path.enabled = self._setup_name.enabled = self._board_name.enabled = self._task_name.enabled = False
		self._board_serial_port.enabled = self._started.enabled = self._ended.enabled = False
		self._name.changed_event = self.__name_edited_evt

	def __name_edited_evt(self):
		if not hasattr(self, '_update_name') or not self._update_name:
			self.name = self._name.value

	def load(self, session_path, data):
		Session.load(self, session_path, data)

	def remove(self): self.setup -= self

	##########################################################################
	####### PROPERTIES #######################################################
	##########################################################################

	@property
	def name(self):
		return self._name.value

	@name.setter
	def name(self, value):
		self._update_name = True  # Flag to avoid recurse calls when editing the name text field
		self._name.value = value
		self._update_name = False
		self.title = "{0}: {1}".format(self.setup.name, value)

	@property
	def path(self):
		return self._path.value

	@path.setter
	def path(self, value):
		self._path.value = value

	@property
	def setup_name(self):
		return self._setup_name.value

	@setup_name.setter
	def setup_name(self, value):
		self._setup_name.value = value

	@property
	def board_name(self):
		return self._board_name.value

	@board_name.setter
	def board_name(self, value):
		self._board_name.value = value

	@property
	def task_name(self):
		return self._task_name.value

	@task_name.setter
	def task_name(self, value):
		self._task_name.value = value

	@property
	def board_serial_port(self):
		return self._board_serial_port.value

	@board_serial_port.setter
	def board_serial_port(self, value):
		self._board_serial_port.value = value

	@property
	def started(self):
		return datetime.datetime.strptime(self._started.value, '%Y/%m/%d %H:%M:%S') if len(
			self._started.value) > 0 else None

	@started.setter
	def started(self, value):
		self._started.value = value.strftime('%Y/%m/%d %H:%M:%S') if value else None

	@property
	def ended(self):
		return datetime.datetime.strptime(self._ended.value, '%Y/%m/%d %H:%M:%S') if len(
			self._ended.value) > 0 else None

	@ended.setter
	def ended(self, value):
		self._ended.value = value.strftime('%Y/%m/%d %H:%M:%S') if value else None
