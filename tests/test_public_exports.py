import ast
from pathlib import Path

import sonarqube


def test_client_resource_classes_are_public_exports():
    client_module = Path("src/sonarqube/client.py")
    module = ast.parse(client_module.read_text())
    client_class = next(
        node
        for node in module.body
        if isinstance(node, ast.ClassDef) and node.name == "SonarQubeClient"
    )
    init_method = next(
        node
        for node in client_class.body
        if isinstance(node, ast.FunctionDef) and node.name == "__init__"
    )
    resource_classes = {
        node.value.func.id
        for node in init_method.body
        if isinstance(node, ast.Assign)
        and isinstance(node.value, ast.Call)
        and isinstance(node.value.func, ast.Name)
        and node.value.func.id.startswith("SonarQube")
    }

    missing_exports = sorted(
        resource_class
        for resource_class in resource_classes
        if not hasattr(sonarqube, resource_class)
    )

    assert missing_exports == []
