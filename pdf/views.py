from django.shortcuts import redirect, render
from .models import Profile
from .forms import ProfileForm
import pdfkit
from django.http import HttpResponse
from django.template import loader
import io

# Create your views here.


def profile_view(request):

    # profile = Profile.objects.get_or_create()

    if request.method == "POST":
        form = ProfileForm(request.POST)
        if form.is_valid():
            profile = form.save()
            print("klklkl;k")
            return redirect("list", pk=profile.id)
    else:

        form = ProfileForm()

    return render(
        request,
        "pdf/pdf.html",
        {
            "form": form,
        },
    )


def resume(request, pk):
    profile = Profile.objects.get(id=pk)
    profile_data = {
        "Name": profile.name,
        "Email": profile.email,
        "Phone": profile.phone,
        "Summary": profile.summary,
        "Degree": profile.degree,
        "School": profile.school,
        "University": profile.university,
        "Previous Role": profile.previous_work,
        "Skills": profile.skils,
    }
    template = loader.get_template("pdf/resume.html")
    html = template.render({"profile_data": profile_data})
    options = {
        "page-size": "Letter",
        "encoding": "UTF-8",
    }
    pdf = pdfkit.from_string(html, False, options)
    response = HttpResponse(pdf, content_type="application/pdf")
    response["Content-Disposition"] = "attachment"
    filename = "resume.pdf"
    return response
    # return render(
    #     request,
    #     "pdf/resume.html",
    #     {
    #         "profile": profile,
    #         "profile_data": profile_data,
    #     },
    # )


def list(request, pk):
    profile = Profile.objects.get(id=pk)
    profile_data = {
        "Name": profile.name,
        "Email": profile.email,
        "Phone": profile.phone,
        "Summary": profile.summary,
        "Degree": profile.degree,
        "School": profile.school,
        "University": profile.university,
        "Previous Role": profile.previous_work,
        "Skills": profile.skils,
    }
    return render(
        request,
        "pdf/list.html",
        {
            "profile": profile,
            "profile_data": profile_data,
        },
    )
