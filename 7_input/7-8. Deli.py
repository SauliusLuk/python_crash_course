sandwich_orders = ['nr1', 'nr2', 'nr3', 'nr4']
finished_sandwiches = []

while sandwich_orders:
    finished_sandwich = sandwich_orders.pop()
    print(f"making sandwich {finished_sandwich}")
    finished_sandwiches.append(finished_sandwich)

for sandwich in finished_sandwiches:
    print(f"finished making sandwich {sandwich}")