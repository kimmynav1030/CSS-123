Create another instance of the Book class described in the book using a book of your choosing (or make up a book). Do the same for an instance of the Article class. Execute the write_bib_entry method for these instances and print out their results to check if it looks like what you wanted.
In the Book class definition, create another method called set_total_inventory that will take an integer as input and store the value as the attribute total_inventory. Do the same for the Article class.
In the Book class definition, create another method called get_total_inventory that returns the value of the attribute total_inventory. Do the same for the Article class.
Use the set_total_inventory method to set initial quantities to your Book and Article instances.
Create a method title_year in the Book and Article classes that will return as a string the book or journal's title and the year in parenthesis. For example, for this Book object:
team = Book( "Lencioni", "Patrick" \
             , "The Five Dysfunctions of a Team" \
             , "San Francisco" \
             , "Jossey-Bass", "2002" )
the method will return:
>>> print(team.title_year())
The Five Dysfunctions of a Team (2002)
Put the Book and Article instances you created into a list called titles. Loop through that list and print out, for each object, the title, year, and total inventory. For instance, something like this:
The Five Dysfunctions of a Team (2002): 4
Time Magazine (2016): 8
Calculate the total number of items in your store's list of titles (i.e., in the list titles) and print it to screen.  Remember each title has, in general, multiple copies in the inventory.
Create a method in the Book and Article classes called sold_one that, when called, will decrease the total inventory of that title for an instance by one. If there are no items left to sell, the method should print a message saying there are no items left to sell and leave total_inventory unchanged.
For every item in your store's list of titles (i.e., the list titles), sell two items and then print out a report listing each item in your store's list of titles (a summary description) and how many items there are left of each item.
Find at least 5 people and ask for a height and a weight. (It doesn't have to be their own.) Take these 5 pairs of numbers and create a scatter plot of height (y-axis) vs. weight (x-axis).  Choose a marker you like and make the marker size something big.