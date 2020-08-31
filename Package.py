class Package:
    def __init__(self, package_id, address, deadline, weight):
        self.package_id = package_id
        self.address = address
        self.deadline = deadline
        self.weight = weight
        self.is_delivered = False

    def __eq__(self, other):
        return self.package_id == other.package_id

    def __hash__(self):
        return hash(self.package_id)
