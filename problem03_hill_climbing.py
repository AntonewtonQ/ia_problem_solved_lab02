import random

# Matriz de distâncias entre as cidades
distance_matrix = [
    [0, 10, 15, 20, 25],
    [10, 0, 35, 25, 30],
    [15, 35, 0, 30, 20],
    [20, 25, 30, 0, 15],
    [25, 30, 20, 15, 0]
]

# Função para calcular o custo total de uma rota
def calculate_route_cost(route, distance_matrix):
    """Calcula o custo total de uma rota (distância total)."""
    cost = sum(distance_matrix[route[i - 1]][route[i]] for i in range(len(route)))
    cost += distance_matrix[route[-1]][route[0]]  # Retorno à cidade inicial
    return cost

# Função para gerar vizinhos trocando pares de cidades na rota
def generate_neighbors(route):
    """Gera todas as rotas vizinhas trocando dois pontos de posição."""
    neighbors = []
    for i in range(len(route)):
        for j in range(i + 1, len(route)):
            neighbor = route[:]
            neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
            neighbors.append(neighbor)
    return neighbors

# Algoritmo Hill Climbing
def hill_climbing(distance_matrix):
    """Executa o algoritmo Hill Climbing para minimizar a distância total de uma rota."""
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

# Executa o algoritmo
best_route, best_cost = hill_climbing(distance_matrix)
print(f'Rota ótima encontrada: {best_route} com custo total de: {best_cost}')
