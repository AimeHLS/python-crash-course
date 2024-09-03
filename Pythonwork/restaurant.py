from module3 import Restaurant, IceCreamStand

icecream= IceCreamStand("mubarak",
                        "italian",
                        ("vanilla", "chocolate", "lemon","green tea"))
mubarak = Restaurant("mubarak", "italian")

icecream.dispaly_flavors()
mubarak.describe_menu(("dulian pizza","t-bone steak", "cheese macaroni"))


