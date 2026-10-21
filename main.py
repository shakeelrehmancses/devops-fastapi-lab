from fastapi import FastAPI

app = FastAPI(
    title="DevOps Pipeline Lab API",
    description="A baseline FastAPI application for DevOps training.",
    version="1.0.0"
)

@app.get("/")
def read_root():
    return {
        "status": "online",
        "message": "Welcome to the Advanced Software Development & DevOps Course!",
        "environment": "Local Development"
    }

@app.get("/health")
def health_check():
    return {"status": "healthy", "database": "connected"}