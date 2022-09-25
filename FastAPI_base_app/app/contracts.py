from pydantic import BaseModel


class Locations(BaseModel):  # this is a list of favourite places
    """Contract for Locations list."""

    owner: str  # owner id
    locations: list[
        str
    ]  # here should later be some list of locations that are geolocation class


class PostModel(BaseModel):  # this is post in Postogram
    """Contract for post."""

    pid: int
    title: str
    time: str  # here should later be some time format
    description: str
    locations: Locations
    references: str  # here should be later list of users and companies
