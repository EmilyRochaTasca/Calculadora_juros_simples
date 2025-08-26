def calcular_juros_simples(capital_inicial: float, taxa_anual: float, tempo_anos: float) -> float:
    """
    Calcula o montante final de um investimento com base na fórmula de juros simples.

    M = C * (1 + (i * t)), onde i é a taxa em formato decimal (i/100).

    Args:
        capital_inicial (float): Valor do capital inicial (não-negativo).
        taxa_anual (float): Taxa de juros anual em percentual (não-negativo).
        tempo_anos (float): Tempo do investimento em anos (não-negativo).

    Returns:
        float: Montante final (capital + juros).

    Raises:
        ValueError: Se algum argumento for negativo.
        TypeError: Se algum argumento não for numérico.
    """
    # Validação de tipos
    if not all(isinstance(x, (int, float)) for x in (capital_inicial, taxa_anual, tempo_anos)):
        raise TypeError("Todos os parâmetros devem ser números (int ou float).")
    
    # Validação de valores
    if capital_inicial < 0 or taxa_anual < 0 or tempo_anos < 0:
        raise ValueError("O principal, a taxa e o tempo devem ser valores não-negativos.")
    
    # Cálculo do montante com juros simples
    montante = capital_inicial * (1 + (taxa_anual / 100) * tempo_anos)
    
    return montante

