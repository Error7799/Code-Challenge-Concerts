from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database_setup import Base

class Band(Base):
    __tablename__ = 'bands'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    hometown = Column(String)
    concerts = relationship('Concert', back_populates='band')

    def concerts(self):
        return self.concerts

    def venues(self):
        return {concert.venue for concert in self.concerts}

    def play_in_venue(self, venue, date):
        new_concert = Concert(band_id=self.id, venue_id=venue.id, date=date)
        session.add(new_concert)
        session.commit()

    def all_introductions(self):
        return [concert.introduction() for concert in self.concerts]

    @classmethod
    def most_performances(cls):
        bands = session.query(cls).all()
        return max(bands, key=lambda band: len(band.concerts))


class Venue(Base):
    __tablename__ = 'venues'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    city = Column(String)
    concerts = relationship('Concert', back_populates='venue')

    def concerts(self):
        return self.concerts

    def bands(self):
        return {concert.band for concert in self.concerts}

    def concert_on(self, date):
        return session.query(Concert).filter_by(venue_id=self.id, date=date).first()

    def most_frequent_band(self):
        band_counts = {}
        for concert in self.concerts:
            band_counts[concert.band] = band_counts.get(concert.band, 0) + 1
        return max(band_counts, key=band_counts.get)


class Concert(Base):
    __tablename__ = 'concerts'
    id = Column(Integer, primary_key=True)
    band_id = Column(Integer, ForeignKey('bands.id'))
    venue_id = Column(Integer, ForeignKey('venues.id'))
    date = Column(String)  # For simplicity, date as string
    band = relationship("Band", back_populates="concerts")
    venue = relationship("Venue", back_populates="concerts")

    def band(self):
        return self.band

    def venue(self):
        return self.venue

    def hometown_show(self):
        return self.band.hometown == self.venue.city

    def introduction(self):
        return f"Hello {self.venue.city}!!!!! We are {self.band.name} and we're from {self.band.hometown}"
