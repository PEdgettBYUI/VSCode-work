from supabase import create_client, Client 

supabase_url = "https://wxgpdbzpmxphwubxyqou.supabase.co/"
supabase_api_key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Ind4Z3BkYnpwbXhwaHd1Ynh5cW91Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3Mzg3MTc2NzEsImV4cCI6MjA1NDI5MzY3MX0.ZgqA3KGS2igfkNNoKs5_HlnciB_A43tw2rKpGuwRVSI"

client = create_client(supabase_url, supabase_api_key)

test = {
    "last_name": "Patrick",
    "first_name": "Edgett"
}

response = (
    client.table("test")
    .insert(test)
    .execute()
)

print("Hello World")