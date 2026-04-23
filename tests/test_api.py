import json

import pytest
from jsonschema import validate
from playwright.sync_api import sync_playwright

@pytest.mark.parametrize("api_request_context", ["users"], indirect=True)
def test_get_user(api_request_context):
    response = api_request_context.get("/users/1")

    assert response.status == 200

    data = response.json()
    print(json.dumps(data, indent=4))

    schema = {
        "type": "object",
        "properties": {
            "id": {"type": "number"},
            "name": {"type": "string"},
            "username": {"type": "string"},
            "email": {"type": "string"},
            "address": {"type": "object"},
            "phone": {"type": "string"},
            "website": {"type": "string"},
            "company": {"type": "object"}
        },
        "required": ["id", "name", "username", "email"]
    }

    validate(instance=data, schema=schema)


def test_post_user(api_request_context):
    payload = {
        "name": "Johnathan",
        "email": "john@test.com"
    }

    response = api_request_context.post("/users", json=payload)

    assert response.status == 201

    data = response.json()
    print(json.dumps(data, indent=4))

    expected = {
        "name": "Johnathan",
        "email": "john@test.com"
    }

    for key, value in expected.items():
        assert data[key] == value

    assert isinstance(data["id"], int)
    assert isinstance(data["name"], str)
    assert isinstance(data["email"], str)