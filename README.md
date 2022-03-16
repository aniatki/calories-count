<img src="./lightmode.png" alt="FoodWise logo" width="150" style="margin:-20px 0 0">

# Look up your food in a CLI application

FoodWise allows you to look up any detail about your food simply by entering its name in the command line. Our wide range of food entries will bring up any suggestions or keywords related to that food that you might want to have a look at or any substitute suggestions.

[foodWise Heroku Link](foodwise.png)

## Existing Features

* Search for foods by entering a food name in the input field in the command line to view its nutritional values.

There's a huge range of entries in a spreadsheet for foods (over 8000 entries), by having details about a specific food in a row of data. The name in the first column, then numbers about energy, protein, fat and fiber in their respective columns. The input string typed by the user triggers a function that iterates through all the rows of data to find potential matches, and when it does it displays those entries in the console as found in the image below.

![Snapshot of foodWise CLI](https://i.ibb.co/BfjtFj4/foodwise.png)

## Features to Add

* Ability to enter a row of data for a specific food that isn't already in the database.
* Ability to search by its nutritional values rather than just the food name.

## Testing
### Validator Testing

Code was validated by PEP8 standards and no errors were found during testing. There's comments and docstrings implemented in parts of the code which its functionality is not obvious to make it easier to read and understand.

### Unfixed Bugs

* The input type `int` in the search query has not been dealt with.
* The program doesn't restart the query function after an input that doesn't match the database has been submitted.

## Deployment

As advised on the walkthrough project **Love sandwiches**, the app has been deployed to Heroku beforehand to see for any bugs or surprises along the way. The `requirements.txt` file has been updated everytime a new library or module has been added to the project, as it is vital for the functionality of the program. 

Once the steps are followed correctly, the deployment process is very straightforward. Heroku and GitHub have made it very easy to maintain the latest `git push` on our app.

## Credits

* [Excel file source]('https://www.excelmadeeasy.com/templates-nutritional-charts.php')

* My mentor for being very patient and helpful, [GitHub Profile]('https://github.com/celelstine')

### Content

One of the challenges that i spent most time on on this project was getting the indices of the rows that matched the search results. After spending a considerable amount of time on that, I finally resolved that by going throuogh each row on the spreadsheet, assigning a variable `i` and increasing its value every time it looped. If the search term matched with the name on the row, then the variable would be assigned to a new `list`. This resulted in a logical way to get the search results and was also fast when testing.

The code was optimized to make an API call only once per running the program so python wouldn't go into `RecursionError`. 

The code consists mainly of iteration loops and `if` statements for the most part. 
