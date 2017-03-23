# !/usr/bin/python3
# -*- coding: utf-8 -*-

import os

# see pyforms_generic_editor.resources.__init__ for generic icons

def path(filename):
	return os.path.join(os.path.dirname(__file__), 'icons', filename)

BOARDS_SMALL_ICON = path('boxes.png')
BOX_SMALL_ICON = path('box.png')

SUBJECT_SMALL_ICON = path('subject.png')
UPLOAD_SMALL_ICON = path('upload.png')

EXPERIMENT_SMALL_ICON = path('experiment.png')
EXPERIMENTS_SMALL_ICON = path('experiments.png')

TASK_SMALL_ICON = path('task.png')
TASKS_SMALL_ICON = path('tasks.png')
