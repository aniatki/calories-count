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

casefold_names_converted = get_casefold_food_names()


def get_search_query():
    query = input("Please enter text here\n").casefold()
    result = list(filter(lambda x: x.startswith(query), casefold_names_converted))
    return result

search_results = get_search_query()

def get_row_index_from_search():    
    
    # Loop through search results
    ind_list = []
    
    for result in search_results:
        
        index = 0
        
        # Loop through the names column to find matches
        for name in casefold_names_converted:
            #Get row indices
            index += 1 # Update the index for each match
            if result.casefold() == name:
                ind_list.append(index)
    return ind_list

