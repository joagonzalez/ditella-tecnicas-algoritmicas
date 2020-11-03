# Versión recursiva (exponencial).
def ED_rec(s, t):
    if len(s)==0:
        res = len(t)
    elif len(t)==0:
        res = len(s)
    else:
        d1 = ED_rec(s, t[:-1])
        d2 = ED_rec(s[:-1], t)

        if s[-1] == t[-1]:
            d3 = ED_rec(s[:-1], t[:-1])
            res = min(d1+1, d2+1, d3)
        else:
            res = min(d1+1, d2+1)
    return res
    
# Versión iterativa con programación dinámica (polinomial).
def ED_iter(s, t):
    # Construyo una matriz de len(s)+1 x len(t)+1:
    # 0 1 2 3 ... 
    # 1 _ _ _
    # 2 _ _ _
    # 3 _ _ _
    # ...
    m = []
    m.append(list(range(len(t)+1)))
    for i in range(1, len(s)+1):
        m.append([i] + [0]*len(t))
    # Algoritmo principal:
    for i in range(1, len(s)+1):
        for j in range(1, len(t)+1):
            d1 = m[i][j-1]
            d2 = m[i-1][j]
            if s[i-1] == t[j-1]: 
                d3 = m[i-1][j-1]
                m[i][j] = min(d1+1, d2+1, d3)
            else:
                m[i][j] = min(d1+1, d2+1)
    return m[len(s)][len(t)]

#####################################################################

if __name__ == "__main__":
    # Algunos ejemplos:
    for (s1,s2) in [("agua", "gota"), 
                    ("algoritmos", "universidad"),
                    ("algoritmos", "programas"), 
                    ("manzana", "naranja"),
                    ("manzanaaaaaaaaa", "naranjaaaaaaaaa")]:
        print(s1, s2)
        print("dinámica:", ED_iter(s1, s2))
        print("recursiva:", ED_rec(s1, s2))
        print()
        # En el último ejemplo, la versión dinámica termina inmediatamente,
        # y la recursiva demora una eternidad.

