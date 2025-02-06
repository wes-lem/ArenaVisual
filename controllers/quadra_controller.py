from fastapi import APIRouter, Request, Form, HTTPException
from fastapi.templating import Jinja2Templates
from services.quadra_service import (
    fetch_quadras,
    add_quadra,
    delete_quadra_service,
    fetch_quadra_by_id,
    update_quadra_service,
)

router = APIRouter()
templates = Jinja2Templates(directory="templates")


@router.get("/quadras")
def listar_quadras(request: Request):
    quadras = fetch_quadras()
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "titulo": "Lista de Quadras",
            "colunas": ["ID", "Nome", "Capacidade"],
            "itens": quadras,
            "url_add": "/quadras/novo",
            "url_editar": "/quadras/editar",
            "url_excluir": "/quadras/excluir",
        },
    )


@router.get("/quadras/novo")
def form_nova_quadra(request: Request):
    return templates.TemplateResponse(
        "form.html",
        {
            "request": request,
            "titulo": "Nova Quadra",
            "url_salvar": "/quadras/salvar",
            "url_voltar": "/quadras",
            "campos": {"id": "","nome": "", "capacidade": ""},
        },
    )

@router.post("/quadras/salvar")
def salvar_quadra(
    id: str = Form(...),
    nome: str = Form(...),
    capacidade: int = Form(...),
):
    nova_quadra = {
        "id": id,
        "nome": nome,
        "capacidade": capacidade,
    }
    return add_quadra(nova_quadra)


@router.get("/quadras/editar/{quadra_id}")
def form_editar_quadra(request: Request, quadra_id: int):
    quadra = fetch_quadra_by_id(quadra_id)
    if not quadra:
        raise HTTPException(status_code=404, detail="Quadra não encontrada")

    return templates.TemplateResponse(
        "form.html",
        {
            "request": request,
            "titulo": "Editar Quadra",
            "url_salvar": f"/quadras/atualizar/{quadra_id}",
            "url_voltar": "/quadras",
            "campos": quadra,
        },
    )


@router.post("/quadras/atualizar/{quadra_id}")
def atualizar_quadra(
    quadra_id: int,
    nome: str = Form(...),
    capacidade: int = Form(...),
):
    if not nome or not capacidade:
        raise HTTPException(
            status_code=400, detail="Nome e Capacidade são obrigatórios"
        )

    updated_data = {
        "nome": nome,
        "capacidade": capacidade,
    }
    updated_quadra = update_quadra_service(quadra_id, updated_data)
    if not updated_quadra:
        raise HTTPException(status_code=404, detail="Quadra não encontrada")

    return updated_quadra


@router.get("/quadras/excluir/{quadra_id}")
def excluir_quadra(quadra_id: int):
    if delete_quadra_service(quadra_id):
        return {"message": "Quadra deletada com sucesso"}
    raise HTTPException(status_code=404, detail="Quadra não encontrada")
