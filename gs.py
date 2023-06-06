#her defineres de vektorer, man vil køre gram-schmidt på.
original_basis = [[1,0,1],[5,1,1],[4,-1,0]]


def inner_product(v,u):
    #her defineres det indre produkt. Her er f.eks. det indre produkt fra 2019 august
    return v[0] * u[0] + 4 * v[1] * u[1] + 3 * v[2] * u[2]

def norm(v):
    return inner_product(v,v) ** 0.5

def gram_schmidt(vectors):
    orthonormal_basis = []
    for i in range(len(vectors)):
        v = vectors[i]

        if i == 0:
            u = []

            for coordinate in enumerate(v):
                u.append((1 / norm(v)) * v[coordinate[0]])

            orthonormal_basis.append(u)
            print_u(u,i+1)
        else:
            p = [0,0,0]

            for j in range(i):
                for k in range(len(p)):
                    p[k] += inner_product(v,orthonormal_basis[j]) * orthonormal_basis[j][k]
            print_p(p,i)

            u = []
            v_p = []

            for q in range(len(v)):
                v_p.append(v[q]-p[q])

            for k in range(len(v)):
                u.append((1 / norm(v_p)) * v_p[k])

            orthonormal_basis.append(u)
            print_u(u,i+1)

    return orthonormal_basis

def print_u(u,i):
    for j in range(len(u)):
        if u[j] < 0.0001 and u[j] > -0.0001:
            u[j] = 0
        else:
            u[j] = round(u[j],10)
            
    print("Vector " + str(i) + " in the orthonormal basis is equal to " +
          str(u) + ".\n")  

def print_p(p,i):
    for j in range(len(p)):
        if p[j] < 0.0001 and p[j] > -0.0001:
            p[j] = 0
        else:
            p[j] = round(p[j],10)

    print("p_" + str(i) + " is equal to " +
          str(p) + ".\n")  


gram_schmidt(original_basis)