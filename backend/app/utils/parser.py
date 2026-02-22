def detect_email_attributes(subject, body):
    text = (subject + " " + body).lower()

    high_keywords = [
        "urgent",
        "immediately",
        "asap",
        "server down",
        "production issue",
        "failure",
        "critical",
        "invoice",
        "payment",
        "security alert",
        "breach",
        "compliance",
        "escalation"
    ]

    medium_keywords = [
        "reminder",
        "deadline",
        "important",
        "follow up"
    ]

    spam_keywords = [
        "lottery",
        "congratulations",
        "click here",
        "free money",
        "winner",
        "prize",
        "claim now"
    ]

    work_keywords = [
        "meeting",
        "client",
        "project",
        "server",
        "production",
        "deployment"
    ]

    # Default values
    priority = "low"
    category = "general"

    # 🔥 Spam has highest override
    for word in spam_keywords:
        if word in text:
            category = "spam"
            priority = "low"
            return category, priority

    # High priority
    for word in high_keywords:
        if word in text:
            priority = "high"
            break

    # Medium priority
    if priority != "high":
        for word in medium_keywords:
            if word in text:
                priority = "medium"
                break

    # Work category
    for word in work_keywords:
        if word in text:
            category = "work"
            break

    return category, priority