class Retailitem:
    def __init__(self, d, u, p):
        self.__description = d
        self.__units = u
        self.__price = p

    def set_description(self, newdescription):
        self.__description = newdescription

    def set_units(self, newunits):
        self.__units = newunits

    def set_price(self, newprice):
        self.__price = newprice

    def get_description(self):
        return self.__description

    def get_units(self):
        return self.__units

    def get_price(self):
        return self.__price
