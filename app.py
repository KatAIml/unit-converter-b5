"""Command-line menu for the Unit Converter (Group B5)."""

from converter.length import convert_length, UNITS as LENGTH_UNITS
from converter.temperature import convert_temperature, UNITS as TEMP_UNITS
from converter.weight import convert_weight, UNITS as WEIGHT_UNITS

MENU = {
    "1": ("Length", convert_length, list(LENGTH_UNITS)),
    "2": ("Temperature", convert_temperature, list(TEMP_UNITS)),
    "3": ("Weight", convert_weight, list(WEIGHT_UNITS)),
}


def main():
    for key, (name, _, units) in MENU.items():
        print(f"{key}. {name} ({', '.join(units)})")
    choice = input("Choose a category: ").strip()
    if choice not in MENU:
        print("Invalid choice")
        return
    name, func, _ = MENU[choice]
    try:
        value = float(input("Value: "))
        src = input("From unit: ").strip()
        dst = input("To unit: ").strip()
        print(f"Result: {func(value, src, dst):.4f} {dst}")
    except (ValueError, TypeError) as err:
        print(f"Error: {err}")


if __name__ == "__main__":
    main()
