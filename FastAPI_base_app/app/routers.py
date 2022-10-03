from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def read_root():  # noqa: D103
    return {"title": "This will be the Postogram main page"}


@router.get("/posts/{post_id}")
async def read_post(post_id: int):  # noqa: D103
    return {"post_id": post_id}


@router.get("/users/{user_id}/posts/{post_id}")
async def read_user_post(  # noqa: D103
    user_id: str, post_id: int, q: str | None = None, short: bool = False
):
    post = {"post_id": post_id, "owner_id": user_id}
    if q:
        post.update({"q": q})
    if not short:
        post.update(
            {"description": "This is an amazing post that has a long description"}
        )
    return post


@router.get("/users/{user_id}/list")
async def read_user_list(  # noqa: D103
    user_id: str, q: str | None = None, short: bool = False
):
    loclist = {"owner": user_id, "locations": ["1703"]}
    if q:
        loclist.update({"q": q})
    if not short:
        loclist.update(
            {"locations": ["1703", "Shamrock"]}
        )
    return loclist
