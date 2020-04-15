__all__ = ["Audi", "BMW", "Jaguar", "Mercedes"]


def price(Specs):
    return Specs['Price']


def specifications(Specs):
    return Specs['Speecifications']


def availableColors(Specs):
    return Specs['Available colors']


# def compareWith(Specs1, Specs2):
#     print("Comparison between ")
#     #  + Specs1['Name'] + " and " + Specs2["Name"])
#     print("\nPrice: ")

#     # + Specs1['Price']+"\t|\t"+ Specs2['Price'])
#     print("\nSpecifications: ")
#     for (spec1, spec2) in zip(Specs['Specifications'], otherSpecs['Specifications']):
#         print(spec1+"\t|\t"+spec2+'\n')
