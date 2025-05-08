from django.shortcuts import render

def home(request):
    projects = [
        {"title": "XX County Transcription of Deeds", "desc": "Leveraged a powerful computer vision model to transcribe 300 year old documents into a digitized format. This data was then indexed, making search much more efficient."},
        {"title": "Radiologist Level Computer Vision Model", "desc": "We developed and trained a Computer Vision Model to read chest X-Rays, with an accuracy of x.xx %. This model has been made publically available in order to help trained professionals to be able to diagnose patients more efficiently. ", "link" : "https://huggingface.co/spaces/cfgpp/Danny_Net_Demo"}
    ]
    about = "We are a team of Data Science Consultants eager to work on varying projects. From Healthcare to Computer Vision, Strick Technologies is here to help. Contact us to collaborate or consult!"
    contact_email = "your@email.com"
    return render(request, "projects/home.html", {
        "projects": projects,
        "about": about,
        "contact_email": contact_email
    })

def contact(request):
    return render(request, "projects/contact.html")

def about(request):
    return render(request, "projects/about.html")

def projects(request):
    projects = [
        {"title": "XX County Transcription of Deeds", "desc": "Leveraged a powerful computer vision model to transcribe 300 year old documents into a digitized format. This data was then indexed, making search much more efficient."},
        {"title": "Radiologist Level Computer Vision Model", "desc": "We developed and trained a Computer Vision Model to read chest X-Rays, with an accuracy of x.xx %. This model has been made publically available in order to help trained professionals to be able to diagnose patients more efficiently. ", "link" : "https://huggingface.co/spaces/cfgpp/Danny_Net_Demo"}
    ]
    about = "We are a team of Data Science Consultants eager to work on varying projects. From Healthcare to Computer Vision, Strick Technologies is here to help. Contact us to collaborate or consult!"
    contact_email = "your@email.com"
    return render(request, "projects/projects.html", {
        "projects": projects,
        "about": about,
        "contact_email": contact_email
    })

