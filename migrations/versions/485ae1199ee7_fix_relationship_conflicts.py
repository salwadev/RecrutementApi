"""Fix relationship conflicts

Revision ID: 485ae1199ee7
Revises: d340e9dad93f
Create Date: 2024-10-07 04:29:24.718141

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '485ae1199ee7'
down_revision = 'd340e9dad93f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('critere',
    sa.Column('idCritere', sa.Integer(), nullable=False),
    sa.Column('nomCritere', sa.String(length=100), nullable=False),
    sa.Column('poidsCritere', sa.Float(), nullable=False),
    sa.PrimaryKeyConstraint('idCritere')
    )
    op.create_table('modele_ml',
    sa.Column('idModele', sa.Integer(), nullable=False),
    sa.Column('nomModele', sa.String(length=100), nullable=False),
    sa.Column('typeModele', sa.String(length=50), nullable=False),
    sa.Column('parametres', sa.PickleType(), nullable=False),
    sa.Column('precision', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('idModele')
    )
    op.create_table('competence',
    sa.Column('idCompetence', sa.Integer(), nullable=False),
    sa.Column('nomCompetence', sa.String(length=100), nullable=False),
    sa.Column('niveau', sa.Integer(), nullable=False),
    sa.Column('candidat_id', sa.Integer(), nullable=True),
    sa.Column('poste_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['candidat_id'], ['candidat.idCandidat'], ),
    sa.ForeignKeyConstraint(['poste_id'], ['poste.idPoste'], ),
    sa.PrimaryKeyConstraint('idCompetence')
    )
    op.add_column('candidat', sa.Column('idCandidat', sa.Integer(), nullable=False))
    op.add_column('candidat', sa.Column('lettreMotivation', sa.String(length=200), nullable=False))
    op.add_column('candidat', sa.Column('diplome', sa.String(length=100), nullable=False))
    op.alter_column('candidat', 'email',
               existing_type=sa.VARCHAR(length=120),
               type_=sa.String(length=100),
               existing_nullable=False)
    op.alter_column('candidat', 'cv',
               existing_type=sa.VARCHAR(length=200),
               nullable=False)
    op.alter_column('candidat', 'experience',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.drop_column('candidat', 'id')
    op.drop_column('candidat', 'lettre_motivation')
    op.add_column('entretien', sa.Column('idEntretien', sa.Integer(), nullable=False))
    op.add_column('entretien', sa.Column('dateEntretien', sa.Date(), nullable=False))
    op.add_column('entretien', sa.Column('noteEntretien', sa.PickleType(), nullable=True))
    op.add_column('entretien', sa.Column('postEntretienNotes', sa.String(length=500), nullable=True))
    op.alter_column('entretien', 'candidat_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.drop_constraint(None, 'entretien', type_='foreignkey')
    op.create_foreign_key(None, 'entretien', 'candidat', ['candidat_id'], ['idCandidat'])
    op.drop_column('entretien', 'id')
    op.drop_column('entretien', 'date_entretien')
    op.drop_column('entretien', 'note_entretien')
    op.add_column('poste', sa.Column('idPoste', sa.Integer(), nullable=False))
    op.add_column('poste', sa.Column('diplomes', sa.String(length=100), nullable=False))
    op.add_column('poste', sa.Column('typeContrat', sa.String(length=50), nullable=False))
    op.alter_column('poste', 'missions',
               existing_type=sa.TEXT(),
               type_=sa.String(length=500),
               existing_nullable=False)
    op.alter_column('poste', 'experience',
               existing_type=sa.VARCHAR(length=100),
               type_=sa.Integer(),
               nullable=False)
    op.alter_column('poste', 'salaire',
               existing_type=sa.FLOAT(),
               nullable=False)
    op.alter_column('poste', 'localisation',
               existing_type=sa.VARCHAR(length=100),
               nullable=False)
    op.drop_column('poste', 'type_contrat')
    op.drop_column('poste', 'id')
    op.drop_column('poste', 'diplome')
    op.drop_column('poste', 'competences')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('poste', sa.Column('competences', sa.TEXT(), nullable=True))
    op.add_column('poste', sa.Column('diplome', sa.VARCHAR(length=100), nullable=True))
    op.add_column('poste', sa.Column('id', sa.INTEGER(), nullable=False))
    op.add_column('poste', sa.Column('type_contrat', sa.VARCHAR(length=50), nullable=True))
    op.alter_column('poste', 'localisation',
               existing_type=sa.VARCHAR(length=100),
               nullable=True)
    op.alter_column('poste', 'salaire',
               existing_type=sa.FLOAT(),
               nullable=True)
    op.alter_column('poste', 'experience',
               existing_type=sa.Integer(),
               type_=sa.VARCHAR(length=100),
               nullable=True)
    op.alter_column('poste', 'missions',
               existing_type=sa.String(length=500),
               type_=sa.TEXT(),
               existing_nullable=False)
    op.drop_column('poste', 'typeContrat')
    op.drop_column('poste', 'diplomes')
    op.drop_column('poste', 'idPoste')
    op.add_column('entretien', sa.Column('note_entretien', sa.VARCHAR(length=200), nullable=True))
    op.add_column('entretien', sa.Column('date_entretien', sa.DATE(), nullable=True))
    op.add_column('entretien', sa.Column('id', sa.INTEGER(), nullable=False))
    op.drop_constraint(None, 'entretien', type_='foreignkey')
    op.create_foreign_key(None, 'entretien', 'candidat', ['candidat_id'], ['id'])
    op.alter_column('entretien', 'candidat_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.drop_column('entretien', 'postEntretienNotes')
    op.drop_column('entretien', 'noteEntretien')
    op.drop_column('entretien', 'dateEntretien')
    op.drop_column('entretien', 'idEntretien')
    op.add_column('candidat', sa.Column('lettre_motivation', sa.VARCHAR(length=200), nullable=True))
    op.add_column('candidat', sa.Column('id', sa.INTEGER(), nullable=False))
    op.alter_column('candidat', 'experience',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('candidat', 'cv',
               existing_type=sa.VARCHAR(length=200),
               nullable=True)
    op.alter_column('candidat', 'email',
               existing_type=sa.String(length=100),
               type_=sa.VARCHAR(length=120),
               existing_nullable=False)
    op.drop_column('candidat', 'diplome')
    op.drop_column('candidat', 'lettreMotivation')
    op.drop_column('candidat', 'idCandidat')
    op.drop_table('competence')
    op.drop_table('modele_ml')
    op.drop_table('critere')
    # ### end Alembic commands ###
