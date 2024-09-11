with open('recipes.txt', 'r', encoding='utf-8') as f:
    recipes = f.read().split("\n\n")

cookbook = {}

for i in recipes:
    i = i.split("\n")
    cookbook[i[0]] = []
    auxlist = i[2:]
    auxlist2 = {}
    auxlist3 = []
    for y in auxlist:
        y = y.split(' | ')
        auxlist2["ingredient_name"] = y[0]
        auxlist2["quantity"] = int(y[1])
        auxlist2["measure"] = y[2]
        auxlist3.append(auxlist2)
        auxlist2 = {}
    cookbook[i[0]] = auxlist3


def get_shop_list_by_dishes(dishes, person_count):
    grocerylist = {}
    for i in dishes:
        if i not in cookbook.keys():
            return print("No such dish in my books")
        for y in cookbook[i]:
            if y['ingredient_name'] in grocerylist.keys():
                valueupdate = y
                grocerylist.update({y['ingredient_name']: {'measure': y['measure'], 'quantity': valueupdate['quantity'] + (y['quantity']*person_count)}})
            else:
                grocerylist[y['ingredient_name']] = {'measure': y['measure'], 'quantity': (y['quantity'] * person_count)}
    return print(grocerylist)


get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
get_shop_list_by_dishes(['Фахитос', 'Омлет'], 3)
