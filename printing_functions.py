
def print_models(unprinted_designs, completed_models):
    """Simulate printing each design, until none is left.
       Move each design to completed_models after printing.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """Show all the models that were printed."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(f". {completed_model}")

# unprinted_designs = ["phone case", "robot pendant", "dodecahedron"]
# completed_models = []

# print_models(unprinted_designs[:], completed_models)
# show_completed_models(completed_models)

def build_me_car(brand, model, *other_details):
    """A function that stores information about car."""
    car_info =  (f"\nI want to build a {brand.title()}  {model.title()} "
                 "with these details:")
    print(car_info)
    for detail in other_details:
        print(f"\t> {detail.title()}")


# purchasing = build_me_car("raptor", "t13 ford", "color:grey",
#              "offroad_tires: Yes", "offroad_suspension: Yes", "tow_service: No")

# print(purchasing)