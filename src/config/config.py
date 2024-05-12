import os


def get_database_uri():
    return os.getenv("SUPABASE_URI")

def get_open_ai_api_key():
    return os.getenv("OPEN_AI_APIKEY")
