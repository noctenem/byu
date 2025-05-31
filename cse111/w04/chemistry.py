# I have added a function to find the entered chemical formula
# in a list of known formulas and if found, print the name
# of the formula.

# The program prints the total number of protons in a molecule
# from the formula given by the user.

from formula import parse_formula

# Constants
NAME_INDEX = 0
ATOMIC_MASS_INDEX = 1
ATOMIC_NUMBER_INDEX = 2
SYMBOL_INDEX = 0
QUANTITY_INDEX = 1

def make_periodic_table():
    periodic_table = [
        ["Ac", "Actinium", 227, 89],
        ["Ag", "Silver", 107.8682, 47],
        ["Al", "Aluminum", 26.9815386, 13],
        ["Ar", "Argon", 39.948, 18],
        ["As", "Arsenic", 74.9216, 33],
        ["At", "Astatine", 210, 85],
        ["Au", "Gold", 196.966569, 79],
        ["B", "Boron", 10.811, 5],
        ["Ba", "Barium", 137.327, 56],
        ["Be", "Beryllium", 9.012182, 4],
        ["Bi", "Bismuth", 208.9804, 83],
        ["Br", "Bromine", 79.904, 35],
        ["C", "Carbon", 12.0107, 6],
        ["Ca", "Calcium", 40.078, 20],
        ["Cd", "Cadmium", 112.411, 48],
        ["Ce", "Cerium", 140.116, 58],
        ["Cl", "Chlorine", 35.453, 17],
        ["Co", "Cobalt", 58.933195, 27],
        ["Cr", "Chromium", 51.9961, 24],
        ["Cs", "Cesium", 132.9054519, 55],
        ["Cu", "Copper", 63.546, 29],
        ["Dy", "Dysprosium", 162.5, 66],
        ["Er", "Erbium", 167.259, 68],
        ["Eu", "Europium", 151.964, 63],
        ["F", "Fluorine", 18.9984032, 9],
        ["Fe", "Iron", 55.845, 26],
        ["Fr", "Francium", 223, 87],
        ["Ga", "Gallium", 69.723, 31],
        ["Gd", "Gadolinium", 157.25, 64],
        ["Ge", "Germanium", 72.64, 32],
        ["H", "Hydrogen", 1.00794, 1],
        ["He", "Helium", 4.002602, 2],
        ["Hf", "Hafnium", 178.49, 72],
        ["Hg", "Mercury", 200.59, 80],
        ["Ho", "Holmium", 164.93032, 67],
        ["I", "Iodine", 126.90447, 53],
        ["In", "Indium", 114.818, 49],
        ["Ir", "Iridium", 192.217, 77],
        ["K", "Potassium", 39.0983, 19],
        ["Kr", "Krypton", 83.798, 36],
        ["La", "Lanthanum", 138.90547, 57],
        ["Li", "Lithium", 6.941, 3],
        ["Lu", "Lutetium", 174.9668, 71],
        ["Mg", "Magnesium", 24.305, 12],
        ["Mn", "Manganese", 54.938045, 25],
        ["Mo", "Molybdenum", 95.96, 42],
        ["N", "Nitrogen", 14.0067, 7],
        ["Na", "Sodium", 22.98976928, 11],
        ["Nb", "Niobium", 92.90638, 41],
        ["Nd", "Neodymium", 144.242, 60],
        ["Ne", "Neon", 20.1797, 10],
        ["Ni", "Nickel", 58.6934, 28],
        ["Np", "Neptunium", 237, 93],
        ["O", "Oxygen", 15.9994, 8],
        ["Os", "Osmium", 190.23, 76],
        ["P", "Phosphorus", 30.973762, 15],
        ["Pa", "Protactinium", 231.03588, 91],
        ["Pb", "Lead", 207.2, 82],
        ["Pd", "Palladium", 106.42, 46],
        ["Pm", "Promethium", 145, 61],
        ["Po", "Polonium", 209, 84],
        ["Pr", "Praseodymium", 140.90765, 59],
        ["Pt", "Platinum", 195.084, 78],
        ["Pu", "Plutonium", 244, 94],
        ["Ra", "Radium", 226, 88],
        ["Rb", "Rubidium", 85.4678, 37],
        ["Re", "Rhenium", 186.207, 75],
        ["Rh", "Rhodium", 102.9055, 45],
        ["Rn", "Radon", 222, 86],
        ["Ru", "Ruthenium", 101.07, 44],
        ["S", "Sulfur", 32.065, 16],
        ["Sb", "Antimony", 121.76, 51],
        ["Sc", "Scandium", 44.955912, 21],
        ["Se", "Selenium", 78.96, 34],
        ["Si", "Silicon", 28.0855, 14],
        ["Sm", "Samarium", 150.36, 62],
        ["Sn", "Tin", 118.71, 50],
        ["Sr", "Strontium", 87.62, 38],
        ["Ta", "Tantalum", 180.94788, 73],
        ["Tb", "Terbium", 158.92535, 65],
        ["Tc", "Technetium", 98, 43],
        ["Te", "Tellurium", 127.6, 52],
        ["Th", "Thorium", 232.03806, 90],
        ["Ti", "Titanium", 47.867, 22],
        ["Tl", "Thallium", 204.3833, 81],
        ["Tm", "Thulium", 168.93421, 69],
        ["U", "Uranium", 238.02891, 92],
        ["V", "Vanadium", 50.9415, 23],
        ["W", "Tungsten", 183.84, 74],
        ["Xe", "Xenon", 131.293, 54],
        ["Y", "Yttrium", 88.90585, 39],
        ["Yb", "Ytterbium", 173.054, 70],
        ["Zn", "Zinc", 65.38, 30],
        ["Zr", "Zirconium", 91.224, 40],
    ]

    return {symbol: [name, atomic_mass, atomic_number] for symbol, name, atomic_mass, atomic_number in periodic_table}

