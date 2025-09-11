lista_compras = ["maçã", "banana", "laranja"]

def listar_itens(query: str) -> dict:
    # por baixo dos panos o agente usa essa documentacao da funcao abaixo
    # ou seja, se passarmos varias tools, em todas as funcoes ele vai procurar 
    # essas documentacoes e ver qual é mais semelhante ao pedido do usuario
    """Lista os itens na lista de compras.
    
    Args:
        query (str): Pedido do usuário.

    Returns:
        dict: Status da operação e a lista de itens.
    """
    return {"status": "ok", "list": lista_compras}

def adiciona_item(item: str) -> dict:
    """Adiciona um item à lista de compras.
    
    Args:
        item (str): O item a ser adicionado.

    Returns:
        dict: Status da operação e a lista atualizada.
    """
    lista_compras.append(item)
    return {"status": "ok", "list": lista_compras}