from vercel import 
def handler(request):
    return ("200 OK", [("Content-Type", "text/html")], b"<h1>Hello from serverless Python!</h1>")
