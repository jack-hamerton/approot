import React, { useEffect, useState } from 'react';

const CommunityList: React.FC = () => {
    const [communities, setCommunities] = useState([]);

    useEffect(() => {
        const fetchCommunities = async () => {
            try {
                const response = await fetch('/api/community');
                const data = await response.json();
                setCommunities(data);
            } catch (error) {
                console.error('Error fetching communities:', error);
            }
        };

        fetchCommunities();
    }, []);

    return (
        <div>
            <h2>Community List</h2>
            <ul>
                {communities.map((community) => (
                    <li key={community.id}>
                        <h3>{community.name}</h3>
                        <p>{community.description}</p>
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default CommunityList;