import json

QUADRAS_FILE = "data/quadras.json"


def load_quadras():
    """Carrega as quadras do arquivo JSON."""
    try:
        with open(QUADRAS_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_quadras(quadras):
    """Salva as quadras no arquivo JSON."""
    with open(QUADRAS_FILE, "w") as file:
        json.dump(quadras, file, indent=4)


def get_all_quadras():
    """Retorna todas as quadras cadastradas."""
    return load_quadras()


def get_quadra_by_id(quadra_id):
    """Busca uma quadra específica pelo ID."""
    quadras = load_quadras()
    for quadra in quadras:
        if quadra["id"] == quadra_id:
            return quadra
    return None


def insert_quadra(quadra):
    """Insere uma nova quadra no sistema."""
    quadras = load_quadras()
    quadra["id"] = len(quadras) + 1  # Simula um ID autoincremento
    quadras.append(quadra)
    save_quadras(quadras)
    return quadra


def update_quadra(quadra_atualizada):
    """Atualiza uma quadra existente."""
    quadras = load_quadras()
    for i, quadra in enumerate(quadras):
        if quadra["id"] == quadra_atualizada["id"]:
            quadras[i] = quadra_atualizada
            save_quadras(quadras)
            return quadra_atualizada
    return None


def delete_quadra(quadra_id):
    """Remove uma quadra pelo ID."""
    quadras = load_quadras()
    quadras_filtradas = [q for q in quadras if q["id"] != quadra_id]

    if len(quadras) == len(quadras_filtradas):
        return False  # Nenhuma quadra removida

    save_quadras(quadras_filtradas)
    return True  # Sucesso
