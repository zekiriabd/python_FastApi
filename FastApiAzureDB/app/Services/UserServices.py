from sqlalchemy import create_engine, and_, text
from sqlalchemy.orm import sessionmaker

from app.Models.UserDto import UserDto
from app.Models.User import User
from app.Models.UserDto import CredentialModel

server = 'softwebazuresqlserver.database.windows.net'
database = 'fastapi-database'
username = 'softwe3admin'
password = 'Talage2002.'

connection_string = f"mssql+pyodbc://{username}:{password}@{server}/{database}?driver=ODBC+Driver+17+for+SQL+Server"
engine = create_engine(connection_string, echo=True)

Session = sessionmaker(bind=engine)
session = Session()


class UserServices:

    def get_user_by_credential(self, credential: CredentialModel) -> User:
        return (session.query(User)
                .filter(and_(User.name == credential.username, User.password == credential.password))
                .first())

    async def get_users(self) -> list[UserDto]:
        users = session.query(User).all()
        return [UserDto.from_orm(user) for user in users]

    async def get_user_byid(self, user_id: int) -> UserDto:
        user = session.query(User).filter_by(id=user_id).first()
        return UserDto.from_orm(user)

    async def delete_user(self, user_id: int) -> bool:
        user = session.query(User).filter_by(id=user_id).first()
        if user:
            session.delete(user)
            session.commit()
            return True
        return False

    async def set_user(self, user) -> bool:
        userDB = User.from_dto(user)
        session.add(userDB)
        session.commit()
        return True

    async def upd_user(self, user: UserDto) -> bool:
        userDB = session.query(User).filter_by(id=user.id).first()
        if userDB:
            userDB.name = user.name
            userDB.age = user.age
            userDB.city = user.city
            session.commit()
            return True
        return False
