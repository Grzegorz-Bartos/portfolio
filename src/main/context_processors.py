# context_processors.py
from datetime import date

from .models import Profile


def personal_information(request):
    profile = Profile.objects.first()
    if not profile:
        return {
            "YEARS_OF_EXPERIENCE": 0,
            "AVAILABILITY": False,
            "GITHUB": "",
            "LINKEDIN": "",
            "DISCORD": "",
            "CLIENT_COUNT": 0,
            "PROJECTS_COMPLETED": 0,
            "PROFILE_PICTURE": "",
            "RESUME": False,
        }

    return {
        "YEARS_OF_EXPERIENCE": date.today().year - profile.start_year,
        "AVAILABILITY": profile.availability,
        "GITHUB": profile.github,
        "LINKEDIN": profile.linkedin,
        "DISCORD": profile.discord,
        "CLIENT_COUNT": profile.client_count,
        "PROJECTS_COMPLETED": profile.projects_completed,
        "PROFILE_PICTURE": profile.image.url if profile.image else "",
        "RESUME": profile.resume.url if profile.resume else "",
    }
