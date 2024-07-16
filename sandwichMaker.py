import pyinputplus as pyip


def breadSelector() -> list:
    """
    Gather's user information on their bread selection.  Returns selection to caller along with a price for the bread.
    :return: list
    """
    breadAvailable = {"white": 0.10, "wheat": 0.15, "sourdough": 0.20} # Breadname & price for bread
    breadNames = []
    for breadType in breadAvailable:
        breadNames.append(breadType)

    selectedBread = pyip.inputMenu(breadNames, prompt="Please select bread:\n")
    return [selectedBread, breadAvailable[selectedBread]]


def proteinSelector() -> list:
    """
    Gather's user information on their protein selection.  Returns selection to caller along with a price for the item.
    :return: list
    """
    proteinAvailable = {"ham": 1.50, "roast beef": 1.25, "turkey": 1.75, "chicken": 1.00, "tofu": 2.00}
    proteinNames = []
    for proteinType in proteinAvailable:
        proteinNames.append(proteinType)

    selectedProtein = pyip.inputMenu(proteinNames, prompt="Please select a protein:\n")
    return [selectedProtein, proteinAvailable[selectedProtein]]


def cheeseSelector() -> dict: # TODO
    """
    Gather's user information on their cheese selection.  Returns selection to caller along with a price for the item.
    :return: dict
    """
    pass


def toppingSelector() -> dict: # TODO
    """
    Gather's user information on their toppings selection.  Returns selection to caller along with a price for the items.
    :return: dict
    """
    pass


def main():
    sandwichToppings = [breadSelector(), proteinSelector()]

    print(sandwichToppings)


if __name__ == '__main__':
    main()
