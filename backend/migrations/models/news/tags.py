from sqlmodel import SQLModel, Field

class Tags(SQLModel, table=True):
    id: int = Field(primary_key=True)
    name: str = Field(unique=True)
    tag_group_id: int = Field(default=None, nullable=True , foreign_key="taggroups.id")