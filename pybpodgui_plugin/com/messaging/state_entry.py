# !/usr/bin/python3
# -*- coding: utf-8 -*-

from pyforms_generic_editor.com.messaging.board_message import BoardMessage


class StateEntry(BoardMessage):
	""" Message from board that represents a state entry"""

	MESSAGE_TYPE_ALIAS = 'state_entry'

	def __init__(self, state_name, state_timestamp, state_id):
		"""

		:param state_name:
		:param state_timestamp:
		:param state_id:
		"""

		self.state_id = state_id
		self.state_name = state_name

		BoardMessage.__init__(self, board_timestamp=state_timestamp,
		                      content="{0}: {1}".format(state_name, state_timestamp))

	@property
	def state_name(self):
		""" State name """
		return self._state_name

	@state_name.setter
	def state_name(self, value):
		"""
		state name setter
		:param value: state name
		:type value: string
		"""
		self._state_name = value

	@property
	def state_id(self):
		""" State id """
		return self._state_id

	@state_id.setter
	def state_id(self, value):
		"""
		state id setter
		:param value: state id
		:type value: string
		"""
		self._state_id = value
