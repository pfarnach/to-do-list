from prettytable import PrettyTable
import datetime, json
'''
This module implements the classes for the ToDo list application
'''

class TodoListStorage(object):
	"""Used by TodoList, this class takes care or saving a loading todo lists"""
	def __init__(self):
		pass

	def save_json(self, todolist):

		self._save_json = []

		for index, entry in enumerate(todolist):
			self._save_json.append([index]) 
			self._save_json[index]= {}
			self._save_json[index]['ID'] = entry[0]
			self._save_json[index]['done'] = entry[1]
			self._save_json[index]['task_name'] = entry[2]
			self._save_json[index]['task_type'] = entry[3]
			self._save_json[index]['due_date'] = entry[4]
			self._save_json[index]['due_time'] = entry[5]
			self._save_json[index]['task_owner'] = entry[6]
			self._save_json[index]['created_on'] = entry[7]

		with open('jsonfile.txt', 'w') as outfile:
			json.dump(self._save_json, outfile, indent=4)


	def load_json(self):
		f = json.loads(open('jsonfile.txt').read())
		# print f[0]['task_type']

		self.loaded_list = []

		for index, entry in enumerate(f):
			self.loaded_list.append([])
			self.loaded_list[index].append(entry['ID'])
			self.loaded_list[index].append(entry['done'])
			self.loaded_list[index].append(entry['task_name'])
			self.loaded_list[index].append(entry['task_type'])
			self.loaded_list[index].append(entry['due_date'])
			self.loaded_list[index].append(entry['due_time'])
			self.loaded_list[index].append(entry['task_owner'])
			self.loaded_list[index].append(entry['created_on'])

		return self.loaded_list


class TodoList(object):
	"""Manage a list of ToDo items"""
	def __init__(self):
		# makes an empty list to start off with. All entries will work off of this list
		self.master_list = []

	def add_entry(self, entry):
		# self.master_list.append(entry)  // old version

		# prepends entry to master list so it's ordered by 'created on' by default
		self.master_list.insert(0, entry)

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

	def update(self, entry_id, entry_field, entry_change):

		self.change = False

		for entry in self.master_list:
			if entry_id in entry:
				try:
					entry[entry_field] = entry_change
					self.change = True
				except:
					self.change = False

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





