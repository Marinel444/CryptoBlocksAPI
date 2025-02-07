from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from blocks.models import Block, Provider
from django.core.paginator import Paginator

router = APIRouter()


class RegisterUser(BaseModel):
    username: str
    password: str


class LoginUser(BaseModel):
    username: str
    password: str


class BlockResponse(BaseModel):
    id: int
    currency: str
    provider: str
    block_number: int
    created_at: str
    stored_at: str


@router.post("/register")
def register(user: RegisterUser):
    if User.objects.filter(username=user.username).exists():
        raise HTTPException(status_code=400, detail="User already exists")

    new_user = User.objects.create_user(username=user.username, password=user.password)
    return {"message": "User created", "user_id": new_user.id}


@router.post("/login")
def login(user: LoginUser):
    user_obj = authenticate(username=user.username, password=user.password)
    if not user_obj:
        raise HTTPException(status_code=400, detail="Invalid credentials")

    return {"message": "Login successful"}


@router.get("/blocks", response_model=list[BlockResponse])
def get_blocks(currency: str = None, provider: str = None, page: int = 1):
    queryset = Block.objects.all()

    if currency:
        queryset = queryset.filter(currency__symbol=currency.upper())

    if provider:
        queryset = queryset.filter(provider__name=provider)

    paginator = Paginator(queryset, 5)
    page_obj = paginator.get_page(page)

    return [
        BlockResponse(
            id=block.id,
            currency=block.currency.name,
            provider=block.provider.name,
            block_number=block.block_number,
            created_at=block.created_at.isoformat(),
            stored_at=block.stored_at.isoformat(),
        )
        for block in page_obj
    ]


@router.get("/blocks/{block_id}", response_model=BlockResponse)
def get_block(block_id: int):
    try:
        block = Block.objects.get(id=block_id)
        return BlockResponse(
            id=block.id,
            currency=block.currency.name,
            provider=block.provider.name,
            block_number=block.block_number,
            created_at=block.created_at.isoformat(),
            stored_at=block.stored_at.isoformat(),
        )
    except Block.DoesNotExist:
        raise HTTPException(status_code=404, detail="Block not found")
