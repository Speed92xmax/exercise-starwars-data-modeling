import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()


class User (Base) :
    __tablename__="user"

    id = Column ( Integer, primary_key=True)
    name = Column (String(100),nullable=True)
    email = Column (String(100),nullable=False)
    password = Column (String(100),nullable=False)
    favorite_list = relationship("favorite_list")

class FavoriteList (Base):
    __tablename__ = "favorite_list"

    id = Column ( Integer, primary_key=True)
    user_id = Column (Integer, ForeignKey("user.id"),nullable=False)
    planet_id = Column (Integer, ForeignKey("planet.id"),nullable=False)
    character_id = Column (Integer, ForeignKey("character.id"),nullable=False)
    vehicle_id = Column (Integer, ForeignKey("vechicle.id"),nullable=False)


class Character (Base):
    __tablename__="character"

    id = Column ( Integer, primary_key=True)
    msg = Column (String(100),nullable=False)
    properties_id = Column (Integer, ForeignKey("properties_char.id"),nullable=False)
    favorite_list = relationship("favorite_list")

class PropertiesChar (Base):

    __tablename__="properties_char"

    id = Column ( Integer, primary_key=True)
    height = Column(Integer,nullable=True)
    mass = Column(Integer,nullable=True)
    name = Column(String(100),nullable=True)
    hair_color = Column(String(100),nullable=True)
    home_planet = relationship("planet_list")
    vechile = relationship("vehicle_list")
    character= relationship("character")

class Vehicle (Base):
    __tablename__="vehicle"

    id = Column ( Integer, primary_key=True)
    msg = Column (String(100),nullable=False)
    properties_id = Column (Integer, ForeignKey("properties_vehicle.id"),nullable=False)
    favorite_list = relationship("favorite_list")
    vehicle_list = relationship("vehicle_list")

class PropertiesVehicle (Base):

    __tablename__="properties_vehicle"

    id = Column ( Integer, primary_key=True)
    cost_in_credits = Column(Integer,nullable=True)
    lenght = Column(Integer,nullable=True)
    model = Column(String(100),nullable=True)
    vehicle_class = Column(String(100),nullable=True)
    consumables = Column(String(100),nullable=True )
    manufacturer = Column(String(100),nullable=True )
    name = Column(String(100),nullable=True)
    vechile = relationship("vehicle")

class VehicleList (Base):
    __tablename__="vehicle_list"

    id = Column ( Integer, primary_key=True)
    vehicle_id = Column ( Integer, ForeignKey("vehicle.id"))
    character_id = Column ( Integer, ForeignKey("character.properties_char.id"))


class Planet (Base):
    __tablename__="planet"

    id = Column ( Integer, primary_key=True)
    msg = Column (String(100),nullable=False)
    properties_id = Column (Integer, ForeignKey("properties_planet.id"),nullable=False)
    favorite_list = relationship("favorite_list")
    planet_list = relationship("planet_list")

class PropertiesPlanet (Base):

    __tablename__="properties_planet"

    id = Column ( Integer, primary_key=True)
    diameter= Column(Integer,nullable=True)
    rotation_period= Column(Integer,nullable=True)
    orbital_period= Column(Integer,nullable=True)
    gravity = Column(String(100),nullable=True)
    population= Column(Integer,nullable=True)
    climate = Column(String(100),nullable=True)
    name = Column(String(100),nullable=True)
    planet = relationship("planet")

class PlanetList (Base):
    __tablename__="planet_list"

    id = Column ( Integer, primary_key=True)
    planet_id = Column ( Integer, ForeignKey("planet.id"))
    character_id = Column ( Integer, ForeignKey("character.properties_char.id"))




render_er(Base,'diagam.png')

