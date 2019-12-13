# Borderlands2Project
COMP 420 DB Project

To set up a seperate instance of this database, Run the Import Data Files with different credentials between lines 7 and 10.

To connect to a seperate instance in the GUI, change the credentials between line 1872 and 1878.

Under normal operations, this database connects to a CI-Keys MySQL server. A user account and IP address permissions will be provided 
from an administator. 






Using the GUI is simple. Upon running the script, you will be prompted for login credentials. Inputting the correct username and password
will allow access to the database and functionality for the main UI. 

From the main UI you can create new characters, click checkboxes, change selected characters and change queries just to name some of the 
initial options. Some queries do no require any setup in the interface such as 'Show All Vehicles'. 

When selecting a character, many options become available, such as 'Show Character Equipment' or 'Show Current Character Stats and Badass'.
Currencies are also updated to what is on record in the database.

You can manipulate main currencies by changing those values directly and hitting the update currency button for that character. Or you
can manipulate the ammunition by left-clicking and right-clicking those boxes. Incrementing and deincrementing the values by 1.

Other buttons such as 'Add/Duplicate Item to Inventory' or 'Equip Item on Character' requires more options to be selected, in logical 
fashion. For example, to delete an item from the inventory, you need to be in the inventory to select an item. To unequip an item, you need
to be looking into equipment. To add an item, you may need to be in the vast variety of other queries.

Preforming any of those operations is as simple as clicking on the desired object and pressing the action you require. These operations
usually require a selected character so do not forget to choose one. Not that many of the operations will allow you to do anything without
a character. 

Play around with the GUI. The auto-update functionality is fun, easy to use, and gives good feedback for most actions the user performs. 
