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


def proteinSelector() -> dict: # TODO
    """
    Gather's user information on their protein selection.  Returns selection to caller along with a price for the item.
    :return: dict
    """
    pass


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
    sandwichToppings = []
    sandwichToppings.append(breadSelector())

    print(sandwichToppings)


if __name__ == '__main__':
    main()
