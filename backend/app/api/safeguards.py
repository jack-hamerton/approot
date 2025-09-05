from fastapi import APIRouter, HTTPException
from app.models.safeguard import Safeguard
from app.services.safeguard_service import SafeguardService

router = APIRouter()
safeguard_service = SafeguardService()

@router.post("/safeguards/", response_model=Safeguard)
async def create_safeguard(safeguard: Safeguard):
    try:
        return await safeguard_service.create_safeguard(safeguard)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/safeguards/{safeguard_id}", response_model=Safeguard)
async def get_safeguard(safeguard_id: int):
    safeguard = await safeguard_service.get_safeguard(safeguard_id)
    if not safeguard:
        raise HTTPException(status_code=404, detail="Safeguard not found")
    return safeguard

@router.put("/safeguards/{safeguard_id}", response_model=Safeguard)
async def update_safeguard(safeguard_id: int, safeguard: Safeguard):
    updated_safeguard = await safeguard_service.update_safeguard(safeguard_id, safeguard)
    if not updated_safeguard:
        raise HTTPException(status_code=404, detail="Safeguard not found")
    return updated_safeguard

@router.delete("/safeguards/{safeguard_id}")
async def delete_safeguard(safeguard_id: int):
    success = await safeguard_service.delete_safeguard(safeguard_id)
    if not success:
        raise HTTPException(status_code=404, detail="Safeguard not found")
    return {"detail": "Safeguard deleted successfully"}