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

	def add_entry(self, entry):
		self.master_list.append(entry)

	def delete_entry(self, entry_id):

		self._temp_master_list = []

		for entry in self.master_list:
			if entry_id not in entry:
				self._temp_master_list.append(entry)

		if self.master_list == self._temp_master_list:
			self.change = False
		else:
			self.change = True

		self.master_list = self._temp_master_list

		return self.change

	def mark_done(self, entry_id):

		self.change = False

		for entry in self.master_list:
			if entry_id in entry:
				entry[1] = "Yes"
				self.change = True

		return self.change

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

	def __init__(self, task_id, task_name, task_type, task_owner, due_date = "n/a", due_time = "n/a", done = "No"):
		self._task_name = task_name
		self._task_type = task_type
		self._task_owner = task_owner
		self._due_date = due_date
		self._due_time = due_time
		self._done = done
		self._time_created = str(datetime.datetime.now())[5:-7]
		self._task_id = "%03d" % task_id

	def entry_list(self):
		self.entry_list = [self._task_id, self._done, self._task_name, self._task_type, self._due_date, self._due_time, self._task_owner, self._time_created]
		return self.entry_list





