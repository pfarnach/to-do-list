from prettytable import PrettyTable
import colorama
import time
import todo
from todo import TodoList, TodoItem


class ToDoListApp(object):

   def __init__(self):
      self.task_counter = 0

   
   def show_banner(self):
      """Display the application welcome banner"""
      print "\n\nWelcome to the ToDo list application"


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

      self.task_counter += 1

      entry = TodoItem(task_id = self.task_counter, task_name = task_name, task_type=task_type, task_owner=task_owner, due_date=due_date, due_time=due_time)
      todolist.add_entry(entry.entry_list())

      self.draw_table(todolist.master_list)


   def delete_command(self, todolist):

      requested_id = raw_input(">> Please enter a task ID for the entry you wish to delete: ").strip()

      deleted = todolist.delete_entry(requested_id)

      if not deleted:
         print "\nSorry, no entry with an ID of %s was found.\n" % requested_id
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
      
      # This class manages my todo list
      todolist = TodoList()
      
      # Current command the user entered
      command = ""
      
      # Main command loop - ask for the command and execute it. Quit if user enters 'quit'
      while command != "quit":

         print "\n1. Add a task\n2. Delete a task\n3. Find a task\n4. Mark a task as done\n5. View current tasks\n0. Quit"
         command = raw_input("Choose a number: ").strip()

         if not command:
            continue
   
         #print "Executing", command
         
         if command == '1':
            self.add_command(todolist)

         elif command == '2':
            self.delete_command(todolist)

         elif command == "4":
            self.mark_done_command(todolist)

         elif command == "5":
            self.draw_table(todolist.master_list)

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
      in your todo list. Think about what classes you'll need. How will you model the real world of managing a todo list?

      4. Decide on a standard record format for your to-do items. Think about what kinds of information you want
      to record for a todo item. There should be standard todo item data schema that everyone in class uses 
      (common schema); for extra credit, you could add some additional optional fields.
      
      5. Allow you to create, mark-done, (update), delete and list todo items in for yourself. These should be saved 
      in memory for the duration of the program.
      
      6. When listing todo items, items should be shown sorted by date in descending order. Any Todo items due 
      today should be highlighted.       
      
      6.5 save & load to a local JSON file
            
      6.6 Add the ability to assign and group todo items into 'Projects'
      
      7. Implement a 'save' command that saves your to-do items to your cloud database collection hosted on 
      compose.io (details to come).
      When you store an item to your database collection, the database will generate a unique 'id' for the record. 
      The classes that implement Cloud database save & load should have the same interface as local 
      save & load (polymorphism)
            
      8. By default, a todo item is assigned to you. You should identify yourself as your name & last initial.
          
      9. Allow you to create and 'assign' a todo item to another student by referencing that student as '@studentname'. 
      For example, if I wanted to create a todo item but assign it to a student named 'sally jones', my todo item might 
      contain something like: 
      
      "Do not forget to pick me up after work @sallyj". 
      
      Todo items assigned to someone else get stored to that student's to-do list stored in the cloud not in your own. 
      Next time they 'load' their todo list, they will see all their items and all items assigned to them by other
      users (including information about who assigned it). The item you assigned to them stays in your todo list as 
      a 'delegated' item. You cannot mark such items as 'done'.      
      
      10. If you have any items assigned to you by other people, those items should be preserved when you 'save' 
      to cloud storage.
            
      11. Implement a 'load' command that fetches your to-do list from cloud storage. Items loaded from cloud 
      storage should replace anything currently stored in memory.       
      
      
      12. Use at least some exception handling to handle errors and make the code robust against invalid data. 
      Think about what constitutes invalid data.      
      
      13. For every command that generates output, have an alternate output view as a static HTML file of the 
      displayed data (can be viewed using the file:/// protocol). If you have assigned todo items to another user 
      or have received todo items from another user, display that user's gravatar beside that item.       
      
      14. Support adding small attachments to the todo item      
'''

