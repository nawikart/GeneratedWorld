import django
import apps.generated_world.models as m

django.setup()


#1. Returns all the state capitals
def state_capitals():
    for city in m.City.objects.filter(is_capital = 1):
        print('state: {}  \t city: {}'.format(city.state.name, city.name))

# state_capitals():


#2. Returns all cities in reverse order by population
def cities_in_reverse_order_by_population():
    for city in m.City.objects.all().order_by('-population'):
        print('city: {} \t population: {}'.format(city.name, city.population))

# cities_in_reverse_order_by_population()



#3. Takes in a string (sport) and returns the leagues for that sport
def leagues_by_sport(sport):
    for league in m.League.objects.filter(sport=sport):
        print('league: {}'.format(league.name))

# leagues_by_sport('Baseball')



#4. Takes in a string (name_fragment) and returns the clubs that contain that string in their name
def clubs_by_name(name):
    for club in m.Club.objects.filter(name__contains=name):
        print('club: {}'.format(club.name))

# clubs_by_name('alfano')


#5. Takes in a string (name_fragment) and returns the companies that do not contain that string in their name
def companies_name_not_contains_of(name):
    for company in m.Company.objects.exclude(name__contains=name):
        print('company: {}'.format(company.name))    

# companies_name_not_contains_of('Corp')


#6. Takes in a float and returns the companies that have a net income below that float
def companies_net_income_lt(net_income):
    for company in m.Company.objects.filter(net_income__lt = net_income):
        print('company: {} \t net income: {}'.format(company.name, company.net_income))    

# companies_net_income_lt(-2000)


#7. Takes in an integer and returns the streets that match that integer
def streets_match_of(street_no):
    for address in m.Address.objects.filter(street__startswith=street_no):
        print('street: {}'.format(address.street))

# streets_match_of(4435)


#8. Takes in two integers and finds the cities with a population between those two integers
def cities_population_between_in(min, max):
    for city in m.City.objects.filter(population__gte=min, population__lte=max).order_by('population'):
        print('city: {} \t population: {}'.format(city.name, city.population))

# cities_population_between_in(30000, 30500)


#9. Takes in a cardinal direction and returns the cities that contain that are named accordingly
def cities_contains_cardinal(cardinal):
    for city in m.City.objects.filter(name__startswith = cardinal):
        print('city: {}'.format(city.name))    

# cities_contains_cardinal('North')


#10. Takes in a company association and returns the companies that contain that company association
def companies_by_association(association):
    for company in m.Company.objects.filter(name__endswith = association):
        print('company: {}'.format(company.name))
        
companies_by_association ('LLC')