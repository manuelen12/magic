class Magic:

    def __init__(self, count: int):
        self.count = count

    def get_value(self):
        numbers = []
        for number in range(1, self.count+1):
            _spell = self.spell(number)
            numbers.append(_spell)
            print(_spell)
        return numbers

    @staticmethod
    def spell(number):
        _magic = ""
        if not number % 3:
            _magic += "abracadabra"
        if not number % 5:
            _magic += "alakazam"

        if not _magic:
            return str(number)
        else:
            return _magic
