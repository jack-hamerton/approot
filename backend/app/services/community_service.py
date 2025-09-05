from typing import List
from fastapi import HTTPException
from ..models.community import Community
from ..models.user import User

class CommunityRoomManager:
    def __init__(self):
        self.communities = []  # This will hold the community instances

    def create_community(self, community: Community) -> Community:
        if any(c.name == community.name for c in self.communities):
            raise HTTPException(status_code=400, detail="Community already exists")
        self.communities.append(community)
        return community

    def get_communities(self) -> List[Community]:
        return self.communities

    def get_community(self, community_id: int) -> Community:
        for community in self.communities:
            if community.id == community_id:
                return community
        raise HTTPException(status_code=404, detail="Community not found")

    def delete_community(self, community_id: int) -> None:
        for index, community in enumerate(self.communities):
            if community.id == community_id:
                del self.communities[index]
                return
        raise HTTPException(status_code=404, detail="Community not found")

    def join_community(self, community_id: int, user: User) -> None:
        community = self.get_community(community_id)
        if user not in community.members:
            community.members.append(user)
        else:
            raise HTTPException(status_code=400, detail="User already a member")

    def leave_community(self, community_id: int, user: User) -> None:
        community = self.get_community(community_id)
        if user in community.members:
            community.members.remove(user)
        else:
            raise HTTPException(status_code=400, detail="User not a member")