import React from 'react';

interface CommunityDetailProps {
    community: {
        id: string;
        name: string;
        description: string;
        members: number;
        createdAt: string;
    };
}

const CommunityDetail: React.FC<CommunityDetailProps> = ({ community }) => {
    return (
        <div className="community-detail">
            <h2>{community.name}</h2>
            <p>{community.description}</p>
            <p>Members: {community.members}</p>
            <p>Created At: {new Date(community.createdAt).toLocaleDateString()}</p>
        </div>
    );
};

export default CommunityDetail;