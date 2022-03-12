import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)

SHEET = GSPREAD_CLIENT.open('nuitrition_sheet').worksheet('ABBREV')
names_col = SHEET.col_values(1)


def get_casefold_food_names():
    i = 0
    while i < 1:
        casefold_names = [x.casefold() for x in names_col]
        i += 1
    return casefold_names


def get_search_query():
    query = input("Please enter text here\n").casefold()
    result = list(filter(lambda x: x.startswith(query), casefold_names_converted))
    return result


def get_row_index_from_search():    
    ind_list = []
    # Loop through search results
    for result in search_results:
        index = 0
        # Loop through the names column to find matches
        for name in casefold_names_converted:
            #Get row indices
            index += 1 # Update the index for each match
            if result.casefold() == name:
                ind_list.append(index)
    return ind_list


def display_search_results():

    if len(index_query_list) == 0:
        print(f"Sorry, we didn't find any results!\nHint: Try entering text.")
    elif len(index_query_list) > 0:
        print(f"We found {len(index_query_list)} results.\n")
    return len(index_query_list)


def create_data_from_row():
    for ind in index_query_list:
        row = SHEET.row_values(ind)
        name = row[0].capitalize()
        energy = row[1]
        protein = row[2]
        fat = row[3]
        carbs = row[4]
        fiber = row[-1]
        print(f"{name} contains {energy}kCal, {protein}g of protein, {fat}g of fat, and {fiber}g of fiber.")


# Calling the functions

casefold_names_converted = get_casefold_food_names()
search_results = get_search_query()
index_query_list = get_row_index_from_search()
display_search_results()
create_data_from_row()
