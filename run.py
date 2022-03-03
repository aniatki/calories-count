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
SHEET = GSPREAD_CLIENT.open('nuitrition_sheet')

food_entries = SHEET.worksheet('ABBREV')

class FoodEntry:
    """
    Creates an instance of FoodEntry
    """
    def __init__(self, name, energy, protein, lipid, carbs, fiber):
        self.name = name
        self.energy = energy
        self.protein = protein
        self.lipid = lipid
        self.carbs = carbs
        self.fiber = fiber

    def description(self):
        return f"{self.name} contains {self.energy}kCal, {self.protein}g of Protein, {self.lipid}g of Saturated Fats, {self.carbs}g of Carbohydrates and {self.fiber}g of Fiber."

food_names = food_entries.col_values(1)

i = 0
while i < len(food_names):
    food_names[i].lower()
    i += 1