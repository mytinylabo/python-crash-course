import matplotlib.pyplot as plt

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.jet, s=10)

# https://matplotlib.org/3.1.1/gallery/color/colormap_reference.html

# Set chart title and label axes.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set size of tick labels.
ax.tick_params(axis='both', which='major', labelsize=14)
ax.ticklabel_format(axis='both', style='plain')

# Set the range for each axis.
ax.axis([0, len(x_values) * 1.1, 0, y_values[-1] * 1.1])

plt.show()
# plt.savefig('squares_plot.png', bbox_inches='tight')
