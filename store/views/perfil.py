from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from store.models.perfil import UserProfile
from store.forms.perfilForms import UserProfileForm, MyUserForm
from store.models.customer import Customer


# @login_required
def view_profile(request):
    user_id = request.session.get("customer")
    user = Customer.objects.get(id=user_id)
    profile = UserProfile.objects.get(user=user)
    context = {
        "profile": profile,
        "user" : user,
    }
    return render(request, "perfil.html", context)


# @login_required
def edit_profile(request):
    user_id = request.session.get("customer")
    user = Customer.objects.get(id=user_id)
    profile = UserProfile.objects.get(user=user)

    if request.method == "POST":
        profile_form = UserProfileForm(request.POST, request.FILES, instance=profile)
        user_form = MyUserForm(request.POST, instance=user)

        if profile_form.is_valid() and user_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect("perfil")
    else:
        profile_form = UserProfileForm(instance=profile)
        user_form = MyUserForm(instance=user)

    return render(
        request,
        "edit_perfil.html",
        {"profile_form": profile_form, "user_form": user_form},
    )
