from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase
from config_data.config import load_config, Config

config: Config = load_config()
DB_URL = f'postgresql+asyncpg://{config.db.db_user}:{config.db.db_password}@{config.db.db_host}/{config.db.database}'

engine: create_async_engine = create_async_engine(DB_URL, echo=False)
async_session: async_sessionmaker = async_sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)


class Base(DeclarativeBase):
    pass
