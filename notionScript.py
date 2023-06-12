from git import Repo
import os

PITT_URL = "https://github.com/pittcsc/Summer2024-Internships.git"
PATH = "Summer2024-Internships"
REAME = "README.md"


def parseLine(line: str):
    if (line.count("|") != 4):
        return ()
    line = line[1:]
    name = line[:line.find('|')]
    line = line[line.find('|') + 1:]
    location = line[:line.find('|')]
    line = line[line.find('|') + 1:]
    roles = line[:line.find('|')]
    return (name, location, roles)


def main():
    Repo.clone_from(PITT_URL, "Summer2024-Internships")

    path = os.path.join(PATH, REAME)
    if not os.path.exists(path):
        return exit()

    file1 = open(path, 'r')
    lines = file1.readlines()
    startPoint = -1
    for i, line in enumerate(lines):
        if line == "| Name | Location | Notes |\n":
            startPoint = i + 2
            break
    if startPoint == -1:
        return exit()
    rows = []
    while startPoint < len(lines) and lines[startPoint] != "\n":
        rows.append(lines[startPoint])
        startPoint += 1

    parsedRows = list(map((parseLine), rows))
    print(parsedRows)

    exit()


def exit():
    for root, dirs, files in os.walk(PATH, topdown=False):
        for name in files:
            os.remove(os.path.join(root, name))
        for name in dirs:
            os.rmdir(os.path.join(root, name))

    os.rmdir(PATH)
    return 0


if __name__ == "__main__":
    main()
