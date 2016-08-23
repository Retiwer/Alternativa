# -*- coding: utf-8 -*-
"""
Created on Mon Aug 22 09:27:11 2016

@author: Carlos
"""

import T
import matplotlib.colors as colors

Paises = ['Bolivia','Ecuador','Francia','Japon','SriLanka','USA']

wb = openpyxl.load_workbook('/Test/F844C800.xlsx')  #Abrir el archivo Excel
sheet = wb.get_sheet_by_name('Hoja2')  

Tabla, new_list2 = Port()
Dim = 2
Ind, aux = np.unique(new_list2, return_counts=True)
print 'Paises'
print Ind
print ''

print "Cantidad de Elementos de la Tabla Principal"
print Tabla.shape
print ''


min_max_scaler = preprocessing.MinMaxScaler()
X_train_minmax = min_max_scaler.fit_transform(Tabla)*10
Tabla = preprocessing.normalize(X_train_minmax, norm='l2')

n_components = Dim    #Parametros de dimension del TSNE
n_neighbors = 10    #Parametros minimos TSNE
tsne = manifold.TSNE(n_components=n_components, init='pca', random_state=0)
mds = manifold.MDS(n_components=n_components, random_state=0)

z=3
kmeans = KMeans(n_clusters=z)
kmeans.fit(Tabla)

cluster_centers = kmeans.cluster_centers_
labels = kmeans.labels_
n_clusters_ = len(np.unique(labels))
Combinadas = armar(Tabla, cluster_centers)
Desdoblada = tsne.fit_transform(Combinadas)
g, h = desarmar(Desdoblada, n_clusters_)
Var = TaC(new_list2)

Ind, aux = np.unique(labels, return_counts=True)
print 'Clusters'
print aux
print ''

plt.figure()
plt.scatter(g[:, 0], g[:, 1], c=Var)
#plt.scatter(g[:, 0], g[:, 1], c=labels)

for i in range(len(h)):
    plt.plot(h[i][0], h[i][1], c='r', marker='x', markersize = 15)

l=0
Matrix = [[0 for x in range(390)] for y in range(6)]
for j in range(6):
    for i in range(390):
        Matrix[j][i] = labels[l]
        l=l+1


OP = [[0 for x in range(3)] for y in range(6)] 

M0, aux0 = np.unique(Matrix[0][:], return_counts=True)
OP[0][:]=aux0

M0, aux0 = np.unique(Matrix[1][:], return_counts=True)
OP[1][:]=aux0

M0, aux0 = np.unique(Matrix[2][:], return_counts=True)
OP[2][:]=aux0

M0, aux0 = np.unique(Matrix[3][:], return_counts=True)
OP[3][:]=aux0

M0, aux0 = np.unique(Matrix[4][:], return_counts=True)
OP[4][:]=aux0

M0, aux0 = np.unique(Matrix[5][:], return_counts=True)
OP[5][:]=aux0        

print 'Clusters por Paises'
print OP
print ''

Dis = [[0 for x in range(6)] for y in range(6)] 
for i in range(6):
    for j in range(6):
        Dis[i][j] = vector(OP[i][0],OP[j][0],OP[i][1],OP[j][1],OP[i][2],OP[j][2])

print 'Distancias por Paises'
print Dis
print ''

#min_max_scaler = preprocessing.MinMaxScaler()
#Dis = min_max_scaler.fit_transform(Dis)*255

#print 'Distancias por Paises Escaladas a 255'
#print Dis
#print ''

for j in range(len(Paises)):
    Label(text=Paises[j], relief=RIDGE,width=15).grid(row=j+1,column=0)
    Label(text=Paises[j], relief=RIDGE,width=15).grid(row=0,column=j+1)

p=0
for i in range(1,len(Paises)+1,1):
    for j in range(1,len(Paises)+1,1):
        Label(text=("%.1f" % Dis[i-1][j-1]), bg=colors.rgb2hex((Dis[i-1][j-1], Dis[i-1][j-1], Dis[i-1][j-1])), relief=RIDGE,width=15).grid(row=i,column=j)

mainloop()
