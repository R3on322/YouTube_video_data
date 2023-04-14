from database.db_settings import Base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship


class User(Base):
    __tablename__ = 'user_info'

    user_id: Mapped[int] = mapped_column(primary_key=True)
    user_name: Mapped[str]
    video_info: Mapped[list["UserVideoInfo"]] = relationship(
        back_populates='user', cascade='all, delete-orphan'
    )

    def __repr__(self):
        return f'User(id={self.user_id}, name={self.user_name})'


class UserVideoInfo(Base):
    __tablename__ = 'user_video_info'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('user_info.user_id'))
    video_name: Mapped[str]
    video_url: Mapped[str]

    user: Mapped["User"] = relationship(back_populates='video_info')

    def __repr__(self):
        return f'User(user_id={self.user_id}), Video_name({self.video_name}), Video_URL({self.video_url})'
