sandwich_orders = ['pastrami','ruben','tuna','cheesestake','blt']
finished_sandwiches = []
while sandwich_orders:
    made_sandwich = sandwich_orders.pop()
    print('I made you a {} sandwich'.format(made_sandwich))
    finished_sandwiches.append(made_sandwich)
print(finished_sandwiches)