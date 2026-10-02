"""Startovací API pro GroveCloud (FastAPI).

GroveCloud spouští: uvicorn main:app --host 0.0.0.0 --port $PORT
"""
from datetime import datetime, timezone

from fastapi import FastAPI

app = FastAPI(title="Moje API na GroveCloudu")


@app.get("/")
def koren() -> dict:
    return {"stav": "běží", "endpointy": ["/health", "/api/ahoj?jmeno=Petr", "/docs"]}


@app.get("/health")
def health() -> dict:
    return {"ok": True}


@app.get("/api/ahoj")
def ahoj(jmeno: str = "světe") -> dict:
    return {"zprava": f"Ahoj, {jmeno}!", "cas": datetime.now(timezone.utc).isoformat()}
