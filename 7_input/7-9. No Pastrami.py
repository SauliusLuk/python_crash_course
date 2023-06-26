sandwich_orders = ['nr1', 'pastrami', 'nr2','pastrami', 'nr3','pastrami', 'nr4']
finished_sandwiches = []

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
print("sorry, out of pastrami")

while sandwich_orders:
    finished_sandwich = sandwich_orders.pop()
    print(f"making sandwich {finished_sandwich}")
    finished_sandwiches.append(finished_sandwich)

for sandwich in finished_sandwiches:
    print(f"finished making sandwich {sandwich}")