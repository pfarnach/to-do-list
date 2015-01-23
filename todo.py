from prettytable import PrettyTable
import datetime
'''
This module implements the classes for the ToDo list application
'''

class TodoListStorage(object):
	"""Used by TodoList, this class takes care or saving a loading todo lists"""
	pass

class TodoList(object):
	"""Manage a list of ToDo items"""
	def __init__(self):
		self.master_list = []


class TodoItem(object):
	"""Manage a single ToDo item"""

	# text - the task
	# date - when the task was made
	# duedate - date task is due
	# who - whose task
	# status - done y/n?
	# 
	# Behaviors:
	# constructor - create a todo item
	# change status - set the status
	# get data
	# 

	def __init__(self, task_name, task_type, task_owner, due_date = "n/a", due_time = "n/a", done = "No"):
		self._task_name = task_name
		self._task_type = task_type
		self._task_owner = task_owner
		self._due_date = due_date
		self._due_time = due_time
		self._done = done

		self._time_now = datetime.datetime.now()
		self._date_created = datetime.datetime.now()
		self._time_created = str(self._time_now.hour) + ":" + str(self._time_now.minute) + ":" + str(self._time_now.second)
		# self._time_left = ??

	def entry_list(self):
		self.entry_list = [self._done, self._task_name, self._task_type, self._task_type, self._due_date, self._due_time, self._date_created, self._time_created]
		return self.entry_list

	# def add_entry(self, done = False, task_name, task_type, task_owner = fullname, due_date, due_time = "23:59:59"):
	# 	self.new_entry = 




