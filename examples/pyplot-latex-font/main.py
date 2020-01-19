import matplotlib.pyplot as plt
import random

# Drawing without using latex font.
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot([i for i in range(10)], [random.random() for i in range(10)])
ax.set_xlabel('Not using latex font')
ax.set_ylabel('Not using latex font')
fig.savefig('non-latex-font.pdf', bbox_inches="tight", pad_inches=0.05)

# Parameters to use latex font.
# Note that there might be other ways to do this.
plt.rcParams['ps.useafm'] = True
plt.rcParams['pdf.use14corefonts'] = True
plt.rcParams['text.usetex'] = True
plt.rcParams['font.family'] = "serif"
plt.rcParams['font.serif'] = "Times"

# Drawing using latex font.
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot([i for i in range(10)], [random.random() for i in range(10)])
ax.set_xlabel('Using latex font')
ax.set_ylabel('Using latex font')
fig.savefig('latex-font.pdf', bbox_inches="tight", pad_inches=0.05)
