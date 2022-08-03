import uuid
from decimal import Decimal
from enum import Enum
from typing import Tuple, Optional, List
from haversine import haversine
from models import ProjectCatalogueEntry, User, UserProjectSubscription
from enums import DistanceUnit, Limit

"""
TODO - this file should be split up into concern-specific managers. 
e.g. user model manager, user project api manager, project catalog model manager, model utils
"""

def generate_uuid():
    return uuid.uuid1()


def calculate_distance(
    user_lat_long: Tuple, 
    project_lat_long: Tuple, 
    distance_unit: Optional[DistanceUnit]=DistanceUnit.MILES,
) -> (int, tuple):
    """
    user_lat_long :: tuple consisting two decimal values, the user latitude and user longitude
    project_lat_log :: tuple consisting two decimal values, the project latitude and project longitude
    distance_unit :: enum value indicating the unit we're calculating in (miles or kilometers)

    haversine package is python implementation of movable-type.co.uk/scripts/latlong.html

    e.g.
    berkeley = (37.871666, -122.272781) # lat, long
    oakland = (37.804363, -122.271111) # lat, long
    haversine(berkeley, oakland, unit=DistanceUnit.MILES.value)
    outputs 4.651087188124635

    TODO - add validations
    """
    distance = haversine(user_lat_long, project_lat_long, unit=distance_unit.value)
    return (distance, distance_unit)


def fetch_projects_within_radius(
    center_lat_long: Tuple, 
    radius: int, 
    radius_distance_unit: Optional[DistanceUnit]=DistanceUnit.MILES,
) -> List:
    """
    This would probably need to be optimized out the gate. should at the least profile the query to gauge it

    Potential approaches and/or improvements:
    * set upper_limit on num of projects to return, 
      batch query ProjectCatalogueEntry items by descending int ID in sets of 100 until we hit upper limit
    * client side caching {uuid, name, lat, long, distance, retrieved_at}
    * add another field on the ProjectCatalogueEntry table that serves as a secondary location bucket, e.g. country code
      so we can limit query to only select from rows in the same country as the user
    """
    projects = (
        ProjectCatalogueEntry
        .query
        .filter(ProjectCatalogueEntry.deleted_at.is_(None))
        .filter(ProjectCatalogueEntry.distance_to_coordinates(user_coordinates=center_lat_long, distance_unit=radius_distance_unit)<=radius)
        .all()
    )
    return projects


def fetch_recently_updated_projects(
    limit: Optional[Enum]=Limit.LOW,
) -> List:
    """
    Return most recently created entries in Project Catalogue.
    """
    projects = (
        ProjectCatalogueEntry
        .query
        .filter(ProjectCatalogueEntry.deleted_at.is_(None))
        .order_by(ProjectCatalogueEntry.project_catalogue_entry_id.desc())
        .limit(limit.value)
        .all()
    )
    return projects


def get_country_code_from_coordinates(
    lat_long_coordinates: Tuple,
) -> str:
    """
    placeholder. would be nice-to-have country code as additional filter param on user and catalogue entry queries
    """
    pass


def create_user(
    email: str,
    firstname=None,
    lastname=None,
    latitude=None,
    longitude=None,
    created_at=None,
) -> User:
    """
    insert user to User table. 
    TODO: auth flow
    """


def create_or_update_catalogue_entry(
    project_catalogue_entry_uuid: str,
    name=None,
    latitude=None,
    longitude=None,
    created_at=None,
) -> ProjectCatalogueEntry:
    """
    UUID is persistent, source of truth for uniqueness. UUID datatype at DB level, str from api
    
    This is intended to be called by an async job that updates the append-only ProjectCatalogueEntry table values.

    if uuid:
        it's an update.
        fetch existing row values for uuid, do field diff, if diff delete existing row and create new row in ProjectCatalogueEntry with updated values
    if no uuid:
        it's a create.
        generate uuid, insert values to ProjectCatalogueEntry table
    """
    pass


def subscribe_user_to_project(
    user_id: int,
    project_catalogue_entry_uuid: str,
    created_at=None,
) -> UserProjectSubscription:
    """
    - check if undeleted subscription exists for user_id+project_catalogue_entry_uuid pair
    - if no undeleted subscription exists, insert to UserProjectSubscription join table
    - task to email users with project updates will read from this table, then the catalogue and user tables
    """
    pass




