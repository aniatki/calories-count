class FoodEntry:
    """
    Creates an instance of FoodEntry
    """
    def __init__(self, name, energy, protein, lipid, carbs, fiber):
        self.name = name # row X col A
        self.energy = energy # row X col B
        self.protein = protein # row X col C
        self.lipid = lipid # row X col D
        self.carbs = carbs # row X col E
        self.fiber = fiber # row X col F

    def description(self):
        return f"{self.name} contains {self.energy}kCal, {self.protein}g of Protein, {self.lipid}g of Saturated Fats, {self.carbs}g of Carbohydrates and {self.fiber}g of Fiber."