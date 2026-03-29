class Element:

    def __init__(self, value: float, unit_letter: str):
        self.value = value
        self.unit_letter = unit_letter

    def __str__(self):
        return f"{self.value} {self.unit_letter}"


class Voltage(Element):

    def __init__(self, value):
        super().__init__(value, "V")


class Current(Element):

    def __init__(self, value):
        super().__init__(value, "A")


class Resistance(Element):
    def __init__(self, value):
        super().__init__(value, "Ohms")


class OhmsLaw:

    @staticmethod
    def calculateVoltage(current: Current, resistance: Resistance):
        result = current.value * resistance.value
        return Voltage(result)

    @staticmethod
    def calculateCurrent(voltage: Voltage, resistance: Resistance):
        return Current(voltage.value / resistance.value)

    @staticmethod
    def calculateResistance(voltage: Voltage, current: Current):
        return Resistance(voltage.value / current.value)