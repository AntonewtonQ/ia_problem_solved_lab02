import numpy as np
import random

# Função para gerar uma matriz de distâncias aleatórias
def generate_locations(n):
    """Gera uma matriz de distâncias aleatórias para n localidades."""
    matrix = np.random.randint(10, 100, size=(n, n))
    np.fill_diagonal(matrix, 0)  # Distância de uma cidade para si mesma é 0
    return matrix

# Função de cálculo do custo da rota
def calculate_route_cost(route, distance_matrix):
    """Calcula o custo total de uma rota (tempo total de viagem)."""
    cost = sum(distance_matrix[route[i - 1], route[i]] for i in range(len(route)))
    return cost

# Função para gerar vizinhos (alterações na ordem da rota)
def generate_neighbors(solution):
    """Gera vizinhos trocando dois elementos da rota."""
    neighbors = []
    for i in range(len(solution)):
        for j in range(i + 1, len(solution)):
            neighbor = solution[:]
            neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
            neighbors.append(neighbor)
    return neighbors

# Algoritmo Hill Climbing
def hill_climbing(distance_matrix):
    """Executa o algoritmo Hill Climbing para minimizar o tempo total de uma rota."""
    n = len(distance_matrix)
    
    # Gera uma rota inicial aleatória
    current_solution = list(range(n))
    random.shuffle(current_solution)
    current_cost = calculate_route_cost(current_solution, distance_matrix)

    while True:
        # Gera todos os vizinhos da solução atual
        neighbors = generate_neighbors(current_solution)
        best_neighbor, best_neighbor_cost = None, float('inf')

        # Avalia o custo de cada vizinho
        for neighbor in neighbors:
            cost = calculate_route_cost(neighbor, distance_matrix)
            if cost < best_neighbor_cost:
                best_neighbor, best_neighbor_cost = neighbor, cost

        # Se nenhum vizinho for melhor, para o algoritmo
        if best_neighbor_cost >= current_cost:
            break

        # Atualiza a solução atual para o melhor vizinho
        current_solution, current_cost = best_neighbor, best_neighbor_cost
        print(f'Melhor solução atual: {current_solution} com custo: {current_cost}')

    return current_solution, current_cost

# Definir o número de localidades
n_locations = 6

# Gerar uma matriz de distâncias aleatórias para as localidades
distance_matrix = generate_locations(n_locations)

# Exibir a matriz de distâncias gerada
print("Matriz de distâncias entre localidades:")
print(distance_matrix)

# Executar o algoritmo Hill Climbing
best_route, best_cost = hill_climbing(distance_matrix)

# Exibir a melhor rota encontrada e o custo total
print(f'\nMelhor rota encontrada: {best_route} com custo total: {best_cost}')
