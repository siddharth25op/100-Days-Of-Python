import data

run_machine = False

money = []

while not run_machine:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if user_choice == "report":
        for key in data.resources:
            print(f"{key}: {data.resources[key]}")
        new_money = sum(money)
        print(f"Money: ${new_money}")

    elif user_choice == "espresso":
        espresso_cost = float(data.MENU["espresso"]["cost"])
        if data.resources["water"] >= data.MENU["espresso"]["ingredients"]["water"]:
            if data.resources["coffee"] >= data.MENU["espresso"]["ingredients"]["coffee"]:
                coins_by_user = float(input("Please insert coins: "))
                if coins_by_user >= espresso_cost:
                    refunded_money = coins_by_user - espresso_cost
                    print(f"Here is ${refunded_money} in change.")
                    print("Here is your espresso. Enjoy!")
                    data.resources["water"] = data.resources["water"] - data.MENU["espresso"]["ingredients"]["water"]
                    data.resources["coffee"] = data.resources["coffee"] - data.MENU["espresso"]["ingredients"]["coffee"]
                    money.append(espresso_cost)
                else:
                    print("Sorry that's not enough money. Money refunded")
            else:
                print("Sorry there is not enough coffee.")
        else:
            print("Sorry there is not enough water.")

    elif user_choice == "latte":
        latte_cost = float(data.MENU["latte"]["cost"])
        if data.resources["water"] >= data.MENU["latte"]["ingredients"]["water"]:
            if data.resources["coffee"] >= data.MENU["latte"]["ingredients"]["coffee"]:
                if data.resources["milk"] >= data.MENU["latte"]["ingredients"]["milk"]:
                    coins_by_user = float(input("Please insert coins: "))
                    if coins_by_user >= latte_cost:
                        refunded_money = coins_by_user - latte_cost
                        print(f"Here is ${refunded_money} in change.")
                        print("Here is your latte. Enjoy!")
                        data.resources["water"] = data.resources["water"] - data.MENU["latte"]["ingredients"][
                            "water"]
                        data.resources["coffee"] = data.resources["coffee"] - data.MENU["latte"]["ingredients"][
                            "coffee"]
                        data.resources["milk"] = data.resources["milk"] - data.MENU["latte"]["ingredients"][
                            "milk"]
                        money.append(latte_cost)
                    else:
                        print("Sorry that's not enough money. Money refunded")
                else:
                    print("Sorry there is not enough milk.")
            else:
                print("Sorry there is not enough coffee.")
        else:
            print("Sorry there is not enough water.")

    elif user_choice == "cappuccino":
        cappuccino_cost = float(data.MENU["cappuccino"]["cost"])
        if data.resources["water"] >= data.MENU["cappuccino"]["ingredients"]["water"]:
            if data.resources["coffee"] >= data.MENU["cappuccino"]["ingredients"]["coffee"]:
                if data.resources["milk"] >= data.MENU["cappuccino"]["ingredients"]["milk"]:
                    coins_by_user = float(input("Please insert coins: "))
                    if coins_by_user >= cappuccino_cost:
                        refunded_money = coins_by_user - cappuccino_cost
                        print(f"Here is ${refunded_money} in change.")
                        print("Here is your cappuccino. Enjoy!")
                        data.resources["water"] = data.resources["water"] - data.MENU["cappuccino"]["ingredients"][
                            "water"]
                        data.resources["coffee"] = data.resources["coffee"] - data.MENU["cappuccino"]["ingredients"][
                            "coffee"]
                        data.resources["milk"] = data.resources["milk"] - data.MENU["cappuccino"]["ingredients"][
                            "milk"]
                        money.append(cappuccino_cost)
                    else:
                        print("Sorry that's not enough money. Money refunded")
                else:
                    print("Sorry there is not enough milk.")
            else:
                print("Sorry there is not enough coffee.")
        else:
            print("Sorry there is not enough water.")

    elif user_choice == "off":
        run_machine = True

    else:
        print("Wrong Input")