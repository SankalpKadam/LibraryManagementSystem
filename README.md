# Library Management System
A basic project on Library Management System using Python as programming language

• USER LOGIN 
 
This feature used by the user to login into system. They are required to enter user id and password before they are allowed to enter the system .The user id and password will be verified and if invalid id is there user is allowed to not enter the system.

User ID - "admin" & Password - "admin123"
 
Functional requirements :

✓ user id is provided when they register 

✓ The system must only allow user with valid id and password to enter the system 

✓ The system performs authorization process which decides what user level can acess to. 

✓ The user must be able to logout after they finished using system. 
 
 
• REGISTER NEW USER 
 
This feature can be performed by all users to register new user to create account. 
 
Functional requirements :

✓ System must be able to verify information

✓ System must be able to delete information if information is wrong 
 
 
• REGISTER NEW BOOK 
 
This feature allows to add new books to the library 
 
Functional requirements : 

✓ System must be able to verify information 

✓ System must be able to enter number of copies into table. 

✓ System must be able to not allow two books having same book id 
 
• SEARCH BOOK 
 
This feature is found in book maintenance part . we can search book based on book id , book name , publication or by author name. 
 
Functional requirements : 

✓ System must be able to search the database based on select search type 

✓ System must be able to filter book based on keyword entered 

✓ System must be able to show the filtered book in table view 
 
 
• ISSUE BOOKS AND RETURN BOOKS 
 
This feature allows to issue and return books and also view reports of book issued. 
 
Functional requirements :

✓ System must be able to enter issue information in database.

✓ System must be able to update number of books. 

✓ System must be able to search if book is available or not before issuing books

✓ System should be able to enter issue and return date information 

METHODOLOGY 

The LIBRARY MANAGEMENT SYSTEM app that we have build consists of two parts i.e the front end is designed completely by using core python to build GUI and the back end is designed by using MY SQL in phpmyadmin as database. 
 
HOME PAGE Now, when we run the application, it'll display us a simple home page which asks the user for the username and password. If the credentials are incorrect, then a pop up appears saying "login unsuccessfull". 

Once logged in, the user will get certain menu choices like 

• BOOKS 

• ISSUE 

• RETURN 

• STUDENTS 

• LIBRARIAN 

simultaneously, a server-side database purely using MySQL will be used, so that all the records we create can be properly saved. 
 
FUNCTIONS 
 
• BOOKS 
 
   ✓ Add books                       
   A window where employees can add books into the library with certain information regarding the book. (Book ID, name, etc) 

  ✓ Delete book                        
  A window where employees can delete their books from the library. 
 
  ✓ View all books
  This window shows us a tabular form of all the books present in our library. Whenever we add any new book that shows up here, any changes we make in the table will be reflected    here. 
 
• ISSUE 

This window gives the option to the employee to issue a book to the student, provided that he enters the correct book ID and the correct student informations like student name , library ID and date of issue. 
 
• RETURN 

This window gives the option to the student to return a book to the library, provided that he enters the correct library ID of the student and also the date of returning the book. 
 
• STUDENTS 

This window gives the option to the student to register himself/herself by entering his/her name, library ID, contact number, Unique ID and course. 
 
• LIBRARIAN 

This window gives the option to the employee to register himself/herself by entering his/her name, contact number, employee ID and address. 
 
All the informations that the user enters will be stored in a database using MY SQL and can be viewed anytime the user wants. 
 
 
 
