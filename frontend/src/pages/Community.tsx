import React from 'react';
import CommunityList from '../components/Community/CommunityList';
import CommunityDetail from '../components/Community/CommunityDetail';

const CommunityPage: React.FC = () => {
    return (
        <div>
            <h1>Community Management</h1>
            <CommunityList />
            <CommunityDetail />
        </div>
    );
};

export default CommunityPage;