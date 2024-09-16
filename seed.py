from models import Band, Venue, Concert
from database_setup import session

def seed_data():
    band1 = Band(name="The Rockers", hometown="New York")
    band2 = Band(name="The Jazzers", hometown="Chicago")
    
    venue1 = Venue(title="Madison Square Garden", city="New York")
    venue2 = Venue(title="Chicago Theatre", city="Chicago")
    
    concert1 = Concert(band=band1, venue=venue1, date="2024-09-15")
    concert2 = Concert(band=band2, venue=venue2, date="2024-09-20")
    
    session.add_all([band1, band2, venue1, venue2, concert1, concert2])
    session.commit()

if __name__ == '__main__':
    seed_data()
