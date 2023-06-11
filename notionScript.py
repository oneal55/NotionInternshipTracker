from git import Repo
import os

PittURL = "https://github.com/pittcsc/Summer2024-Internships.git"
Repo.clone_from(PittURL, "pittFolder")





for root, dirs, files in os.walk("pittFolder", topdown=False):
    for name in files:
        os.remove(os.path.join(root, name))
    for name in dirs:
        os.rmdir(os.path.join(root, name))

os.rmdir("pittFolder")