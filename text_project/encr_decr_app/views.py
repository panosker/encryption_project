from django.shortcuts import render
from .encryption import encrypt, decrypt
from .ratelimit import new_rates


@new_rates(non_registered_rate="10/m", registered_rate="50/m")
def index(request):
    return render(request, "index.html")


@new_rates(non_registered_rate="10/m", registered_rate="50/m")
def action(request):
    if request.method == "POST":
        selected_action = request.POST.get("action")
        return render(request, "index.html", {"selected_action": selected_action})
    return render(request, "index.html")


@new_rates(non_registered_rate="10/m", registered_rate="50/m")
def encrypted(request):
    if request.method == "POST":
        text = request.POST.get("text")
        encrypted_text = encrypt(text)
        return render(
            request,
            "index.html",
            {
                "text": text,
                "encrypted_text": encrypted_text,
                "selected_action": "encrypt",
            },
        )
    return render(request, "index.html")


@new_rates(non_registered_rate="10/m", registered_rate="50/m")
def decrypted(request):
    if request.method == "POST":
        text = request.POST.get("text")
        decrypted_text = decrypt(text)
        return render(
            request,
            "index.html",
            {
                "text": text,
                "decrypted_text": decrypted_text,
                "selected_action": "decrypt",
            },
        )
    return render(request, "index.html")


@new_rates(non_registered_rate="10/m", registered_rate="50/m")
def about(request):
    return render(request, "about.html")
