from sqlmodel import SQLModel, Field


class Tags(SQLModel, table=True):
    id: int = Field(primary_key=True)
    name: str = Field()