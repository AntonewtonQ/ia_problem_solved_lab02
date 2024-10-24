import numpy as np

# Função de desempenho para maximizar
def desempenho(x):
    x1, x2, x3 = x
    return 0.4 * x1 + 0.5 * (x2 ** 2) + 0.1 * (x3 ** 3)

# Algoritmo Random Search
def random_search(bounds, n_iterations):
    best_solution = None
    best_score = float('-inf')

    for i in range(n_iterations):
        # Gera uma solução aleatória dentro dos limites
        candidate = [np.random.uniform(low, high) for low, high in bounds]
        score = desempenho(candidate)

        # Verifica se a solução atual é melhor que a melhor solução encontrada
        if score > best_score:
            best_solution, best_score = candidate, score
            print(f'Iteração {i + 1}: Melhor solução atual: {best_solution}, com pontuação: {best_score}')

    return best_solution, best_score

# Definindo os limites para cada dimensão
bounds = [(10, 50), (1, 10), (1, 5)]  # Limites para x1, x2 e x3
n_iterations = 5000  # Número de iterações

# Executando o Random Search
best_solution, best_score = random_search(bounds, n_iterations)
print(f'Melhor solução encontrada: {best_solution}, com pontuação: {best_score}')
