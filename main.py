if __name__ == "__main__":
    import sys

    import uvicorn

    # En Windows, reload=True crea un subproceso que suele romper sesiones SQLAlchemy
    # globales en los CRUD (500 en Swagger). En Linux/macOS el recarga automática sigue activa.
    use_reload = sys.platform != "win32"
    uvicorn.run(
        "src.api.app:app",
        host="0.0.0.0",
        port=8000,
        reload=use_reload,
    )
