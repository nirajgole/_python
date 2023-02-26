from fastapi import APIRouter, Depends
import schemas
from db import Base, SessionLocal, engine
from user import User
from sqlalchemy.orm import Session

user = APIRouter()
Base.metadata.create_all(engine)


def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()


@user.get('/users')
async def fetch_users(session: Session = Depends(get_session)):
    data = session.query(User).all()
    return data


@user.get('/{id}')
async def fetch_users(id: int, session: Session = Depends(get_session)):
    return session.query(User).get(id)


@user.post('/users')
async def create_user(user: schemas.User, session: Session = Depends(get_session)):
    # implement email already exists
    item = User(email=user.email, password=user.password, name=user.name)
    session.add(item)
    session.commit()
    session.refresh(item)
    return item


@user.put('/{id}')
async def update_user(id: int, user: schemas.User, session: Session = Depends(get_session)):
    item = session.query(User).get(id)
    item.name = user.name
    # implement email already exists
    item.email = user.email
    item.password = user.password
    session.commit()
    return item


@user.delete('/{id}')
async def delete_user(id: int, session: Session = Depends(get_session)):
    item = session.query(User).get(id)
    session.delete(item)
    session.commit()
    session.close()
    return 'Item was deleted.'


# exception handling
# error handling
# dockerize app -> Dockerfile, docker compose
# password encryption/decryption
# user login
