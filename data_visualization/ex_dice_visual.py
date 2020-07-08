from functools import reduce
import operator
import sys

from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

dice_set = list([Die(int(n)) for n in sys.argv[1].split(',')])
n_rolls = int(sys.argv[2])
ope = sys.argv[3]  # 's'um or 'm'ultiply
print(f"{dice_set}, {n_rolls}, {ope}")

# Make some rolls, and store results in a list.
results = []
for roll_num in range(n_rolls):
    rolls = [d.roll() for d in dice_set]
    if ope == 's':
        result = sum(rolls)
    else:
        result = reduce(operator.mul, rolls, 1)
    results.append(result)

# Analyze the results.
min_result = len(dice_set) if ope == 's' else 1
max_result = sum([d.num_sides for d in dice_set]) if ope == 's' else reduce(operator.mul, [d.num_sides for d in dice_set], 1)
frequencies = list([results.count(v) for v in range(min_result, max_result + 1)])

# Visualize the results.
x_values = list(range(min_result, max_result + 1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': "Result", 'dtick': 1}
y_axis_config = {'title': "Fequency of Result"}
dice_str = ', '.join([str(d) for d in dice_set])

my_layout = Layout(title=f"Results of rolling {dice_str} {n_rolls} times",
                   xaxis=x_axis_config, yaxis=y_axis_config)
filename = dice_str = '_'.join([str(d).lower() for d in dice_set]) + f'_{n_rolls}_{ope}.html'
offline.plot({'data': data, 'layout': my_layout}, filename=f'/mnt/f/tmp/{filename}')
