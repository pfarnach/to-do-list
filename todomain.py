from prettytable import PrettyTable
import time
import todo
from todo import TodoList, TodoItem, TodoListStorage


class ToDoListApp(object):

   def __init__(self):
      self._task_counter = 0

   
   def show_banner(self):
      """Display the application welcome banner"""
      print "\n\nWelcome to the ToDo list application"

   # checks for empty string -- if empty, will make it "n/a"
   def check_empty(self, input_string):
      if len(input_string) == 0:
         return 'n/a'
      else:
         return input_string
      
      
   def add_command(self, todolist):

      print "Please enter task information."

      task_name = self.check_empty(raw_input(">> What's the task? ").strip().capitalize())
      task_type = self.check_empty(raw_input(">> What's the type of task? (e.g. home/work/school) ").strip().capitalize())
      due_date = self.check_empty(raw_input(">> What day is the task due? ").strip().capitalize())
      due_time = self.check_empty(raw_input(">> What time is the task due? ").strip().capitalize())
      task_owner = self.check_empty(raw_input(">> Whose task is this? ").strip().capitalize())

      self._task_counter += 1

      entry = TodoItem(task_id = self._task_counter, task_name = task_name, task_type=task_type, task_owner=task_owner, due_date=due_date, due_time=due_time)
      todolist.add_entry(entry.entry_list())

      self.draw_table(todolist.master_list)


   def delete_command(self, todolist):

      requested_id = raw_input(">> Please enter a task ID for the entry you wish to delete: ").strip()

      deleted = todolist.delete_entry(requested_id)

      if not deleted:
         print "\n* Sorry, no entry with an ID of %s was found." % requested_id
      else:
         self.draw_table(todolist.master_list)


   def mark_done_command(self, todolist):

      requested_id = raw_input(">> Please enter a task ID for the entry you wish to mark as done: ").strip()

      marked_done = todolist.mark_done(requested_id)

      if not marked_done:
         print "\nSorry, no entry with an ID of %s was found.\n" % requested_id
      else:
         print "\nEntry marked as done."
         while True:
            delete_entry = raw_input(">> Would you like to delete it from your list? \n").strip().lower()
            if delete_entry == "yes" or delete_entry == "y":
               deleted = todolist.delete_entry(requested_id)
               break
            elif delete_entry == "no" or delete_entry == "n":
               break
            else:
               print "Sorry, that was a yes or no question."


         self.draw_table(todolist.master_list)


   def update_command(self, todolist):

      requested_id = raw_input(">> Please enter a task ID for the entry you wish to update: ").strip()
      
      try:
         print "What field would you like to update:\n1. Done?\n2. Task name\n3. Task type\n4. Due date\n5. Due time\n6. Task owner"
         requested_field = int(raw_input("\n>> Please enter the number of field you'd like to update: ").strip())
         requested_change = self.check_empty(raw_input("\n>> Please enter the new value: ").strip())
         print

         updated = todolist.update(requested_id,requested_field, requested_change)

         if updated:
            print "Entry was successfully updated.\n"
         else:
            print "* The entry you want to update does not exist.\n"

      except:
         print "* You either did not enter a valid value for the field or you did not choose a valid field."


   def save_command(self,todolist, todoliststorage):

      todoliststorage.save_json(todolist.master_list)

      print "File saved.\n"


   def draw_table(self, master_list):

      # Provides table titles for prettytable
      col_titles = ['ID', 'Done', 'Task Name', 'Task Type', 'Due Date', 'Due Time', 'Task owner', 'Created on']
      
      # Puts table titles into table and aligns the first element to the left
      master_table = PrettyTable(col_titles)
      master_table.align['ID'] = 'l'

      # goes through and places each entry into a new row and prints
      for entry in master_list:
         master_table.add_row(entry)
      
      print master_table
      

   def command_loop(self):
      """Main command loop for todo list application"""
      
      self.show_banner()
      
      # This class manages my to-do list
      todolist = TodoList()
      
      # This class manages the external storage of my to-do list
      todoliststorage = TodoListStorage()

      # Current command the user entered
      command = ""
      
      # Main command loop - ask for the command and execute it. Quit if user enters 'quit'
      while command != "quit":

         print "\n1. Add a task\n2. Delete a task\n3. Update a task\n4. Mark a task as done\n5. View current tasks\n6. Arrange to-do list by field\n7. Save tasks to JSON file\n0. Quit"
         command = raw_input("Choose a number: ").strip()
         print

         if not command:
            continue
   

         
         if command == '1':
            self.add_command(todolist)

         elif command == '2':
            self.delete_command(todolist)

         elif command == '3':
            self.update_command(todolist)

         elif command == "4":
            self.mark_done_command(todolist)

         elif command == "5":
            self.draw_table(todolist.master_list)

         elif command == "6":
            self.arrange_command(todolist)

         elif command == "7":
            self.save_command(todolist, todoliststorage)

         elif command == "0":
            break
            
         else:
            print "Unknown command:", command
         
         
      print "Goodbye\n"
         


