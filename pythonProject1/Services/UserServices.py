from typing import List
import pandas as pd
from Models.UserModel import UserModel

class UserServices:
    FILE_NAME = './Data/Users.json'
    async def get_users(self) -> List[UserModel]:
        df = pd.read_json(self.FILE_NAME)
        users = [UserModel(**x) for x in df.to_dict(orient='records')]
        return users

    async def get_user_byid(self, user_id: int) -> UserModel:
        df = pd.read_json(self.FILE_NAME)
        row = df[df['id'] == user_id].iloc[0]
        return UserModel(**row)

    async def delete_user(self, user_id: int) -> bool:
        df = pd.read_json(self.FILE_NAME)
        df.drop(df[df['id'] == user_id].index, inplace=True)
        df.to_json(self.FILE_NAME)
        return True

    async def set_user(self, user: UserModel) -> bool:
        df = pd.read_json(self.FILE_NAME)
        df.loc[len(df)] = pd.Series({'id': user.id, 'name': user.name, 'age': user.age, 'city': user.city})
        df.to_json(self.FILE_NAME)
        return True

    async def upd_user(self, user: UserModel) -> bool:
        df = pd.read_json(self.FILE_NAME)
        df.loc[df['id'] == user.id, ['id', 'name', 'age', 'city']] = [user.id, user.name, user.age, user.city]
        df.to_json(self.FILE_NAME)
        return True