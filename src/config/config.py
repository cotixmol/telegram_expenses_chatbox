import os

def get_database_uri():
    return os.getenv("SUPABASE_URI")
