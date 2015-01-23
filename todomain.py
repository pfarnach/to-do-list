from prettytable import PrettyTable
import colorama
import time
import todo
from todo import TodoList, TodoItem


class ToDoListApp(object):
   
   def show_banner(self):
      """Display the application welcome banner"""
      print "\n\nWelcome to the ToDo list application\n\n"
      
      
   def add_command(self, todolist):
      print "Please enter task information."
      
      entry = TodoItem()
      todolist.master_list.append(entry.add_entry())
      print todolist.master_list

      todolist.draw_table(todolist.master_list)
      
   def command_loop(self):
      """Main command loop for todo list application"""
      
      self.show_banner()
      
      # This class manages my todo list
      todolist = TodoList()
      
      # Current command the user entered
      command = ""

      
      # Main command loop - ask for the command and execute it. Quit if user enters 'quit'
      while command != "quit":

         print "You can type 'add', 'delete', 'find' or 'quit'."
         command = raw_input("What is your command: ").strip().lower()
         if not command:
            continue
            
         if command == "quit":
            break
            
         #print "Executing", command
         
         if command == 'add':
            self.add_command(todolist)
         
            
         else:
            print "Unknown command:", command
         
         
      print "Goodbye"
         


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

