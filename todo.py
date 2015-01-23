from prettytable import PrettyTable
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

	def draw_table(self, master_list):
		self.entry_titles = ['Done', 'Task Name', 'Task Type', 'Task owner', 'Due Date', 'Due Time']
		
		master_table = PrettyTable(self.entry_titles)
		
		for entry in master_list:
			master_table.add_row([master_list[0]['done'],master_list[0]['task name'],master_list[0]['task type'],master_list[0]['task owner'],master_list[0]['due date'],master_list[0]['due time']])
		
		print master_table


class TodoItem(object):
	"""Manage a single ToDo item"""
	def __init__(self):
		pass

	def add_entry(self):

		self.task_name = raw_input("What's the task? ")
	  	self.task_type = raw_input("What's the task type? ")
	  	self.due_date = raw_input("What day is the task due? ")
		self.due_time = raw_input("What time is the task due? ")
		self.owner = raw_input("What's your name? ")

		self.entry = {'done': False, 'task name': self.task_name, 'task type': self.task_type, 'task owner': self.owner, 'due date': self.due_date, 'due time': self.due_time}

		return self.entry



	# def add_entry(self, done = False, task_name, task_type, task_owner = fullname, due_date, due_time = "23:59:59"):
	# 	self.new_entry = 




