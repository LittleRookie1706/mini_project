from sqlmodel import SQLModel, Field

class TagGroups(SQLModel, table=True):
    id: int = Field(primary_key=True)
    name: str = Field(unique=True)
