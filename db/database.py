from sqlalchemy import (
    create_engine,
    MetaData,
    Table,
    Column,
    Integer,
    String,
    BigInteger,
)

from config import MYSQL_URL

engine = create_engine(MYSQL_URL)
meta = MetaData()


class UsersManager:
    def __init__(self, engine) -> None:
        self.engine = engine
        self.user = self.get_users_schema()

    def get_users_schema(self):
        users = Table(
            'users', meta,
            Column('id', Integer, primary_key=True),
            Column('telegram_user_id', BigInteger),
            Column('name', String(100)),
            Column('surname', String(100)),
            Column('middle_name', String(100)),
            Column('gender', String(50)),
            Column('family_status', String(100)),
            Column('country', String(100)),
            Column('city', String(255)),
            Column('street', String(255)),
            # Column('house', String(20)),
            # Column('apartment', String(20), nullable=True),
            Column('photo_url', String(255)),
            extend_existing=True
        )
        return users

    def create_table(self):
        meta.create_all(self.engine, checkfirst=True)

    def record_user_in_db(self, data):
        ins = self.user.insert().values(
            **data
        )
        with self.engine.connect() as connect:
            connect.execute(ins)
            connect.commit()


users_manager = UsersManager(engine=engine)
