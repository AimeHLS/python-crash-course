# city_input = input("Choose a random city: ")
# country_input = input("And indicate its country: ")

def country_city(city, country, population=''):
    """A function that tell cities and their countries."""
    if population:
        capital = f"{city}, {country}, {population}"
    else:
        capital = f"{city}, {country}"
    return capital.title()

def city_population(city, country, population):
    """A test for city's population."""
    city_people = f"{city} {country} population: {population} people"
    return city_people.title()


class AnonymousSurvery:
    """Collect anonymous answers to a survey question."""

    def __init__(self,question):
        """Store a question, and prepare to store responses."""
        self.question = question
        self.responses = []

    def show_question(self):
        """Show survey question."""
        print(self.question)

    def store_response(self, new_response):
        """Store a single response to the survey."""
        self.responses.append(new_response)

    def show_results(self):
        """Show all the responses that have been given."""
        print("Survey results:")
        for response in self.responses:
            print(f"-{response}")


class Employee:
    """Store information about employee."""

    def __init__(self, first_name, last_name, annual_salary):
        """Initialize attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary
        self.raise_amount = 5000

    def give_raise(self, raise_amount=5000):
        """Take the annual salary by the given amount."""
        self.annual_salary += raise_amount
        return self.annual_salary

