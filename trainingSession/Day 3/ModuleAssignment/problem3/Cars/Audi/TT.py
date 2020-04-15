
Specs = {"Name": "TT", "Price": "30", "Specifications": (
    "a", "b", "c"), "Available colors": ("black", "white")}


def price():
    return Specs['Price']


def specifications():
    return Specs['Speecifications']


def availableColors():
    return Specs['Available colors']


def exportSpecs():
    return Specs


def compareWith(otherSpecs):
    print("Comparison between " + Specs['Name'] + " and " + otherSpecs["Name"])
    print("\nPrice: " + Specs['Price']+"\t|\t"+otherSpecs['Name'])
    print("\nSpecifications: ")
    for (spec1, spec2) in zip(Specs['Specifications'], otherSpecs['Specifications']):
        print(spec1+"\t|\t"+spec2+'\n')
