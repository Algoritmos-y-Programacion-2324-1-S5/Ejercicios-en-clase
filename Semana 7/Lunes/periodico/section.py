class Section:
    def __init__(self, id, name, employees, articles):
        self.id = id
        self.name = name
        self.employees = employees
        self.articles = articles

    def show_section(self):
        print(f"***** SECTION {self.name} *****")
        print(f"Employees:")
        for employee in self.employees:
            print(employee.show_employee())
        print("Articles: ")
        for article in self.articles:
            print(article.show_article())