import os
import tempfile

import pytest

from api import api
from api.api import GitCloneRequest, clone_git_repo_and_get_structure


@pytest.mark.asyncio
async def test_clone_and_get_structure_success(monkeypatch):
    temp_dir = tempfile.mkdtemp(prefix="deepwiki_test_clone_")
    repo_dir = os.path.join(temp_dir, "repo")
    nested_dir = os.path.join(repo_dir, "src")
    os.makedirs(nested_dir)

    readme_path = os.path.join(repo_dir, "README.md")
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write("# Demo Repository\n\nSample content\n")

    sample_file = os.path.join(nested_dir, "main.py")
    with open(sample_file, "w", encoding="utf-8") as f:
        f.write("print('hello world')\n")

    hidden_file = os.path.join(repo_dir, ".env")
    with open(hidden_file, "w", encoding="utf-8") as f:
        f.write("SECRET=1\n")

    async def mock_clone_git_repository(request: GitCloneRequest):
        return {"clone_path": repo_dir, "temp_dir": temp_dir}

    monkeypatch.setattr(api, "clone_git_repository", mock_clone_git_repository)

    request = GitCloneRequest(repo_url="https://example.com/demo.git")
    response = await clone_git_repo_and_get_structure(request)

    assert "file_tree" in response
    assert "readme" in response

    file_tree_entries = response["file_tree"].split("\n")
    assert "src/main.py" in file_tree_entries
    assert "README.md" in file_tree_entries
    assert ".env" not in file_tree_entries

    assert response["readme"].startswith("# Demo Repository")

    assert not os.path.exists(temp_dir)


@pytest.mark.asyncio
async def test_clone_and_get_structure_clone_error(monkeypatch):
    async def mock_clone_git_repository(request: GitCloneRequest):
        from fastapi.responses import JSONResponse

        return JSONResponse(status_code=400, content={"error": "Git clone failed"})

    monkeypatch.setattr(api, "clone_git_repository", mock_clone_git_repository)

    request = GitCloneRequest(repo_url="https://example.com/demo.git")
    response = await clone_git_repo_and_get_structure(request)

    assert not isinstance(response, dict)
    assert response.status_code == 400


