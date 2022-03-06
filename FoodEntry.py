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