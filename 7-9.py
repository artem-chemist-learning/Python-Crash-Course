sandwich_orders = ['pastrami','pastrami','pastrami','ruben','tuna','cheesestake','blt']
finished_sandwiches = []
print('Sorry we are out of pastrami')
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
while sandwich_orders:
    made_sandwich = sandwich_orders.pop()
    print('I made you a {} sandwich'.format(made_sandwich))
    finished_sandwiches.append(made_sandwich)
print(finished_sandwiches)