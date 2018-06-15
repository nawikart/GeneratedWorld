import django
import datetime
from django.db.models import Count, Sum
import apps.generated_world.models as m

django.setup()

print()

#1. Takes in a string (department) and returns the companies that have that department
def companies_of_department(department_name):
    for company in m.Company.objects.filter(departments__name=department_name):
        print('company --> id: {}, \t\t name: {}'.format(company.id, company.name))  

# companies_of_department('Finance')


#2. Finds all the people who are currently employed
def people_employed():
    for person in m.Person.objects.filter(jobs__is_employed = 1):
        print('person --> id: {} \t\t name: {}'.format(person.id, person.first))  

# people_employed()



#3. Finds all the people who currently play for a given club
def people_of_club(club_name):
    for person in m.Person.objects.filter(memberships__club__name = club_name, memberships__is_active = 1):
        print('person --> id: {} \t\t name: {}'.format(person.id, person.first))

# people_of_club('Alfano City Broncos')        



# 4. Finds all past addresses for a given person
def past_addresses_of_person(person_id):
    for address in m.Address.objects.filter(person_id=person_id, is_current=0):
        print('address --> id: {} \t\t street: {}'.format(address.id, address.street))

past_addresses_of_person(1)


# 5. Finds all the companies for a given industry
def companies_of_industry(industry):
    for listing in m.Listing.objects.filter(industry = industry):
        print('company --> id: {} \t name: {}'.format(listing.company.id, listing.company.name))

# companies_of_industry('Manufacturing')


# 6. Finds all the clubs for a given league
def clubs_of_league(league_id):
    for club in m.Club.objects.filter(league__id=league_id):
        print('club --> id: {} \t\t name: {}'.format(club.id, club.name))
        
# clubs_of_league(1)        



# 7. Finds the state with the most number of cities
def state_the_most_number_of_city():
    for state in m.State.objects.annotate(city_total=Count('cities')).order_by('-city_total')[:5]:
        print('state --> name: {} \t\t num of cities: {}'.format(state.name, state.city_total))

# state_the_most_number_of_city()



# 8. Finds the most populous state
def state_most_populous():
    for state in m.State.objects.annotate(populous=Sum('cities__population')).order_by('-populous')[:5]:
        print('state --> name: {} \t\t populous: {}'.format(state.name, state.populous))

# state_most_populous() 



# 9. Finds the total assets for a given industry
def total_assets_for_industry(industry):
    print('Total Assets: ', m.Company.objects.filter(listings__industry=industry).aggregate(total_assets=Sum('total_assets'))['total_assets'])

# total_assets_for_industry('Manufacturing')



# 10. Find the companies for a given industry after a certain date
def companies_of_industry_after_certain_date(industry, certain_date):
    for company in m.Company.objects.filter(listings__industry = industry, founded_on__gte = certain_date):
        print('company --> id: {} \t name: {}'.format(company.id, company.name))

companies_of_industry_after_certain_date('Manufacturing', datetime.date(1994,5,11))
