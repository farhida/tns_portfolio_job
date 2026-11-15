from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegisterForm, LoginForm, ContactForm
from .models import Profile, Skill, Education, Experience, Project

def home(request):
    profile = Profile.objects.first()
    context = {
        "profile": profile,
        "skills": Skill.objects.all(),
        "education": Education.objects.all()[:3],
        "experiences": Experience.objects.all()[:3],
        "projects": Project.objects.all(),
        "contact_form": ContactForm(),
    }
    return render(request, "Portfolio/home.html", context)

def project_detail(request, slug):
    project = get_object_or_404(Project, slug=slug)
    return render(request, "Portfolio/project_detail.html", {"project": project, "profile": Profile.objects.first()})

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thanks! Your message has been sent successfully.")
            return redirect("home")
        messages.error(request, "Please correct the errors in the contact form.")
    else:
        form = ContactForm()
    return render(request, "Portfolio/contact.html", {"form": form, "profile": Profile.objects.first()})

def resume(request):
    return render(request, "Portfolio/resume.html", {
        "profile": Profile.objects.first(),
        "skills": Skill.objects.all(),
        "education": Education.objects.all(),
        "experiences": Experience.objects.all(),
        "projects": Project.objects.all(),
    })

def register(request):
    if request.user.is_authenticated:
        return redirect("dashboard")
    form = RegisterForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        user = form.save()
        login(request, user)
        messages.success(request, "Your account has been created.")
        return redirect("dashboard" if user.is_staff else "home")
    return render(request, "Portfolio/auth.html", {"form": form, "page_title": "Create account", "is_register": True})

def login_view(request):
    if request.user.is_authenticated:
        return redirect("dashboard" if request.user.is_staff else "home")
    form = LoginForm(request, data=request.POST or None)
    if request.method == "POST" and form.is_valid():
        user = form.get_user()
        login(request, user)
        return redirect("dashboard" if user.is_staff else "home")
    return render(request, "Portfolio/auth.html", {"form": form, "page_title": "Welcome back", "is_register": False})

def logout_view(request):
    logout(request)
    messages.info(request, "You have been logged out.")
    return redirect("home")

@login_required
@user_passes_test(lambda user: user.is_staff)
def dashboard(request):
    from .models import ContactMessage
    return render(request, "Portfolio/dashboard.html", {
        "profile": Profile.objects.first(),
        "skill_count": Skill.objects.count(),
        "project_count": Project.objects.count(),
        "message_count": ContactMessage.objects.count(),
        "unread_count": ContactMessage.objects.filter(is_read=False).count(),
    })
