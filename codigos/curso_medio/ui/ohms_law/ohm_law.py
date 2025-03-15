class Element:

    VOLTAGE = 100
    CURRENT = 200
    RESISTANCE = 300
    POWER = 400

    def __init__(self, value: float, unit_letter: str):
        self.value = value
        self.unit_letter = unit_letter

    def __str__(self):
        return f"{self.value} {self.unit_letter}"

    def name(self):
        return ""


class Voltage(Element):

    def __init__(self, value):
        super().__init__(value, "V")

    def name(self):

        return "voltage"


class Current(Element):

    def __init__(self, value):
        super().__init__(value, "A")

    def name(self):
        return "current"


class Resistance(Element):
    def __init__(self, value):
        super().__init__(value, "Ω")

    def name(self):
        return "resistance"


class OhmsLaw:

    @staticmethod
    def calculateVoltage(current: Current, resistance: Resistance):
        result = current.value * resistance.value
        return Voltage(result)

    @staticmethod
    def calculateCurrent(voltage: Voltage, current: Current):
        return Current(voltage.value / current.value)

    @staticmethod
    def calculateResistance(voltage: Voltage, current: Current):
        return Resistance(voltage.value / current.value)
