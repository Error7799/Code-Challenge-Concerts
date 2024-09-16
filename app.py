from models import Band, Venue, Concert
from database_setup import session

# You can use this file to test functionality by querying and interacting with your database.
if __name__ == '__main__':
    # Example: Querying the first Band
    first_band = session.query(Band).first()
    print(f"First Band: {first_band.name}")

    # Test methods, create instances, etc.
    band = Band(name="The Rockers", hometown="New York")
    venue = Venue(title="Madison Square Garden", city="New York")
    concert = Concert(band=band, venue=venue, date="2024-09-15")

    session.add_all([band, venue, concert])
    session.commit()

    # Try calling one of the methods
    print(concert.introduction())
