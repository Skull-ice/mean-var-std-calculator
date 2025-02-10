import numpy as np

def calculate(liste):
    if len(liste) != 9:
        raise ValueError("La liste doit contenir neuf nombres.")
    
    matrice = np.array(liste).reshape(3, 3)
    
    resultats = {
        'mean': [matrice.mean(axis=0).tolist(), matrice.mean(axis=1).tolist(), matrice.mean()],
        'variance': [matrice.var(axis=0).tolist(), matrice.var(axis=1).tolist(), matrice.var()],
        'standard deviation': [matrice.std(axis=0).tolist(), matrice.std(axis=1).tolist(), matrice.std()],
        'max': [matrice.max(axis=0).tolist(), matrice.max(axis=1).tolist(), matrice.max()],
        'min': [matrice.min(axis=0).tolist(), matrice.min(axis=1).tolist(), matrice.min()],
        'sum': [matrice.sum(axis=0).tolist(), matrice.sum(axis=1).tolist(), matrice.sum()]
    }
    
    return resultats
