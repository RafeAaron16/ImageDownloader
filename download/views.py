from django.shortcuts import render
import os
import requests

# Create your views here.

def index(request):
    message = None
    if request.method == "POST":
        url = request.POST["url"]
        save_name = request.POST["name"]

        response = requests.get(url)
        if response.status_code == 200:
            save_path = os.path.join(os.path.expanduser("~"), "Downloads", save_name)
            with open(save_path, 'wb') as file:
                file.write(response.content)
            message = "Image downloaded successfully."
        else:
            message = "Failed to download image"
    return render(request, "download/index.html", {
        "message": message
    })


