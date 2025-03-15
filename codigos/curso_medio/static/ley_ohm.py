class OhmLaw:

    @staticmethod
    def get_voltage(current, resistance=1):
        return resistance * current

    @staticmethod
    def get_resistance(voltage, current=1):
        return voltage / current

    @staticmethod
    def get_current(voltage , resistance):
        return voltage / resistance
