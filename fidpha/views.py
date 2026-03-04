

from django.contrib.auth import authenticate, login
from django.shortcuts import render

from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib import messages

from django.contrib.auth.decorators import login_required

from .models import Client


from .legacy_models import Sells
from .models import ContractProduct


# Create your views here.


#
# def index(request):
#     return render(request, "fidpha/index.html")
#
#
# def clients_resume(request):
#
#     clients = Client.objects.prefetch_related(
#         Prefetch(
#             "contracts",
#             queryset=Contract.objects.prefetch_related(
#                 Prefetch(
#                     "contractproduct_set",
#                     queryset=ContractProduct.objects.select_related("product")
#                 )
#             )
#         )
#     )
#
#     return render(request, "fidpha/clients_resume.html", {"clients": clients})






@login_required
def client_dashboard(request):
    if request.user.is_staff:
        return redirect("/admin/")

    try:
        client = Client.objects.get(user=request.user)
    except Client.DoesNotExist:
        return redirect("/accounts/login/")

    # Join Sells with ContractProduct to get the factor
    total_points = 0
    sells = Sells.objects.filter(client=client)

    for sell in sells:
        try:
            contract_product = ContractProduct.objects.get(
                contract_id=sell.client.client_id,
                product_id=sell.product.product_id
            )
            total_points += sell.quantity * contract_product.factor
        except ContractProduct.DoesNotExist:
            # No factor defined for this product in this contract
            pass

    return render(request, "fidpha/client_dashboard.html", {
        "client": client,
        "total_points": total_points
    })

@login_required
def client_details(request):
    client = Client.objects.get(user=request.user)

    # Fetch all sales for this client
    sells = Sells.objects.filter(client=client).order_by('-sell_date')

    # Prepare history list for template ---
    sell_history = []

    for sell in sells:
        try:
            contract_product = ContractProduct.objects.get(
                contract_id=sell.contract.contract_id,
                product_id=sell.product.product_id
            )
            factor = contract_product.factor
        except ContractProduct.DoesNotExist:
            factor = 0  # fallback if no factor defined

        sell_history.append({
            'date': sell.sell_date,
            'contract': sell.contract.contract_number,
            'product': sell.product.product_name,
            'quantity': sell.quantity,
            'factor': factor,
            'points': sell.quantity * factor
        })

    return render(request, "fidpha/client_details.html", {
        "client": client,
        "sell_history": sell_history
    })



def custom_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        is_admin_checked = request.POST.get("admin_login")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            if is_admin_checked and not user.is_staff:
                messages.error(request, "You are not an admin user")
                return redirect("login")  # redirect → message preserved

            login(request, user)

            if user.is_staff:
                return redirect("/admin/")
            else:
                return redirect("fidpha:client_dashboard")
        else:
            # Wrong credentials → message stored in session
            messages.error(request, "Invalid username or password")
            return redirect("login")  # redirect → message preserved

    # GET request → render login page
    return render(request, "registration/login.html")


def custom_logout(request):
    """
    Logs out the current user and redirects to the login page.
    """
    logout(request)  # ends the session
    messages.success(request, "You have been logged out successfully.")
    return redirect("login")  # redirect to your login page


# @login_required
# def landing(request):
#     if request.user.is_staff:
#         return redirect("/admin/")
#     else:
#         return redirect("fidpha:client_dashboard")