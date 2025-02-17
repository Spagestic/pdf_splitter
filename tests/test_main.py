import pytest
from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_upload_pdf():
    with open("tests/sample.pdf", "rb") as pdf_file:
        response = client.post("/upload/", files={"file": pdf_file})
    assert response.status_code == 200
    assert "images" in response.json()

def test_invalid_file_type():
    response = client.post("/upload/", files={"file": ("test.txt", b"test content")})
    assert response.status_code == 400
    assert response.json() == {"detail": "Invalid file type. Only PDF files are allowed."}