import django
from django.db.models import Count, Sum
import apps.generated_world.models as m

django.setup()
# Create a function that:

#1. Returns the states in descending order by the number of cities they have
def state_the_most_number_of_city():
    for state in m.State.objects.annotate(city_total=Count('cities')).order_by('-city_total')[:5]:
        print('state --> name: {} \t\t num of cities: {}'.format(state.name, state.city_total))

# state_the_most_number_of_city()



#2. Returns the clubs that have the most past memberships ????
def clubs_most_inactive_memberships():
    for club in m.Club.objects.annotate(total=Count('memberships__person')).filter(memberships__is_active=0).order_by('-total')[:5]:
        print('2. club --> name: {} \t\t num of clubs: {}'.format(club.name, club.total))

# clubs_most_inactive_memberships()   



# 3. Returns the exchanges in descending order by the number of listings they have
def exchanges_desc_by_num_listings():
    for exchange in m.Exchange.objects.annotate(total=Count('listings')).order_by('-total')[:5]:
        print('exchange --> name: {} \t\t num of listings: {}'.format(exchange.name, exchange.total))

# exchanges_desc_by_num_listings()   



# 4. Returns the companies with the most number of departments
def companies_most_number_of_departments():
    for company in m.Company.objects.annotate(total=Count('departments')).order_by('-total')[:5]:
        print('company --> name: {} \t\t num of departments: {}'.format(company.name, company.total))    

# companies_most_number_of_departments()



# 5. Returns the cities with the most employed people
def cities_with_the_most_employed_people():
    for city in m.City.objects.annotate(total=Count('addresses__person')).filter(addresses__person__jobs__is_employed = 1).order_by('-total')[:5]:
        print('city: {} \t total: {}'.format(city.name, city.total))

# cities_with_the_most_employed_people()



# 6. Returns the most profitable industries
def most_profitable_industries():
    for industry in m.Listing.objects.annotate(net_income_total=Sum('listings__company__net_income')).order_by('-net_income_total')[:5]:
        print('industry: {} \t total: {}'.format(industry.name, industry.net_income_total))

# most_profitable_industries()




# 7. Returns the leagues in order of past membership
def leagues_order_past_membership():
    for league in m.League.objects.annotate(total=Count('clubs__memberships__person')).filter(clubs__memberships__is_active=0).order_by('-total')[:5]:
        print('2. league --> name: {} \t\t num of leagues: {}'.format(league.name, league.total))

# leagues_order_past_membership()


# 8. Returns the industries with the highest rate of unemployment
# def industries_highest_rate_of_unemployment



# 9. Returns the cities with the most vacant addresses
def cities_with_the_most_vacant_addresses():
    for city in m.City.objects.annotate(total=Count('addresses__person')).order_by('total')[:5]:
        print('city: {} \t total: {}'.format(city.name, city.total))

# cities_with_the_most_vacant_addresses()


# 10. Returns the states in descending order by revenue ::: company gak ada alamat jadi gak bisa disambungkan ke state
def states_in_descending_order_by_revenue():