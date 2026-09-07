from fastapi import APIRouter, HTTPException, Response, status

from app.models import User
from app.schemas import UserCreate, UserResponse, UserUpdate

router = APIRouter(prefix="/users", tags=["users"])

_users: dict[int, User] = {}
_next_user_id = 1


def _get_user_or_404(user_id: int) -> User:
    user = _users.get(user_id)
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user


@router.post("", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def create_user(payload: UserCreate) -> User:
    """Create and return an in-memory user."""
    global _next_user_id
    user = User(id=_next_user_id, **payload.model_dump())
    _users[user.id] = user
    _next_user_id += 1
    return user


@router.get("", response_model=list[UserResponse])
def list_users() -> list[User]:
    """Return every user created while this process is running."""
    return list(_users.values())


@router.get("/{user_id}", response_model=UserResponse)
def get_user(user_id: int) -> User:
    return _get_user_or_404(user_id)


@router.put("/{user_id}", response_model=UserResponse)
def replace_user(user_id: int, payload: UserUpdate) -> User:
    """Replace every mutable property of an existing user."""
    _get_user_or_404(user_id)
    user = User(id=user_id, **payload.model_dump())
    _users[user_id] = user
    return user


@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: int) -> Response:
    _get_user_or_404(user_id)
    del _users[user_id]
    return Response(status_code=status.HTTP_204_NO_CONTENT)
