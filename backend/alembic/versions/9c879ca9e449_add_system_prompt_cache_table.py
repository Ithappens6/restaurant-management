"""add_system_prompt_cache_table

Revision ID: 9c879ca9e449
Revises: 1e85fe77f2e9
Create Date: 2025-10-28 18:30:51.275252

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9c879ca9e449'
down_revision: Union[str, None] = '1e85fe77f2e9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Create system_prompt_cache table
    op.create_table(
        'system_prompt_cache',
        sa.Column('restaurant_id', sa.String(length=100), nullable=False),
        sa.Column('prompt_text', sa.Text(), nullable=False),
        sa.Column('version', sa.Integer(), nullable=False),
        sa.Column('includes_menu', sa.Boolean(), nullable=True),
        sa.Column('includes_hours', sa.Boolean(), nullable=True),
        sa.Column('includes_about', sa.Boolean(), nullable=True),
        sa.Column('estimated_tokens', sa.Integer(), nullable=True),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.Column('updated_at', sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint('restaurant_id')
    )
    op.create_index('ix_system_prompt_cache_restaurant_id', 'system_prompt_cache', ['restaurant_id'], unique=False)


def downgrade() -> None:
    # Drop system_prompt_cache table
    op.drop_index('ix_system_prompt_cache_restaurant_id', table_name='system_prompt_cache')
    op.drop_table('system_prompt_cache')
