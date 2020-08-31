class Location:
    def __init__(self, name, street, city, state, zip_code):
        self.name = name
        self.street = street
        self.city = city
        self.state = state
        self.zip_code = zip_code

    def __hash__(self):
        return hash(self.street, self.city, self.name)

    def __eq__(self, other):
        if other == None:
            return False
        elif isinstance(other, Location):
            return self.street == other.street and self.city == other.city and self.zip_code == other.zip_code

    def __str__(self):
        return f"{self.street}, {self.city}, {self.state} {self.zip_code}"

    def __repr__(self):
        return f"Location({self.name}, {self.street}, {self.city}, {self.state}, {self.zip_code})"
        
