# !/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import logging

from pyforms import conf

import pyforms as app
from pyforms import BaseWidget
from pyforms.controls import ControlText
from pyforms.controls import ControlButton
from pyforms.controls import ControlCheckBoxList
from pyforms.controls import ControlNumber

from pybpodgui_api.models.board import Board


from pybpodapi.bpod.bpod_com_protocol_modules import BpodCOMProtocolModules as Bpod

logger = logging.getLogger(__name__)


class BoardWindow(Board, BaseWidget):
	"""
	Define here which fields from the board model should appear on the details section.

	The model fields shall be defined as UI components like text fields, buttons, combo boxes, etc.

	You may also assign actions to these components.

	**Properties**

		name
			:class:`string`

			Name associated with this board. Returns the current value stored in the :py:attr:`_name` text field.

		serial_port
			:class:`string`

			Serial port associated with this board. Returns the current value stored in the :py:attr:`_serial_port` text field.


	**Private attributes**

		_name
			:class:`pyforms.controls.ControlText`

			Text field to edit board name. Editing this field fires the event :meth:`BoardWindow._BoardWindow__name_changed_evt`.

		_serial_port
			:class:`pyforms.controls.ControlText`

			Text field to edit serial port. Editing this field fires the event :meth:`BoardWindow._BoardWindow__serial_changed_evt`.

		_log_btn
			:class:`pyforms.controls.ControlButton`

			Button to show this board events on a console window. Pressing the button fires the event :class:`BoardDockWindow.open_log_window`.

		_formset
			Describe window fields organization to PyForms.

	**Methods**

	"""

	def __init__(self, project=None):
		"""

		:param project: project where this board belongs
		:type project: pycontrolgui.models.project.Project
		"""
		BaseWidget.__init__(self, 'Board')
		self.layout().setContentsMargins(5,10,5,5)

		self._name 				= ControlText('Box name')
		self._serial_port 		= ControlText('Serial port')
		self._log_btn 			= ControlButton('Console')
		self._active_bnc 		= ControlCheckBoxList('BNC')
		self._active_wired 		= ControlCheckBoxList('Wired')
		self._active_behavior 	= ControlCheckBoxList('Behavior')
		self._loadports_btn 	= ControlButton('Load ports')
		self._netport    		= ControlNumber('Net port', default=36000+len(project.boards), minimum=36000, maximum=36100)
        

		Board.__init__(self, project)

		self._formset = [
			'_name',
			('_serial_port','_log_btn'),
			'_netport',
			' ',
			('Enabled or disable ports',' ','_loadports_btn'),			
			'_active_bnc',
			'_active_wired',
			'_active_behavior'
		]

		self._name.changed_event 		= self.__name_changed_evt
		self._serial_port.changed_event = self.__serial_changed_evt
		self._loadports_btn.value 		= self.__load_bpod_ports

	def __load_bpod_ports(self):

		try:
			bpod = Bpod(self._serial_port.value)
			bpod.start()
			hw = bpod.hardware

			### load the ports to the GUI ###############################
			self._active_bnc.value 		= [ ('BNC{0}'.format(j+1),  True) for j, i in enumerate(hw.bnc_inputports_indexes) 	]
			self._active_wired.value 	= [ ('Wire{0}'.format(j+1), True) for j, i in enumerate(hw.wired_inputports_indexes) 	]
			self._active_behavior.value = [ ('Port{0}'.format(j+1), True) for j, i in enumerate(hw.behavior_inputports_indexes)]
			#############################################################
			
			bpod.stop()
		except Exception as e:
			self.critical(str(e), 'Error loading ports')

	def __name_changed_evt(self):
		"""
		React to changes on text field :py:attr:`_name`.

		This methods is called every time the user changes the field.
		"""
		if not hasattr(self, '_update_name') or not self._update_name:
			self.name = self._name.value

	def __serial_changed_evt(self):
		"""
		React to changes on text field :py:attr:`_serial_port`.

		This methods is called every time the user changes the field.
		"""

		if not hasattr(self, '_update_serial') or not self._update_serial:
			self.serial_port = self._update_serial.value

	@property
	def name(self):
		return self._name.value

	@name.setter
	def name(self, value):
		self._update_name = True  # Flag to avoid recursive calls when editing the name text field
		self._name.value = value
		self._update_name = False

	@property
	def serial_port(self):
		return self._serial_port.value

	@serial_port.setter
	def serial_port(self, value):
		self._update_serial = True  # Flag to avoid recursive calls when editing the name text field
		self._serial_port.value = value
		self._update__serial = False


	@property
	def enabled_bncports(self):				return [b for v,b in self._active_bnc.items] if self._active_bnc.count>0 else None
	@enabled_bncports.setter
	def enabled_bncports(self, value): 
		Board.enabled_bncports.fset(self, value)
		if value is None:
			self._active_bnc.value = []
		else:
			self._active_bnc.value = [ ('BNC{0}'.format(j+1), v) for j, v in enumerate(value)]
		

	@property
	def enabled_wiredports(self):			return [b for v,b in self._active_wired.items] if self._active_wired.count>0 else None
	@enabled_wiredports.setter
	def enabled_wiredports(self, value):
		Board.enabled_wiredports.fset(self, value)

		if value is None:
			self._active_wired.value = []
		else:
			self._active_wired.value = [ ('Wire{0}'.format(j+1), v) for j, v in enumerate(value)]
		

	@property
	def enabled_behaviorports(self):		return [b for v,b in self._active_behavior.items] if self._active_behavior.count>0 else None
	@enabled_behaviorports.setter
	def enabled_behaviorports(self, value):
		Board.enabled_behaviorports.fset(self, value)
		if value is None:
			self._active_behavior.value = []
		else:
			self._active_behavior.value = [ ('Port{0}'.format(j+1), v) for j, v in enumerate(value)]



# Execute the application
if __name__ == "__main__":
	app.start_app(BoardWindow)
