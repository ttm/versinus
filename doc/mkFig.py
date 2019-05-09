import pylab as p, numpy as n

fig=p.figure(figsize=(6.,4.))
p.xlim(0,1)
p.ylim(0,1)

xmargin = 0.1
amp = 0.7
offset = 0.1
x = n.linspace(0+xmargin, 0.5, 1000)
y = 0.5 + 0.5 * amp * n.sin(n.linspace(0, n.pi, 1000)) - offset
p.plot(x, y, label='hubs')

p.annotate('', (1-xmargin, 0.2), (1, 0.2), ha="center", va="center", arrowprops=dict(arrowstyle="|-|"))
p.annotate(r'$\mu$', (0.94, 0.22), fontsize=14)

# p.arrow(0.1, 0.7, 0.1, 0.2, arrowprops=dict(arrowstyle="|-|"))
p.annotate('', (0.05, y.max()), (0.05, y.min()), ha="center", va="center", arrowprops=dict(arrowstyle="|-|"))
p.annotate(r'$\alpha$', (0.07, y.max()*0.75), fontsize=14)

p.annotate('', (0.2, 0.5), (0.2, y.min()), ha="center", va="center", arrowprops=dict(arrowstyle="|-|"))
p.annotate(r'$\Delta$', (0.22, 0.43), fontsize=14)

x = n.linspace(0.5, 1-xmargin, 1000)
y = 0.5 + 0.5 * amp * n.sin(n.linspace(n.pi, 2*n.pi, 1000)) - offset
p.plot(x, y, label='intermediary')

x0, y0 = 0.8, 0.6
x1, y1 = 0.4, 0.9

xx = n.linspace(x0, x1, 100)
yy = n.linspace(y0, y1, 100)
ax = p.plot(xx, yy, label='periphery')

p.annotate(r'$(x_0, y_0)$', (x0, y0+.02), fontsize=14)
p.annotate(r'$(x_1, y_1)$', (x1-0.02, y1+0.02), fontsize=14)

p.xticks([0, 0.5, 1])
p.yticks([0, 0.5, 1])
p.legend()

p.title("Placement of nodes in Versinus", fontsize=16)

p.subplots_adjust(left=0.06, bottom=0.06, right=0.97, top=0.93)

p.savefig("./nodePositioning.png")
# p.show()
