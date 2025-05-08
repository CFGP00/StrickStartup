from django.shortcuts import render

def home(request):
    projects = [
        {"title": "Hampden County Registry of Deeds", "desc": "Leveraged a powerful computer vision model to transcribe 300 year old documents into a digitized format. This data was then indexed, making search much more efficient."},
        {"title": "Radiologist Level Computer Vision Model", "desc": "We developed and trained a Computer Vision Model to read chest X-Rays, with an accuracy of x.xx %. This model has been made publically available in order to help trained professionals to be able to diagnose patients more efficiently. ", "link" : "https://huggingface.co/spaces/cfgpp/Danny_Net_Demo"}
    ]
    mission = "Strick Data Solutions is a data science and AI consulting agency based in Boston, Massachusetts. We specialize in helping small and medium-sized businesses unlock the power of their data to drive smarter decisions, boost efficiency, and fuel growth. Founded on the belief that cutting-edge technology should be accessible to all businesses, not just Fortune 500s, we bring elite data science and AI expertise to organizations that need practical, scalable, and personalized solutions."
    team = "We're a team of highly skilled data scientists and AI engineers who thrive on solving complex challenges. Our size allows us to be agile, our focus keeps us efficient, and our passion ensures every project delivers real impact."
    value = ["Clarity over jargon", "Speed without compromise", "Partnership over transactions", "Results that matter"]
    quote = "Whether you're trying to make sense of messy data, automate workflows, build predictive models, or simply figure out where to start, we’re here to guide you."
    contact_email = "strickds@proton.me"
    return render(request, "projects/home.html", {
        "projects": projects,
        "mission": mission,
        "contact_email": contact_email,
        "team": team,
        "value": value,
        "quote": quote,
    })

def contact(request):
    contact_email = "strickds@proton.me"
    return render(request, "projects/contact.html", {
        "contact_email": contact_email,
    })

def about(request):
    about = "We are a team of Data Science Consultants eager to work on varying projects. From Healthcare to Computer Vision, Strick Data Solutions is here to help. Contact us to collaborate or consult!"
    return render(request, "projects/about.html", {
        "about": about,
    })

def projects(request):
    projects = [
        {"title": "Hampden County Registry of Deeds", "desc": "Leveraged a powerful computer vision model to transcribe 300 year old documents into a digitized format. This data was then indexed, making search much more efficient."},
        {"title": "Radiologist Level Computer Vision Model", "desc": "We developed and trained a Computer Vision Model to read chest X-Rays, with an accuracy of x.xx %. This model has been made publically available in order to help trained professionals to be able to diagnose patients more efficiently. ", "link" : "https://huggingface.co/spaces/cfgpp/Danny_Net_Demo"}
    ]
    return render(request, "projects/projects.html", {
        "projects": projects,
    })

