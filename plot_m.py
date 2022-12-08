import matplotlib.pyplot as plt
  
x = []
y = []
for line in open('m.txt', 'r'):
    lines = [i for i in line.split()]
    x.append(float(lines[0]))
    y.append(float(lines[1]))
      
plt.title("Metall")
plt.xlabel('Temperature')
plt.ylabel('Ohm')
plt.yticks([19.000, 19.500, 20.000, 20.500, 21.000, 21.500, 22.000, 22.500, 23.000, 23.500, 24.000, 24.500, 25.000, 25.500, 26.000, 26.500, 27.000])
plt.plot(x, y, marker = 'o', c = 'g') 
plt.show()
