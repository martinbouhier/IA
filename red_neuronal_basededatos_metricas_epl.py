from sklearn.linear_model import Ridge
f = [
    [0.063807299, 0.71, 0.00071],
    [0.363262854, 0.7, 0.0007],
    [0.836344317, 0.76, 0.00076],
    [0.336103886, 0.76, 0.00076],
    [0.127633903, 0.73, 0.00073],
    [0.986579617, 0.71, 0.00071],
    [0.445450826, 0.7, 0.0007],
    [0.144177017, 0.7, 0.0007],
    [0.284048802, 0.69, 0.00069],
    [0.683907029, 0.7, 0.0007],
    [0.653624485, 0.68, 0.00068],
    [0.044176352, 0.65, 0.00065],
    [0.831671683, 0.64, 0.00064],
    [0.292267367, 0.69, 0.00069],
    [0.244431077, 0.72, 0.00072],
    [0.50348495, 0.73, 0.00073],
    [0.817789834, 0.73, 0.00073],
    [0.856153496, 0.84, 0.00084],
    [0.188464484, 0.78, 0.00078],
    [0.903924038, 0.83, 0.00083],
    [0.516154451, 0.78, 0.00078],
    [0.944829869, 0.85, 0.00085],
    [0.280341871, 0.94, 0.00094],
    [0.190681793, 0.75, 0.00075],
    [0.112015525, 0.72, 0.00072],
    [0.288403567, 0.78, 0.00078],
    [0.269064777, 0.76, 0.00076],
    [0.086968092, 0.77, 0.00077],
    [0.806376116, 0.8, 0.0008],
    [0.538766092, 0.77, 0.00077],
    [0.664144927, 0.8, 0.0008],
    [0.521777437, 0.88, 0.00088],
    [0.816880703, 0.81, 0.00081],
    [0.571129772, 0.75, 0.00075],
    [0.416371307, 0.73, 0.00073],
    [0.872382387, 0.7, 0.0007],
    [0.210141392, 0.68, 0.00068],
    [0.703326289, 0.69, 0.00069],
    [0.007648223, 0.72, 0.00072],
    [0.499602575, 0.74, 0.00074],
    [0.967991252, 0.72, 0.00072],
    [0.60928689, 0.74, 0.00074],
    [0.629853836, 0.75, 0.00075],
    [0.886280518, 0.72, 0.00072],
    [0.992303883, 0.66, 0.00066],
    [0.056925278, 0.75, 0.00075],
    [0.178939496, 0.74, 0.00074],
    [0.931377667, 0.79, 0.00079],
    [0.213079036, 0.53, 0.00053],
    [0.47595793, 0.59, 0.00059],
    [0.219267408, 0.68, 0.00068],
    [0.741663754, 0.67, 0.00067],
    [0.586605533, 0.73, 0.00073],
    [0.575224125, 0.68, 0.00068],
    [0.782370081, 0.62, 0.00062],
    [0.588968327, 0.54, 0.00054],
    [0.882564657, 0.64, 0.00064],
    [0.252962731, 0.64, 0.00064],
    [0.317659358, 0.63, 0.00063],
    [0.045080755, 0.67, 0.00067],
    [0.879335705, 0.89, 0.00089],
    [0.764499171, 0.76, 0.00076],
    [0.255836358, 0.63, 0.00063],
    [0.289318861, 0.77, 0.00077],
    [0.589157784, 0.69, 0.00069],
    [0.087372583, 0.62, 0.00062],
    [0.890619974, 0.72, 0.00072],
    [0.689306468, 0.71, 0.00071],
    [0.885276279, 0.71, 0.00071],
    [0.116117407, 0.69, 0.00069],
    [0.001135891, 0.73, 0.00073],
    [0.925594912, 0.7, 0.0007],
    [0.474350089, 0.7, 0.0007],
    [0.658211188, 0.75, 0.00075],
    [0.859772973, 0.7, 0.0007],
    [0.286321224, 0.67, 0.00067],
    [0.466581333, 0.81, 0.00081],
    [0.189701632, 0.75, 0.00075],
    [0.62036663, 0.76, 0.00076],
    [0.268631623, 0.72, 0.00072],
    [0.661042753, 0.65, 0.00065],
    [0.35519695, 0.64, 0.00064],
    [0.402748284, 0.59, 0.00059],
    [0.407924552, 0.61, 0.00061],
    [0.395775781, 0.84, 0.00084],
    [0.448907609, 0.91, 0.00091],
    [0.875554466, 0.59, 0.00059],
    [0.034988721, 0.7, 0.0007],
    [0.432142543, 0.68, 0.00068],
    [0.339030273, 0.81, 0.00081],
    [0.837996122, 0.82, 0.00082],
    [0.433927894, 0.7, 0.0007],
    [0.36491913, 0.82, 0.00082],
    [0.865771905, 0.74, 0.00074],
    [0.41061821, 0.88, 0.00088],
    [0.816034189, 0.82, 0.00082]
]

a = []
b = []

for item in f:
    a_pre = []
    a_pre.append(float(item[0]))
    a_pre.append(float(item[1]))
    a.append(a_pre)
    b.append(float(item[2]))

X_train, y_train = a, b
ridge = Ridge(alpha=.5)
ridge.fit(X_train, y_train)
ridge.score(X_train, y_train)
ridge.predict([[1, 1]])