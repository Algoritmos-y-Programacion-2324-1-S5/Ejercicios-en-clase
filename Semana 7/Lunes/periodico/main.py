from employee import Writer, Boss
from section import Section
from article import Article


def create_sport_employees(list_employee):
    list_employee.append(Boss(1, "Christian", 5123456))
    list_employee.append(Writer(2, "Antonio", 24464173))
    list_employee.append(Writer(3, "Ana", 24555674))
    list_employee.append(Writer(4, "Sofia", 24285567))
    list_employee.append(Writer(5, "Henry", 26874598))
    list_employee.append(Writer(6, "Salome", 24123456))

def create_cinema_employees(list_employee):
    list_employee.append(Writer(2, "Ricardo", 24464173))
    list_employee.append(Writer(3, "Susana", 24555674))
    list_employee.append(Writer(5, "Gabriel", 26874598))
    list_employee.append(Boss(1, "Pedro", 5123456))

def create_sections(list_sections, employees_sports, employees_cinema,articles_sport,articles_cinema):
    list_sections.append(Section(1, "Sports", employees_sports,articles_sport))
    list_sections.append(Section(2, "Cinema", employees_cinema,articles_cinema))

def create_sport_articles(sport_articles,writer):
    sport_articles.append(Article("Los Leones ganaron ayer","Quedo 6-3", "kjkjkjasjkasjkasjsa",[],"Hoy",writer))
    sport_articles.append(Article("El Real madrid empato","Quedo 1-1", "kjkjkjasjkasjkasjsa",[],"Hoy",writer))

def main():
    employees_sport = []
    employees_cinema = []

    articles_sport = []
    articles_cinema = []

    sections = []
    create_sport_employees(employees_sport)
    create_cinema_employees(employees_cinema)
    create_sport_articles(articles_sport, employees_sport[2])
    create_sections(sections,employees_sport,employees_cinema,articles_sport,articles_cinema)
    while True:
        option = input("Please enter a valid option \n1-Exit\n2-Show sections\n")
        if option == "1":
            break
        elif option == "2":
            for section in sections:
                section.show_section()

main()