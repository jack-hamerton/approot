from fastapi import APIRouter, HTTPException
from typing import List
from ..models.community import Community
from ..services.community_service import CommunityRoomManager

router = APIRouter()
community_manager = CommunityRoomManager()

@router.post("/communities/", response_model=Community)
async def create_community(community: Community):
    return community_manager.create_community(community)

@router.get("/communities/", response_model=List[Community])
async def get_communities():
    return community_manager.get_all_communities()

@router.get("/communities/{community_id}", response_model=Community)
async def get_community(community_id: int):
    community = community_manager.get_community_by_id(community_id)
    if not community:
        raise HTTPException(status_code=404, detail="Community not found")
    return community

@router.put("/communities/{community_id}", response_model=Community)
async def update_community(community_id: int, community: Community):
    updated_community = community_manager.update_community(community_id, community)
    if not updated_community:
        raise HTTPException(status_code=404, detail="Community not found")
    return updated_community

@router.delete("/communities/{community_id}", response_model=dict)
async def delete_community(community_id: int):
    success = community_manager.delete_community(community_id)
    if not success:
        raise HTTPException(status_code=404, detail="Community not found")
    return {"message": "Community deleted successfully"}