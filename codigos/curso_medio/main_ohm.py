from ley_ohm import OhmLaw

if __name__ == "__main__":
    current = 3.2
    voltage = 10
    resistance = 1000

    print(
        f"El voltaje es {OhmLaw.get_voltage(current=current, resistance=resistance)}V"
    )
    print(
        f"La resistencia es {OhmLaw.get_resistance(voltage= voltage, current=current)} Ohms"
    )
    print(
        f"La corriente es {OhmLaw.get_current(voltage= voltage, resistance=resistance)}A"
    )
