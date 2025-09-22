from vercel import VercelResponse  # hypothetical; Vercel runtime gives env to Python functions
# Actually @vercel/python executes the .py file and returns whatever you print.
def handler(request):
    # For demo: return a small HTML
    return ("200 OK", [("Content-Type", "text/html")], b"<h1>Hello from serverless Python!</h1>")
