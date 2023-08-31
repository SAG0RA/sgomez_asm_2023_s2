import sympy as sp

def complex_integral(a):
    z = sp.symbols('z')
    integrand = sp.exp(a*z) / (z**2 + 1)
    
    # Encontrar los residuos en los puntos singulares
    singular_points = [sp.I, -sp.I]
    residues = []
    for point in singular_points:
        residue = sp.limit((z - point) * integrand, z, point)
        residues.append(residue)
    
    integral_value = 2 * sp.pi * sum(residues)
    return integral_value

a_value = 2.0
result = complex_integral(a_value)
simplified_result = sp.simplify(result)
print("El valor de la integral simplificado es:", simplified_result)
print("El valor de la integral compleja es:", result)