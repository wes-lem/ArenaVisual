from dao.quadra_dao import (
    get_all_quadras,
    get_quadra_by_id,
    insert_quadra,
    update_quadra,
    delete_quadra,
)


def fetch_quadras():
    """Retorna todas as quadras cadastradas."""
    return get_all_quadras()


def fetch_quadra_by_id(quadra_id: int):
    """Busca uma quadra específica pelo ID."""
    return get_quadra_by_id(quadra_id)


def add_quadra(data: dict):
    """Adiciona uma nova quadra ao sistema."""
    nova_quadra = {
        "id": None,  # Será gerado automaticamente no DAO
        "nome": data["nome"],
        "capacidade": data["capacidade"],
    }
    return insert_quadra(nova_quadra)


def update_quadra_service(quadra_id: int, data: dict):
    """Atualiza uma quadra existente."""
    quadra_existente = get_quadra_by_id(quadra_id)
    if not quadra_existente:
        return None  # Quadra não encontrada

    quadra_atualizada = {
        "id": quadra_id,
        "nome": data["nome"],
        "capacidade": data["capacidade"],
    }
    return update_quadra(quadra_atualizada)


def delete_quadra_service(quadra_id: int):
    """Exclui uma quadra pelo ID."""
    return delete_quadra(quadra_id)
