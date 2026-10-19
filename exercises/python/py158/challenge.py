def get_timeout(settings, default=30):
    return settings.get("timeout") or default
