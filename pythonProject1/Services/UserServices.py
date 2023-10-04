from typing import List
import pandas as pd
from Models.UserModel import UserModel

class UserServices:

    async def get_users(self) -> List[UserModel]:
        df = pd.read_json('./Data/Users.json')
        users = [UserModel(**x) for x in df.to_dict(orient='records')]
        return users

    async def get_user_byid(self, user_id: int) -> UserModel:
        df = pd.read_json('./Data/Users.json')
        row = df[df['id'] == user_id].iloc[0]
        return  UserModel(**row)

    async def set_user(self, user: UserModel) -> bool:
        df = pd.read_json('./Data/Users.json')
        row = pd.Series({'id': user.id, 'name': user.name, 'age': user.age, 'city': user.city})
        df = df.append(row)
        df.to_json('./Data/Users.json')
        return True

    async def upd_user(self, user: UserModel) -> bool:
        df = pd.read_json('./Data/Users.json')
        row = pd.Series({'id': user.id, 'name': user.name, 'age': user.age, 'city': user.city})
        df.update(row)
        df.to_json('./Data/Users.json')
        return True

    async def delete_user(self, user_id: int) -> bool:
        df = pd.read_json('./Data/Users.json')
        df.drop(df[df['id'] == user_id].index, inplace=True)
        df.to_json('./Data/Users.json')
        return True