# Bootstrap the application
tdlist = ToDoListApp()
tdlist.command_loop()



'''
- A Todo list app:

   - Lots of optional stuff ~ if you can, do more. A project you can go deep on. There will be hints & help. 
   It will be evaluated on how good you do it (not how far you get). Help me generate progress reports. 
   It's something you can build apon - progressive enhancement. 
   
   If you wish, you can work with another person and pair program this project.
   
   - Create a command processor style application that allows you to manage a to-do list.

   - The application:
   
      1. Must be written in an object-oriented style.
      
      1.5 Store everything in git. Create a new subdirectory in your repo. Push daily to github.
      
      2. Must be written using PEP8 standards for naming, doc strings and plenty of comments explaining 
      how you implemented your code

      3. Use at least 2 Python modules. One (tdmain.py) should be the main program that runs the command loop. The other
      module (todo.py) should contain your Python classes that implement all the objects & methods you'll use to manage
      in your to-do list. Think about what classes you'll need. How will you model the real world of managing a to-do list?

      4. Decide on a standard record format for your to-do items. Think about what kinds of information you want
      to record for a to-do item. There should be standard to-do item data schema that everyone in class uses 
      (common schema); for extra credit, you could add some additional optional fields.
      
      5. Allow you to create, mark-done, (update), delete and list to-do items in for yourself. These should be saved 
      in memory for the duration of the program.
      
      6. When listing to-do items, items should be shown sorted by date in descending order. Any to-do items due 
      today should be highlighted.       
      
      6.5 save & load to a local JSON file
            
      6.6 Add the ability to assign and group to-do items into 'Projects'
      
      7. Implement a 'save' command that saves your to-do items to your cloud database collection hosted on 
      compose.io (details to come).
      When you store an item to your database collection, the database will generate a unique 'id' for the record. 
      The classes that implement Cloud database save & load should have the same interface as local 
      save & load (polymorphism)
            
      8. By default, a to-do item is assigned to you. You should identify yourself as your name & last initial.
          
      9. Allow you to create and 'assign' a to-do item to another student by referencing that student as '@studentname'. 
      For example, if I wanted to create a to-do item but assign it to a student named 'sally jones', my to-do item might 
      contain something like: 
      
      "Do not forget to pick me up after work @sallyj".  
      
      Note: I want to be able to specify who should complete the to-do item inside the body of the to-do item
      text by embedding their @username. I shouldn't have to be prompted for it.
      
      to-do items assigned to someone else get stored to that student's to-do list stored in the cloud not in your own. 
      Next time they 'load' their to-do list, they will see all their items and all items assigned to them by other
      users (including information about who assigned it). The item you assigned to them stays in your to-do list as 
      a 'delegated' item. You cannot mark such items as 'done'.      
      
      10. If you have any items assigned to you by other people, those items should be preserved when you 'save' 
      to cloud storage.
            
      11. Implement a 'load' command that fetches your to-do list from cloud storage. Items loaded from cloud 
      storage should replace anything currently stored in memory.       
      
      12. Use at least some exception handling to handle errors and make the code robust against invalid data. 
      Think about what constitutes invalid data.      
      
      13. For every command that generates output, have an alternate output view as a static HTML file of the 
      displayed data (can be viewed using the file:/// protocol). If you have assigned to-do items to another user 
      or have received to-do items from another user, display that user's gravatar beside that item.      
      If you don't want to write static HTML output, use one of the Python GUI libraries (such as tkinter or 
      wxpython) and build a desktop GUI for it.
      
      14. Support adding small attachments to the to-do item      
      
      15. Be able to load the test data I'll provide
'''