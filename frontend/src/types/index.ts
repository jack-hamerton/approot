export interface User {
    id: string;
    username: string;
    email: string;
    accountType: 'basic' | 'premium';
    usageIntent: string;
    consentFlags: {
        dataProcessing: boolean;
        marketing: boolean;
    };
}

export interface Community {
    id: string;
    name: string;
    description: string;
    createdAt: Date;
    members: User[];
}

export interface Safeguard {
    id: string;
    name: string;
    description: string;
    complianceStatus: 'compliant' | 'non-compliant';
}

export interface AuthResponse {
    token: string;
    user: User;
}

export interface CommunityResponse {
    communities: Community[];
}

export interface SafeguardResponse {
    safeguards: Safeguard[];
}