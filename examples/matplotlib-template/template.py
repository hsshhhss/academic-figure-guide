# Import deepcopy for copying data structures
from copy import deepcopy
import numpy as np
import matplotlib.pyplot as plt
import random       # Just for demo purpose

'''
Style elements
    Here we can setup a drawing style for each algorithm.
    This helps to make the drawing style of an algorithm consistent.
'''
defaultStyle = {
    'label' : 'default',    # The name of the algorithm
    'ls' : '-',             # Line style, '-' means a solid line
    'linewidth' : 1,        # Line width
    'color' : 'k',          # Line color, 'k' means color
    'zorder' : 100,         # The 'height' of the plot. 
                            # Affects whether items are in the front of / behind each other.
    # You can add more style items here, e.g., markers.
}
# Here, we setup the style for an algorithm. Let's call it Alg.1.
alg1Style = deepcopy(defaultStyle)          # First copy all default styles.
alg1Style['label'] = r'\textsc{Optimal}'    # Setup algorithm name. 
                                            # We use \textsc here which is a latex command. 
                                            # This is fine since we use latex to generate text.
alg1Style['color'] = 'tab:orange'           # Customized line color
                                            # https://matplotlib.org/3.1.0/gallery/color/named_colors.html
# Another algorithm
alg2Style = deepcopy(defaultStyle)
alg2Style['label'] = r'\textsc{Greedy}'
alg2Style['color'] = 'tab:green'

''' Some global variables '''
FIGURE_SIZE = (3.45, 1.85)      # Figure width and height. 
                                # This is a good value for 2-column paper.
FONT_SIZE = 8                   # Size of text
LEGEND_FONT_SIZE = 7            # We might need different font sizes for different text

''' 
Parameters for legend to better utilize space.
'''
plt.rcParams["legend.labelspacing"] = 0.2
plt.rcParams["legend.handlelength"] = 1.75
plt.rcParams["legend.handletextpad"] = 0.5
plt.rcParams["legend.columnspacing"] = 0.75

plt.rcParams.update({'figure.autolayout': True})

'''
Use latex to generate text
Note that these params usually make the code slow. If you want to preview the figure without generating latex text, feel free to comment these. 
'''
plt.rcParams['ps.useafm'] = True
plt.rcParams['pdf.use14corefonts'] = True
plt.rcParams['text.usetex'] = True
plt.rcParams['font.family'] = "serif"
plt.rcParams['font.serif'] = "Times"

''' The real drawing part starts here. '''
# Put your data over here.
x = [i for i in range(10, 100, 10)]
alg1ComputationTime = [2**i for i in range(1, 10)]
alg2ComputationTime = [10 * i for i in range(1, 10)]
alg1StdDev = [random.random() * i * 2 for i in range(1, 10)]
alg2StdDev = [random.random() * i * 2 for i in range(1, 10)]
# Start to create the figure
fig = plt.figure(figsize = FIGURE_SIZE)
ax = fig.add_subplot(111)
ax.plot(x, alg1ComputationTime, **alg1Style)
ax.plot(x, alg2ComputationTime, **alg2Style)
ax.errorbar(x, alg1ComputationTime, yerr = alg1StdDev, color = alg1Style['color'], capsize = 2, ls = 'none', markeredgewidth = 1, elinewidth = 1)
ax.errorbar(x, alg2ComputationTime, yerr = alg2StdDev, color = alg2Style['color'], capsize = 2, ls = 'none', markeredgewidth = 1, elinewidth = 1)
# Set x and y label. We use latex to generate text
ax.set_xlabel(r"Number of Robots $(n)$", fontsize = FONT_SIZE)
ax.set_ylabel("Computation Time (s)", fontsize = FONT_SIZE)
ax.tick_params(labelsize = FONT_SIZE)
ax.legend(fontsize = LEGEND_FONT_SIZE, ncol = 2)
ax.set_yscale("log")
ax.yaxis.grid(True, alpha = 0.8)
# Directly save the figure to a file.
fig.savefig("result-computation-time.pdf", bbox_inches="tight", pad_inches=0.05)
plt.cla()

''' Another bar chart. '''
# Put your data over here.
x = np.array([i for i in range(10, 100, 10)])
alg1OptimalityRatio = [1 for i in range(1, 10)]
alg2OptimalityRatio = [0.1 * i + 1 for i in range(1, 10)]
# Start to create the figure
fig = plt.figure(figsize = FIGURE_SIZE)
ax = fig.add_subplot(111)
bar_width = 3
ax.bar(x - bar_width / 2, alg1OptimalityRatio, bar_width, edgecolor = 'black', **alg1Style)
ax.bar(x + bar_width / 2, alg2OptimalityRatio, bar_width, edgecolor = 'black', **alg2Style)
ax.set_xticks(x)
ax.set_xlabel(r"Number of Robots $(n)$", fontsize = FONT_SIZE)
ax.set_ylabel("Optimality Ratio", fontsize = FONT_SIZE)
ax.tick_params(labelsize = FONT_SIZE)
ax.legend(fontsize = LEGEND_FONT_SIZE, ncol = 2)
ax.yaxis.grid(True, alpha = 0.8)
# Directly save the figure to a file.
fig.savefig("result-optimality-ratio.pdf", bbox_inches="tight", pad_inches=0.05)
plt.cla()