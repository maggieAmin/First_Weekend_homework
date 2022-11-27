# WRITE YOUR FUNCTIONS HERE

def get_pet_shop_name(pet_shop):
    return pet_shop["name"]

def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]

def add_or_remove_cash(pet_shop, cash):
    pet_shop["admin"]["total_cash"] += cash

def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]

def increase_pets_sold(pet_shop, pet_num):
    pet_shop["admin"]["pets_sold"] += pet_num

def get_stock_count(pet_shop):
    return len(pet_shop["pets"])

def get_pets_by_breed(pet_shop, pet_breed):
    list_of_pets = []
    for pet in pet_shop["pets"]:
        if pet["breed"] == pet_breed:
            list_of_pets.append(pet)
    return list_of_pets

def find_pet_by_name(pet_shop, pet_name):
    for pet in pet_shop["pets"]:
        if pet["name"] == pet_name:
            return pet

def remove_pet_by_name(pet_shop, pet_name):
    list_of_pets = []
    for pet in pet_shop["pets"]:
        if pet["name"] != pet_name:
            list_of_pets.append(pet)
    pet_shop["pets"] = list_of_pets

def add_pet_to_stock(pet_shop, new_pet):
    pet_shop["pets"].append(new_pet)

def get_customer_cash(customer):
    return customer["cash"]

def remove_customer_cash(customer, cash):
    customer["cash"] -= cash

def  get_customer_pet_count(customer):
    return len(customer["pets"])

def add_pet_to_customer(customer, new_pet):
    customer["pets"].append(new_pet)

def customer_can_afford_pet(customer, pet):
    return customer["cash"] >= pet["price"]

def sell_pet_to_customer(pet_shop, pet, customer):
    if pet != None:
        cash = pet["price"]
        if customer_can_afford_pet(customer, pet):

            remove_customer_cash(customer, cash)
            add_or_remove_cash(pet_shop, cash)
            add_pet_to_customer(customer, pet)
            remove_pet_by_name(pet_shop, pet["name"])
            pet_num = 1
            increase_pets_sold(pet_shop, pet_num)
        
    


