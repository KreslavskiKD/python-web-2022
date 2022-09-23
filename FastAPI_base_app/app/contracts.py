from pydantic import BaseModel


class List(BaseModel):          # this is a list of favourite places
    """Contract for list"""

    owner: int              # owner id
    locations: list[str]    # here should later be some list of locations 
                            # that are geolocation class


class Post(BaseModel):          # this is post in Postogram
    """Contract for post."""

    title: str
    time: str               # here should later be some time format
    description: str
    locations: List          
    references: str         # here should be later list of users and companies