def compute_molar_mass(symbol_quantity_list, periodic_table_dict):
    total_mass = 0
    for element in symbol_quantity_list:
        symbol = element[SYMBOL_INDEX]
        quantity = element[QUANTITY_INDEX]
        atomic_mass = periodic_table_dict[symbol][ATOMIC_MASS_INDEX]
        total_mass += atomic_mass * quantity

    return total_mass

def sum_protons(symbol_quantity_list, periodic_table_dict):
    total_protons = 0
    for element in symbol_quantity_list:
        symbol = element[SYMBOL_INDEX]
        quantity = element[QUANTITY_INDEX]
        atomic_number = periodic_table_dict[symbol][ATOMIC_NUMBER_INDEX]
        total_protons += atomic_number * quantity

    return total_protons

known_molecules_dict = {
    "Al2O3": "aluminum oxide",
    "CH3OH": "methanol",
    "C2H6O": "ethanol",
    "C2H5OH": "ethanol",
    "C3H8O": "isopropyl alcohol",
    "C3H8": "propane",
    "C4H10": "butane",
    "C6H6": "benzene",
    "C6H14": "hexane",
    "C8H18": "octane",
    "CH3(CH2)6CH3": "octane",
    "C13H18O2": "ibuprofen",
    "C13H16N2O2": "melatonin",
    "Fe2O3": "iron oxide",
    "FeS2": "iron pyrite",
    "H2O": "water"
}

def get_formula_name(formula, known_molecules_dict):
    return known_molecules_dict.get(formula, '')

def main():
    formula = input('Enter the molecular formula (H2O): ')
    mass = float(input('Enter the mass of the sample in grams: '))

    periodic_table = make_periodic_table()
    symbol_quantity_list = parse_formula(formula, periodic_table)
    molar_mass = compute_molar_mass(symbol_quantity_list, periodic_table)
    moles = mass / molar_mass

    compound_name = get_formula_name(formula, known_molecules_dict)
    total_protons = sum_protons(symbol_quantity_list, periodic_table)

    print(f'Computed name: {compound_name}')
    print(f'Molar mass: {molar_mass:.5f} grams/mole')
    print(f'Moles: {moles:.5f} moles')
    print(f'Total protons: {total_protons}')


    """
    for element in periodic_table:
        name = element[1]
        atomic_mass = element[2]
        print(f'{name} {atomic_mass}')
    """

if __name__ == '__main__':
    main()