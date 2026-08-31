ASSINATURAS: dict[str, dict] = {
    "cliente_123": {"plano": "Pro", "status": "ativa", "renovacao": "2026-07-01"},
}

FATURAS = [
    {
        "id": "fatura_001",
        "cliente_id": "cliente_123",
        "valor": 49.99,
        "data_emissao": "2024-01-01",
        "data_vencimento": "2024-01-15",
        "status": "paga",
    },
    {
        "id": "fatura_002",
        "cliente_id": "cliente_123",
        "valor": 49.99,
        "data_emissao": "2024-02-01",
        "data_vencimento": "2024-02-15",
        "status": "pendente",
    },
]

def listar_faturas(cliente_id: str) -> dict:
    """
        Lista as faturas de um cliente específico.
        Args:
            cliente_id (str): O ID do cliente para o qual as faturas devem ser listadas.
        Returns:
            dict: Um dicionário contendo a lista de faturas do cliente.
    """

    return {
        "faturas": [fatura for fatura in FATURAS if fatura["cliente_id"] == cliente_id],
    }

def consultar_assinatura(cliente_id: str) -> dict:
    """
        Consulta os dados da assinatura de um cliente específico, como plano, status e data de renovação.
        Args:
            cliente_id (str): O ID do cliente para o qual a assinatura deve ser consultada.
        Returns:
            dict: Um dicionário contendo os dados da assinatura do cliente.
    """

    assinatura = ASSINATURAS.get(cliente_id)
    return {"assinatura": assinatura}

def cancelar_assinatura(cliente_id: str, senha: str) -> dict:
    """
        Cancela a assinatura de um cliente específico.
        Args:
            cliente_id (str): O ID do cliente para o qual a assinatura deve ser cancelada.
            senha (str): A senha fornecida pelo cliente para autenticação.
        Returns:
            dict: Um dicionário contendo o status da operação de cancelamento.
    """

    if senha != "senha_secreta":
        return {"status": "nao_cancelada", "mensagem": "Senha incorreta. Cancelamento não autorizado."}
    
    assinatura = ASSINATURAS.get(cliente_id)
    if assinatura is not None:
        assinatura["status"] = "cancelada"
    return {"status": "cancelada", "cliente_id": cliente_id}
