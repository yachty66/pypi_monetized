from supabase import create_client, Client
from dotenv import load_dotenv
import os 
load_dotenv()

url: str = os.getenv("SUPABASE_URL")  
key: str = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(url, key)

def signup(email: str):
    response, error = supabase.auth.sign_up({
        "email": 'example@email.com',
        "password": 'example-password',
    })
    if error:
        print("Error sending magic link:", error)
    else:
        print("Magic link sent to", email)