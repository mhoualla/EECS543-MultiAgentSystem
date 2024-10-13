class Agent:
    def __init__(self, name, age, gender, race, income, position):
        self.name = name
        self.age = age
        self.gender = gender
        self.race = race
        self.income = income
        self.position = position

    def get_demographics(self):
        return {
            'name': self.name,
            'age': self.age,
            'gender': self.gender,
            'race': self.race,
            'income': self.income,
            'position': self.position
        }
