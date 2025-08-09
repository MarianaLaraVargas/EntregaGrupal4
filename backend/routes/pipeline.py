from fastapi import APIRouter
import subprocess

router = APIRouter(prefix="/api", tags=["Pipeline"])

@router.get("/pipeline/run")
def run_pipeline():
    subprocess.run(["python3", "pipeline/etl.py"])
    return {"message": "Pipeline executed"}
