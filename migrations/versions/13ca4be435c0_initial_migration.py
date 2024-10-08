"""Initial migration.

Revision ID: 13ca4be435c0
Revises: 
Create Date: 2024-10-07 02:02:59.050706

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '13ca4be435c0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('candidat',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nom', sa.String(length=100), nullable=False),
    sa.Column('prenom', sa.String(length=100), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('cv', sa.String(length=200), nullable=True),
    sa.Column('lettre_motivation', sa.String(length=200), nullable=True),
    sa.Column('experience', sa.Integer(), nullable=True),
    sa.Column('categorie', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('poste',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('titre', sa.String(length=100), nullable=False),
    sa.Column('missions', sa.String(length=200), nullable=False),
    sa.Column('competences', sa.String(length=200), nullable=False),
    sa.Column('diplome', sa.String(length=100), nullable=True),
    sa.Column('experience', sa.Integer(), nullable=True),
    sa.Column('salaire', sa.Float(), nullable=True),
    sa.Column('localisation', sa.String(length=100), nullable=True),
    sa.Column('type_contrat', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('entretien',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date_entretien', sa.Date(), nullable=True),
    sa.Column('note_entretien', sa.String(length=200), nullable=True),
    sa.Column('candidat_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['candidat_id'], ['candidat.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('entretien')
    op.drop_table('poste')
    op.drop_table('candidat')
    # ### end Alembic commands ###
