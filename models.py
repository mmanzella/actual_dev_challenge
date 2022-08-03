from sqlalchemy import Column
from typing import Tuple

from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import declarative_base
from sqlalchemy.sql.sqltypes import VARCHAR, INT, DECIMAL, DATETIME
from sqlalchemy.dialects.postgresql import UUID


Base = declarative_base()


class User(Base):
    """
    a single user of the app.
    TODO: auth flow
    """
    __tablename__ = 'users'
    user_id = Column(INT(), primary_key=True)
    email = Column(VARCHAR(30))
    firstname = Column(VARCHAR(30), nullable=True, default=None)
    lastname = Column(VARCHAR(30), nullable=True, default=None)
    latitude = Column(DECIMAL(10, 8))
    longitude = Column(DECIMAL(11, 8))
    country_code = Column(VARCHAR(10), nullable=True, default=None)
    distance_unit = Column(VARCHAR(10), nullable=True, default=None)
    created_at = Column(DATETIME(6))
    deleted_at = Column(DATETIME(6), nullable=True, default=None)


class ProjectCatalogueEntry(Base):
    """
    a single project.
    append only. projects unique by uuid.
    """
    __tablename__ = 'project_catalogue'
    project_catalogue_entry_id = Column(INT(), primary_key=True)
    project_catalogue_entry_uuid = Column(UUID(36))
    name = Column(VARCHAR(30), nullable=True)
    latitude = Column(DECIMAL(10, 8))
    longitude = Column(DECIMAL(11, 8))
    country_code = Column(VARCHAR(10), nullable=True, default=None)
    created_at = Column(DATETIME(6))
    deleted_at = Column(DATETIME(6), nullable=True, default=None)

    @hybrid_property
    def distance_to_coordinates(self, user_coordinates: Tuple):
        from manager import calculate_distance
        return calculate_distance(user_coordinates, (self.latitude, self.longitude))


class UserProjectSubscription(Base):
    """
    join table representing a user subscribed to a unique project.
    """
    __tablename__ = 'user_project_subscriptions'
    user_project_subscription_id = Column(INT(), primary_key=True)
    user_id = Column(INT())
    project_catalogue_entry_uuid = Column(UUID(36))
    created_at = Column(DATETIME(6))
    deleted_at = Column(DATETIME(6), nullable=True, default=None)
