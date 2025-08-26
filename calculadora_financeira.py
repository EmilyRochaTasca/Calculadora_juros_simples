"""
Módulo para cálculos financeiros básicos.
"""

def calcular_juros_simples(capital_inicial: float, taxa_anual: float, tempo_anos: float) -> float:
    """
    Calcula o montante final de um investimento com base na fórmula de juros simples.

    Esta função aplica a taxa de juros sobre o capital inicial durante o
    período especificado e retorna a soma do capital com os juros acumulados.

    A fórmula utilizada é: M = C * (1 + (i * t)), onde:
      - M = Montante final
      - C = Capital inicial
      - i = Taxa de juros (em formato decimal)
      - t = Tempo

    Args:
        capital_inicial (float): O valor do capital inicial a ser investido.
            Ex: 1000.00
        taxa_anual (float): A taxa de juros anual em formato percentual.
            Ex: 5 para 5%
        tempo_anos (float): O período do investimento, em anos. Pode ser fracionado.
            Ex: 2.5 para dois anos e meio.

    Returns:
        float: O montante final (capital + juros), arredondado para 2 casas decimais.

    Raises:
        ValueError: Se qualquer um dos argumentos (capital, taxa, tempo)
            for um valor negativo.

    Example:
        >>> calcular_juros_simples(1000.00, 5.0, 2.0)
        1100.00
        >>> calcular_juros_simples(2500.00, 3.5, 10.0)
        3375.00
    """
      # Validação de tipos: apenas int ou float
    if not isinstance(capital_inicial, (int, float)):
        raise TypeError("Todos os parâmetros devem ser números (int ou float).")
    if not isinstance(taxa_anual, (int, float)):
        raise TypeError("Todos os parâmetros devem ser números (int ou float).")
    if not isinstance(tempo_anos, (int, float)):
        raise TypeError("Todos os parâmetros devem ser números (int ou float).")

    # Validação de valores não-negativos
    if capital_inicial < 0 or taxa_anual < 0 or tempo_anos < 0:
        raise ValueError("O principal, a taxa e o tempo devem ser valores não-negativos.")

    # Cálculo do montante com juros simples
    montante = capital_inicial * (1 + (taxa_anual / 100) * tempo_anos)

    return round(montante, 2)