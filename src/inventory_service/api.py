from fastapi import FastAPI

app = FastAPI(
    title="Inventory Restoration Service",
    version="0.1.0"
)

@app.get("/health")
async def read_root():
    return {"status": "healthy"}