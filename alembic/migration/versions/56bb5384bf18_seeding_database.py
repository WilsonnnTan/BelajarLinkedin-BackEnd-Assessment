"""seeding database

Revision ID: 56bb5384bf18
Revises: 4775e06e1290
Create Date: 2025-08-20 14:48:00.826308

"""
from typing import Sequence, Union

from alembic import op
from sqlalchemy import MetaData, Table, Column, String, text
from sqlalchemy.dialects.postgresql import UUID
from passlib.context import CryptContext


# revision identifiers, used by Alembic.
revision: str = '56bb5384bf18'
down_revision: Union[str, None] = '4775e06e1290'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# add admin account
def upgrade() -> None:
    bind = op.get_bind()
    meta = MetaData()
    users_table = Table('users', meta, autoload_with=bind)
    
    admin_data = {
        "username": "admin",
        "email": "admin@example.com",
        # NOTE: better to hash with bcrypt or passlib, this is just SHA256 demo
        "password": pwd_context.hash("admin"),
        "level": "admin"
    }
    
    bind.execute(users_table.insert().values(admin_data))
    


def downgrade() -> None:
    bind = op.get_bind()
    meta = MetaData()

    users_table = Table('users', meta, autoload_with=bind)

    bind.execute(users_table.delete().where(users_table.c.username == "admin"))
