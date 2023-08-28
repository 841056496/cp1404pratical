import datetime
from project import Project


def load_projects(filename):
    projects = []
    with open(filename, 'r') as file:
        next(file)  # Skip header line
        for line in file:
            name, start_date, priority, cost_estimate, completion_percentage = line.strip().split('\t')
            project = Project(name, start_date, priority, cost_estimate, completion_percentage)
            projects.append(project)
    return projects


def save_projects(filename, projects):
    with open(filename, 'w') as file:
        file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
        for project in projects:
            line = f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t{project.priority}\t{project.cost_estimate}\t{project.completion_percentage}\n"
            file.write(line)


def display_projects(projects):
    print("Incomplete projects:")
    for project in sorted([p for p in projects if p.completion_percentage < 100], key=lambda x: x.priority):
        print(f"  {project}")

    print("Completed projects:")
    for project in sorted([p for p in projects if p.completion_percentage == 100], key=lambda x: x.priority):
        print(f"  {project}")


def filter_projects_by_date(projects):
    date_input = input("Show projects that start after date (dd/mm/yy): ")
    target_date = datetime.datetime.strptime(date_input, "%d/%m/%Y").date()

    for project in sorted([p for p in projects if p.start_date > target_date], key=lambda x: x.start_date):
        print(project)


def add_new_project(projects):
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yy): ")
    priority = input("Priority: ")
    cost_estimate = input("Cost estimate: ")
    completion_percentage = input("Percent complete: ")

    new_project = Project(name, start_date, priority, cost_estimate, completion_percentage)
    projects.append(new_project)


def update_project(projects):
    for index, project in enumerate(projects):
        print(f"{index} {project}")

    project_choice = int(input("Project choice: "))
    selected_project = projects[project_choice]

    print(selected_project)
    new_percentage = input("New Percentage: ")
    new_priority = input("New Priority: ")

    if new_percentage:
        selected_project.completion_percentage = int(new_percentage)

    if new_priority:
        selected_project.priority = int(new_priority)


def main():
    filename = "project.txt"
    projects = load_projects(filename)

    while True:
        print("\nMenu:")
        print("D: Display projects")
        print("F: Filter projects by date")
        print("A: Add a new project")
        print("U: Update a project")
        print("S: Save changes")
        print("Q: Quit")
        choice = input("Your choice: ").upper()

        if choice == 'D':
            display_projects(projects)
        elif choice == 'F':
            filter_projects_by_date(projects)
        elif choice == 'A':
            add_new_project(projects)
        elif choice == 'U':
            update_project(projects)
        elif choice == 'S':
            save_projects(filename, projects)
        elif choice == 'Q':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
