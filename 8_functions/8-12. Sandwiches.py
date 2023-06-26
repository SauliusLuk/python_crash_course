def sandwich_order(bread, *other_ingredients):
    print(f"you ordered {bread} bread sandwich with the following ingredients: ")
    for ingredient in other_ingredients:
        print(f" - {ingredient}")

sandwich_order('white','tomato', 'cheese', 'chicken' )
sandwich_order('rye','tomato', 'cheese', 'chicken', 'sausage' )
sandwich_order('cheesey','tomato', 'cheese', 'meatballs' )