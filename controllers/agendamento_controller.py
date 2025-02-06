from fastapi import APIRouter, Request, Form, HTTPException
from fastapi.templating import Jinja2Templates
from services.agendamento_service import (
    fetch_agendamentos,
    add_agendamento,
    delete_agendamento_service,
    fetch_agendamento_by_id,
    update_agendamento_service,
)

router = APIRouter()
templates = Jinja2Templates(directory="templates")


@router.get("/agendamentos")
def listar_agendamentos(request: Request):
    agendamentos = fetch_agendamentos()
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "titulo": "Lista de Agendamentos",
            "colunas": ["ID", "Quadra ID", "Data", "Hora", "Responsável"],
            "itens": agendamentos,
            "url_add": "/agendamentos/novo",
            "url_editar": "/agendamentos/editar",
            "url_excluir": "/agendamentos/excluir",
        },
    )


@router.get("/agendamentos/novo")
def form_novo_agendamento(request: Request):
    return templates.TemplateResponse(
        "form.html",
        {
            "request": request,
            "titulo": "Novo Agendamento",
            "url_salvar": "/agendamentos/salvar",
            "url_voltar": "/agendamentos",
            "campos": {"quadra_id": "", "data": "", "hora": "", "nome_responsavel": ""},
        },
    )


@router.post("/agendamentos/salvar")
def salvar_agendamento(
    quadra_id: int = Form(...),
    data: str = Form(...),
    hora: str = Form(...),
    nome_responsavel: str = Form(...),
):
    novo_agendamento = {
        "quadra_id": quadra_id,
        "data": data,
        "hora": hora,
        "nome_responsavel": nome_responsavel,
    }
    return add_agendamento(novo_agendamento)


@router.get("/agendamentos/editar/{agendamento_id}")
def form_editar_agendamento(request: Request, agendamento_id: int):
    agendamento = fetch_agendamento_by_id(agendamento_id)
    if not agendamento:
        raise HTTPException(status_code=404, detail="Agendamento não encontrado")

    return templates.TemplateResponse(
        "form.html",
        {
            "request": request,
            "titulo": "Editar Agendamento",
            "url_salvar": f"/agendamentos/atualizar/{agendamento_id}",
            "url_voltar": "/agendamentos",
            "campos": agendamento,
        },
    )


@router.post("/agendamentos/atualizar/{agendamento_id}")
def atualizar_agendamento(
    agendamento_id: int,
    quadra_id: int = Form(...),
    data: str = Form(...),
    hora: str = Form(...),
    nome_responsavel: str = Form(...),
):
    updated_data = {
        "quadra_id": quadra_id,
        "data": data,
        "hora": hora,
        "nome_responsavel": nome_responsavel,
    }
    return update_agendamento_service(agendamento_id, updated_data)


@router.get("/agendamentos/excluir/{agendamento_id}")
def excluir_agendamento(agendamento_id: int):
    if delete_agendamento_service(agendamento_id):
        return {"message": "Agendamento deletado com sucesso"}
    raise HTTPException(status_code=404, detail="Agendamento não encontrado")
