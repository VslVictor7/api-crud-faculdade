import pytest
from api import app

@pytest.fixture
def client():
    """Cria um cliente de teste para a API."""
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_add_task(client):
    """Testa a adição de uma nova task."""
    response = client.post("/tasks", json={"task": "Nova tarefa"})
    assert response.status_code == 201
    assert response.json["task"] == "Nova tarefa"

def test_get_tasks(client):
    """Testa se a listagem de tasks retorna corretamente."""
    response = client.get("/tasks")
    assert response.status_code == 200
    assert isinstance(response.json, list)

def test_update_task(client):
    """Testa a atualização de uma task existente."""
    client.post("/tasks", json={"task": "Tarefa antiga"})
    response = client.put("/tasks/1", json={"task": "Tarefa atualizada"})
    assert response.status_code == 200
    assert response.json["task"] == "Tarefa atualizada"

def test_delete_task(client):
    """Testa a remoção de uma task."""
    client.post("/tasks", json={"task": "Tarefa a ser removida"})
    response = client.delete("/tasks/1")
    assert response.status_code == 200
    assert response.json["message"] == "Task deleted"
