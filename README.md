
# DataQuest

DataQuest is a project made for Phase 3 of FlatIron's coding bootcamp. It emulates an Admin CLI for a fictional MMO called "DataQuest". The project was coded in Python and SQL. 

# CLI Script

From the root terminal, activate the CLI with the command 'python lib/cli.py'. 

The menu will open by informing you that admin access has been granted. 

From here, you can choose to either work with either the User Account menu or the Server menu (or quit the application).

You may notice that in the spirit of a good roguelike, DataQuest punishes the user harshly for providing invalid inputs. Expect to see a GAME OVER screen if you aren't careful...

## User Account Menu 

The User Account Menu has a number of options available: 

1) Create User Account

The script executes the create_user() helper function.

Choosing this option will prompt you to create both a username and a password. Both must be longer than 6 characters in order to pass. The menu will automatically assign the account to a default server upon creation. The new account will persist in the 'users' table within the dataquest db. You will automatically return to the User Menu upon completion. 

2) Delete User Account 

The script executes the delete_user() helper function. 

The menu will provide you with a list of users. Select the ID of the user you would like to delete. The deleted account will be removed from the dataquest db. You will automatically return to the User Menu upon completion. 

3) Lookup User by ID 

The script executes the lookup_user() helper function. 

The menu will ask for an ID# and, if the input is valid, return a corresponding user object. You will automatically return to the User Menu upon completion. 

4) Lookup Users Server

The script executes the lookup_user_server() helper function.

The menu will provide a list of users. Select the ID of the user you would like to learn about. If a valid selection is made, the menu will return the corresponding server of the user. 

5) List All Users

The script executes the all_users() helper function. 

The menu will provide a list of all users currently in the DataQuest db. 

6) Return to Main Menu

The script executes the main_menu() function, returning you to the main menu. 

## Server Menu 

The Server Menu has the following options: 

1) Create Server

The script executes the create_server() helper function.

You will be prompted to create a server name and provide the max player count for the server. The server name must be greater than 5 characters in length. The player count must be between 1 and 16 inclusive. The newly created server will persist in the 'servers' table in the DataQuest db. You will automatically return to the Servers Menu upon completion. 

2) Delete Server 

The script executes the delete_server() helper function. 

The menu will provide you with a list of servers. Select the ID of the server you would like to delete. The deleted server will be removed from the DataQuest db. You will automatically return to the Servers Menu upon completion. 

3) Lookup Server by ID 

The script executes the lookup_server() helper function.

The menu will ask for a server ID# and, if the input is valid, return a corresponding server object. You will automatically return to the Server Menu upon completion. 

4) List All Servers 

The script executes the all_servers() helper function. 

The menu will provide a list of all servers currently in the DataQuest db. 

5) List User Population of Server

The script executes the users() helper function.

The menu will provide you with a list of servers. Select the ID of the server you want to learn about. The menu will provide a list of all users currently active on the server you selected. You will automatically return to the Servers Menu upon completion. 

6) Return to Main Menu 

The script executes the main_menu() function, returning you to the main menu. 

#Models

DataQuest has two primary models: server and user. The relationship between the models is reflective of a one-to-many object relationship (one server for many users). 

##Server Model

The server model class initializes with name, player maximum, and id attributes. The name property controls for the data type (must be string) and name length (must be greater than 5). The player_max property controls for the data type (must be integer) and size (must be between 1 and 16, inclusive). The id attribute defaults to none and is set after assignment to the server table. 

###create_server()

Creating a new server starts with the create_server() class method, which activates both initialization and the save() function, which impliments the newly created server data in the database and sets the instance id to correspond with the SQL database id. 

It requires a server name and player max argument.

###delete_server()

Deleting a server is handled with the delete_server() method. It requires a server argument.

###find_by_id(), all_servers(), instance_from_db()

Normal queries are handled by the find_by_id() and all_servers() class methods. Both methods utilize the instance_from_db() class method to return the queried data to the user. The instance_from_db takes the queried data and returns the corresponding instances that match the query. 

find_by_id requires a server id argument. 

###users()

Queries that require data from the users table are handled by the users() method. It similarly sends the data it retrieves to the instance_from_db() method, but the User class version of the method instead of the Server class. In this case it will return a list of users that belong to a given server. 

The model also includes class functions for creating and dropping the SQL 'servers' table. These are primarily used when seeding data for the DataQuest database. 

##user Model 

The user model class initializes with username, password, server_id, and id attributes. Both the username and password properties control for data type (must be a string) and name length (must be greater than 5). The server_id property defaults to 1 (Atlantic server). The id attribute defaults to none and is set after assignment to the user table. 

###create_user()
 
Similar to the Server class, creating a new user starts with the create_user() class method, which initializes the object and executes the save() function. The save() function impliments the newly created server data in the database and sets the instance id to correspond with the SQL database id.  

It requires a username, password and server_id argument. 

###delete_user()

Deleting a server from the database is handled with the delete_user() method. It requires a user argument.

###find_by_id(), all_users(), instance_from_db()

Normal queries are handled by the find_by_id() and all_users() class methods. Both methods utilize the instance_from_db() class method to return the queried data to the user. The instance_from_db method takes the queried data and returns the corresponding instances that match the query. 

find_by_id() requires a user id argument. 

###server()

Queries that require data from the servers table are handled by the server() method. It similarly sends the data it retrieves to the instance_from_db() method, but the Server class version of the method instead of the User class. In this case it will return the server that the given user account is active on.

The model also includes class functions for creating and dropping the SQL 'users' table. These are primarily used when seeding data for the DataQuest database. 

server() requires a user argument.  

#License

MIT License

Copyright (c) [year] [fullname]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

This README serves as a template. Replace the contents of this file to describe
the important files in your project and describe what they do. Each Python file
that you edit should get at least a paragraph, and each function should be
described with a sentence or two.

Describe your actual CLI script first, and with a good level of detail. The rest
should be ordered by importance to the user. (Probably functions next, then
models.)
