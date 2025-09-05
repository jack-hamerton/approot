def check_user_consent(user):
    if not user.consent_flags.get('data_usage'):
        raise ValueError("User has not consented to data usage.")
    return True

def validate_usage_intent(user):
    valid_intents = ['research', 'personal', 'commercial']
    if user.usage_intent not in valid_intents:
        raise ValueError("Invalid usage intent specified.")
    return True

def ethical_check_for_community_creation(user):
    if not user.consent_flags.get('community_creation'):
        raise ValueError("User has not consented to community creation.")
    return True

def ensure_compliance_with_safeguards(data):
    if 'sensitive_info' in data and not data.get('user_consent'):
        raise ValueError("Sensitive information requires user consent.")
    return True