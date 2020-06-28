from datasette.app import Datasette
from datasette_glitch import startup
import pytest
import httpx


@pytest.mark.asyncio
async def test_plugin_is_installed():
    app = Datasette([], memory=True).app()
    async with httpx.AsyncClient(app=app) as client:
        response = await client.get("http://localhost/-/plugins.json")
        assert 200 == response.status_code
        installed_plugins = {p["name"] for p in response.json()}
        assert "datasette-glitch" in installed_plugins


def test_startup_with_no_variable(monkeypatch, capsys):
    monkeypatch.delenv("PROJECT_DOMAIN", raising=False)
    ds = Datasette([], memory=True)
    startup(ds)
    captured = capsys.readouterr()
    assert "" == captured.out


def test_startup_with_variable(monkeypatch, capsys):
    monkeypatch.setenv("PROJECT_DOMAIN", "test-env")
    ds = Datasette([], memory=True)
    startup(ds)
    captured = capsys.readouterr()
    assert (
        "https://test-env.glitch.me/-/auth-token?token={}".format(ds._root_token)
        == captured.out.strip()
    )
