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


def cheeseSelector() -> list:
    """
    Gather's user information on their cheese selection.  Returns selection to caller along with a price for the item.
    :return: list
    """
    cheeseAvailable = {"american": 0.25, "cheddar": 0.50, "swiss": 0.75, "mozzarella": 1.00}
    cheeseNames = []
    for cheeseType in cheeseAvailable:
        cheeseNames.append(cheeseType)

    selectedCheese = pyip.inputMenu(cheeseNames, prompt="Please select a cheese:\n")
    return [selectedCheese, cheeseAvailable[selectedCheese]]


def toppingSelector() -> list:
    """
    Gather's user information on their selection of sandwich toppings.  Returns selection to caller along with a price for the items.
    :return: list
    """
    selectedToppings = []
    mayoSelect = pyip.inputYesNo(prompt="Add Mayo?((Y)es/(N)o)\n")
    if mayoSelect == 'yes':
        selectedToppings.append(["mayo", 0.00])
    mustardSelect = pyip.inputYesNo(prompt="Add Mustard?((Y)es/(N)o)\n")
    if mustardSelect == 'yes':
        selectedToppings.append(["mustard", 0.00])
    lettuceSelect = pyip.inputYesNo(prompt="Add Lettuce?((Y)es/(N)o)\n")
    if lettuceSelect == 'yes':
        selectedToppings.append(["lettuce", 0.25])
    tomatoSelect = pyip.inputYesNo(prompt="Add Tomato?((Y)es/(N)o)\n")
    if tomatoSelect == 'yes':
        selectedToppings.append(["mayo", 0.25])

    return selectedToppings


def quantityPriceCalculator(toppingsList, quantity) -> float:
    """
    Takes the price of each item on the sandwich, sums those, then multiplies the total to find the total cost for all sandwiches
    :param toppingsList: Toppings that have been selected for the sandwich with their prices
    :type toppingsList: list
    :param quantity: Count of sandwiches to be ordered
    :type quantity: int
    :return: float
    """
    singleSandwichTotal = 0
    quantityTotal = 0
    for topping in toppingsList:
        singleSandwichTotal += topping[1]

    quantityTotal = singleSandwichTotal * quantity
    return quantityTotal


def main():
    sandwichToppings = [breadSelector(), proteinSelector()]
    cheeseChoice = pyip.inputYesNo(prompt="Would you like cheese?((Y)es/(N)o)\n")
    if cheeseChoice == 'yes':
        sandwichToppings.append(cheeseSelector())
    condiments = toppingSelector()
    if len(condiments) > 0:
        for item in condiments:
            sandwichToppings.append(item)
    print(sandwichToppings)
    quantity = pyip.inputNum(prompt="How many sandwiches?\n", min=1)
    totalCost = quantityPriceCalculator(sandwichToppings, quantity)
    print("Total: $%.2f" % totalCost)


if __name__ == '__main__':
    main()
