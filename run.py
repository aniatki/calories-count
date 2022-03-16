import gspread
from google.oauth2.service_account import Credentials
from termcolor import colored


welcome_str_start = "Welcome to"
foodWise = f"{colored('food', 'green')}{colored('Wise', 'cyan')}."
welcome_str_end = f"Search for any food's nutritional values by \
typing its name below.\nPlease wait...\n"

print(welcome_str_start, foodWise, welcome_str_end)


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)

SHEET = GSPREAD_CLIENT.open('nuitrition_sheet').worksheet('ABBREV')
sheet_values = SHEET.get_all_values()
all_values_list = sheet_values


def get_names():

    """First column of worksheet"""

    names = []
    for value in sheet_values:
        names.append(value[0])
    return names


names_col = get_names()


def get_casefold_food_names():

    """Converts all food names to ignore letter casing"""

    i = 0
    while i < 1:
        casefold_names = [x.casefold() for x in names_col]
        i += 1
    return casefold_names


casefold_names_converted = get_casefold_food_names()


def get_search_query():
    query = input("What would you like to search for? \
        \nExample: bread\n").casefold()
    result = list(filter(lambda x: x.startswith(query), casefold_names_converted))
    print(f"Processing {query}...")
    return result

s_query = get_search_query()


def validate(s_query):
    if s_query == [] or type(s_query) == "float" or type(s_query) == "int":
        return False
    else:
        return True


condition = validate(s_query)


def get_row_index_from_search():

    """Finds the indices of all rows that contain the search query"""

    ind_list = []
    # Loop through search results
    for q in s_query:
        index = 0
        # Loop through the names column to find matches
        for name in casefold_names_converted:
            # Get row indices
            index += 1  # Update the index for each item
            if q.casefold() == name:
                # Append the index to the list for each match
                ind_list.append(index)
    return ind_list


search_ind = get_row_index_from_search()
length = len(search_ind)


def response_from_search():

    """Shows how many results are found, if any"""

    if length <= 0:
        print(f"Sorry, we didn't find any results for {s_query}!\nHint: Try entering text.")
        get_search_query()
    else:
        print(f"{length} results found.\n")
        show_search_results()


def show_search_results():

    """Formats each individual search result to be readable"""

    for ind in search_ind:
        row = all_values_list[ind-1]
        name = row[0].capitalize()
        energy = row[1]
        protein = row[2]
        fat = row[3]
        carbs = row[4]
        fiber = row[-1]
        s_results = f"{name} contains {energy}kCal, {protein}g of protein,\
{fat}g of fat, and {fiber}g of fiber.\n"
        print(s_results)


def main():
    if condition == False:
        get_search_query()
        validate(s_query)
        get_row_index_from_search()
        response_from_search()
        show_search_results()
    response_from_search()
    show_search_results()
main()
