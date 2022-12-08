import matplotlib.pyplot as plt

x = []
y = []
for line in open('s.txt', 'r'):
    lines = [i for i in line.split()]
    x.append(float(lines[0]))
    y.append(float(lines[1]))
      
plt.title("Semiconductor")
plt.xlabel('Temperature')
plt.ylabel('Ohm')
yaxis = range(0, 3000, 100)
plt.yticks(yaxis)
plt.plot(x, y, marker = 'o', c = 'b') 
plt.show()

