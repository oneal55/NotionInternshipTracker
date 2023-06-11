from git import Repo
import os

PITT_URL = "https://github.com/pittcsc/Summer2024-Internships.git"
Repo.clone_from(PITT_URL, "Summer2024-Internships")


for root, dirs, files in os.walk("Summer2024-Internships", topdown=False):
    for name in files:
        os.remove(os.path.join(root, name))
    for name in dirs:
        os.rmdir(os.path.join(root, name))

os.rmdir("pittFolder")
