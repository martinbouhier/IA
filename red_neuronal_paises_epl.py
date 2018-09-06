from sklearn.linear_model import Ridge
f = [
    ['Pais', 'Fecha', 'Impresionessubastadas', 'Impresionesvendidasensubasta', 'FillratedeExchange', 'eCPM', 'Importeacobraraanunciantes'],
    ['Chile', '20/07/2018', 22455429, 253138, 1.13, 0.43, 109.43],
    ['Chile', '21/07/2018', 30792068, 583513, 1.90, 0.41, 237.02],
    ['Chile', '22/07/2018', 34802498, 819304, 2.35, 0.45, 366.38],
    ['Chile', '23/07/2018', 8414584, 319570, 3.80, 0.47, 151.55],
    ['Chile', '24/07/2018', 2894132, 81911, 2.83, 0.41, 33.59],
    ['Chile', '25/07/2018', 27055525, 610123, 2.26, 0.40, 243.44],
    ['Chile', '26/07/2018', 36358833, 1055481, 2.90, 0.42, 446.76],
    ['Chile', '27/07/2018', 32085418, 857084, 2.67, 0.40, 345.54],
    ['Chile', '28/07/2018', 28045848, 702096, 2.50, 0.40, 278.89],
    ['Chile', '29/07/2018', 33754167, 754720, 2.24, 0.41, 310.65],
    ['Chile', '30/07/2018', 16416652, 572633, 3.49, 0.43, 248.56],
    ['Chile', '31/07/2018', 31756107, 867152, 2.73, 0.39, 336.63],
    ['Chile', '01/08/2018', 37659179, 643388, 1.71, 0.48, 308.03],
    ['Chile', '02/08/2018', 37685752, 1226572, 3.25, 0.34, 421.65],
    ['Chile', '03/08/2018', 33003477, 1468489, 4.45, 0.32, 475.87],
    ['Chile', '04/08/2018', 29194171, 1029454, 3.53, 0.32, 324.55],
    ['Chile', '05/08/2018', 35091360, 1250191, 3.56, 0.28, 350.43],
    ['Chile', '06/08/2018', 43738176, 1596689, 3.65, 0.28, 441.07],
    ['Chile', '07/08/2018', 41061277, 1352974, 3.30, 0.27, 362.29],
    ['Chile', '08/08/2018', 37878192, 1247150, 3.29, 0.26, 328.87],
    ['Chile', '09/08/2018', 35021103, 1272523, 3.63, 0.30, 386.54],
    ['Chile', '10/08/2018', 29042834, 861105, 2.96, 0.52, 446.26],
    ['Chile', '11/08/2018', 28488558, 855876, 3.00, 0.51, 436.60],
    ['Chile', '12/08/2018', 33419362, 854613, 2.56, 0.49, 418.32],
    ['Chile', '13/08/2018', 40618450, 854154, 2.10, 0.49, 420.14],
    ['Chile', '17/08/2018', 25641467, 642191, 2.50, 0.48, 310.68],
    ['Chile', '18/08/2018', 29581445, 829795, 2.81, 0.50, 414.18],
    ['Chile', '19/08/2018', 33930741, 852027, 2.51, 0.50, 423.21],
    ['Chile', '20/08/2018', 39733540, 995573, 2.51, 0.50, 495.87],
    ['Chile', '21/08/2018', 37933207, 916393, 2.42, 0.48, 435.74],
    ['Chile', '22/08/2018', 38222307, 875518, 2.29, 0.46, 405.85],
    ['Chile', '23/08/2018', 37836237, 800629, 2.12, 0.46, 367.95],
    ['Chile', '24/08/2018', 20340295, 718211, 3.53, 0.47, 340.84],
    ['Chile', '25/08/2018', 8699283, 565356, 6.50, 0.52, 296.31],
    ['Chile', '26/08/2018', 10571791, 643269, 6.08, 0.53, 344.09],
    ['Chile', '27/08/2018', 13390425, 490242, 3.66, 0.48, 235.59],
    ['Chile', '28/08/2018', 12132686, 755954, 6.23, 0.47, 357.58],
    ['Chile', '29/08/2018', 1661177, 122284, 7.36, 0.50, 61.23],
    ['Chile', '02/09/2018', 1004812, 51886, 5.16, 0.44, 22.78],
    ['Chile', '03/09/2018', 11866892, 593646, 5.00, 0.48, 286.53],
    ['Chile', '04/09/2018', 11658096, 752307, 6.45, 0.60, 450.87]
    ]

a = []
b = []
max_sub = []
max_imp = []
max_fill = []
max_eCPM = []

for item in f[1:]:
    a_pre = []
    a_pre.append(float(item[2]))
    a_pre.append(float(item[3]))
    a_pre.append(float(item[4]))
    a_pre.append(float(item[5]))
    max_sub.append(int(item[2]))
    max_imp.append(int(item[3]))
    max_fill.append(float(item[4]))
    max_eCPM.append(float(item[5]))
    a.append(a_pre)
    b.append(float(item[6]))

max_sub = max(max_sub)
max_imp = max(max_imp)
max_fill = max(max_fill)
max_eCPM = max(max_eCPM)
max_rev = max(b)

for item in f[1:]:
    if float(item[2]) == float(max_sub):
        print ('Mayor volumen subastado: ', item)
    if float(item[3]) == float(max_imp):
        print ('Mayor volumen de impresiones vendidas: ', item)
    if float(item[4]) == float(max_fill):
        print ('Mayor fillrate: ', item)
    if float(item[5]) == float(max_eCPM):
        print ('Mayor eCPM: ', item)
    if float(item[6]) == float(max_rev):
        print ('Mejor resultado en cuanto al revenue: ', item)

X_train, y_train = a, b
ridge = Ridge(alpha=0.01)
ridge.fit(X_train, y_train)
print(ridge.score(X_train, y_train))

print ('Subastas buscadas:')
sub_predict = int(input())
print ('Impresiones buscadas:')
imp_predict = int(input())
fill_dado = (imp_predict / sub_predict) * 100
print('Fillrate:', fill_dado)
print ('eCPM buscado:')
ecpm_predict = float(input())

print (ridge.predict([[sub_predict, imp_predict, fill_dado, ecpm_predict]]))
