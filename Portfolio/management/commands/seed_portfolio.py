from django.core.management.base import BaseCommand
from Portfolio.models import Profile, Skill, Education, Experience, Project

class Command(BaseCommand):
    help = "Create an initial portfolio profile and sample content."

    def handle(self, *args, **options):
        if not Profile.objects.exists():
            Profile.objects.create(
                full_name="Your Name",
                headline="Web Developer & Creative Problem Solver",
                about="I build clean, accessible, and user-friendly web experiences. Replace this introduction with your own story, interests, and professional goals.",
                email="hello@example.com",
                location="Your City, Country",
            )

        sample_skills = [
            ("HTML", "Frontend", 90), ("CSS", "Frontend", 88),
            ("JavaScript", "Frontend", 82), ("Django", "Backend", 72),
            ("Python", "Backend", 75), ("Git", "Tools", 78),
        ]
        for index, (name, category, proficiency) in enumerate(sample_skills):
            Skill.objects.get_or_create(name=name, defaults={"category": category, "proficiency": proficiency, "sort_order": index})

        if not Project.objects.exists():
            Project.objects.create(
                title="Personal Portfolio Website",
                short_description="A responsive portfolio to introduce skills, experience, and selected work.",
                description="A personal website with project showcases, a resume page, and a contact form. Replace this sample with details about a project you have built.",
                tech_stack="Django, Python, HTML, CSS, JavaScript",
                featured=True,
            )
        self.stdout.write(self.style.SUCCESS("Portfolio starter content is ready."))
