def init_cookbook():
    with open('recipes.txt', 'r', encoding='utf-8') as f:
        recipes = f.read().split("\n\n")

    cookbook1 = {}

    for i in recipes:
        i = i.split("\n")
        cookbook1[i[0]] = []
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
        cookbook1[i[0]] = auxlist3

    return cookbook1


def get_shop_list_by_dishes(dishes, person_count, thebook):

    grocerylist = {}

    for i in dishes:
        if i not in thebook.keys():
            return print("No such dish in my books")
        for y in thebook[i]:
            if y['ingredient_name'] in grocerylist.keys():
                valueupdate = y
                grocerylist.update({y['ingredient_name']: {'measure': y['measure'], 'quantity': ((valueupdate['quantity'] * person_count) + y['quantity']*person_count)}})
            else:
                grocerylist[y['ingredient_name']] = {'measure': y['measure'], 'quantity': (y['quantity'] * person_count)}

    return print(grocerylist)


if __name__ == "__main__":
    cookbook = init_cookbook()
    get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2, cookbook)
    get_shop_list_by_dishes(['Омлет', 'Омлет'], 3, cookbook)
