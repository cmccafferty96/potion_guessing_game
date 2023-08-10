"""empty message

Revision ID: 190f681c66c2
Revises: 
Create Date: 2023-08-10 17:20:37.236925

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '190f681c66c2'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('houses',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.Column('overall_score', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('ingredients',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.Column('description', sa.String(length=50), nullable=True),
    sa.Column('thumbnail', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('potions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.Column('correct_ingredients', sa.String(), nullable=True),
    sa.Column('thumbnail', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('potion_ingredients',
    sa.Column('potion_id', sa.Integer(), nullable=False),
    sa.Column('ingredient_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['ingredient_id'], ['ingredients.id'], name=op.f('fk_potion_ingredients_ingredient_id_ingredients')),
    sa.ForeignKeyConstraint(['potion_id'], ['potions.id'], name=op.f('fk_potion_ingredients_potion_id_potions')),
    sa.PrimaryKeyConstraint('potion_id', 'ingredient_id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=50), nullable=True),
    sa.Column('score', sa.Integer(), nullable=True),
    sa.Column('house_id', sa.Integer(), nullable=True),
    sa.Column('password', sa.String(), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['house_id'], ['houses.id'], name=op.f('fk_users_house_id_houses')),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    op.drop_table('potion_ingredients')
    op.drop_table('potions')
    op.drop_table('ingredients')
    op.drop_table('houses')
    # ### end Alembic commands ###