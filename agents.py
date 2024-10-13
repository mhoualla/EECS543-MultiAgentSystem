class Agent:
    def __init__(self, name, age, gender, income, position, values, biases):
        self.name = name
        self.age = age
        self.gender = gender
        self.income = income
        self.position = position
        self.values = values 
        self.biases = biases

    def get_demographics(self):
        return {
            'name': self.name,
            'age': self.age,
            'gender': self.gender,
            'income': self.income,
            'position': self.position,
            'values': self.values,
            'biases': self.biases,
        }
