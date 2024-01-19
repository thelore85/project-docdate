"""empty message

Revision ID: fbbdb6debf17
Revises: 
Create Date: 2024-01-18 10:25:09.665337

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fbbdb6debf17'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('patients',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('lastname', sa.String(length=50), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('phone', sa.String(length=25), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('phone')
    )
    op.create_table('pros',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('password', sa.String(length=80), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('lastname', sa.String(length=50), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('phone', sa.String(length=25), nullable=False),
    sa.Column('bookingpage_url', sa.String(), nullable=False),
    sa.Column('suscription', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('bookingpage_url'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('phone')
    )
    op.create_table('services',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('specialization', sa.String(), nullable=False),
    sa.Column('service_name', sa.String(), nullable=False),
    sa.Column('service_type', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('hours',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('working_day', sa.Integer(), nullable=False),
    sa.Column('starting_hour', sa.String(), nullable=False),
    sa.Column('ending_hour', sa.String(), nullable=False),
    sa.Column('pro_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['pro_id'], ['pros.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('inactivity',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('starting_date', sa.String(), nullable=False),
    sa.Column('ending_date', sa.String(), nullable=True),
    sa.Column('starting_hour', sa.String(), nullable=True),
    sa.Column('ending_hour', sa.String(), nullable=True),
    sa.Column('pro_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['pro_id'], ['pros.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('locations',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.Column('address', sa.String(), nullable=False),
    sa.Column('city', sa.String(), nullable=False),
    sa.Column('country', sa.String(), nullable=False),
    sa.Column('duration', sa.Integer(), nullable=False),
    sa.Column('pro_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['pro_id'], ['pros.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('pro_id')
    )
    op.create_table('pro_services',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('price', sa.Integer(), nullable=True),
    sa.Column('pro_id', sa.Integer(), nullable=False),
    sa.Column('service_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['pro_id'], ['pros.id'], ),
    sa.ForeignKeyConstraint(['service_id'], ['services.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('bookings',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date', sa.String(), nullable=False),
    sa.Column('starting_time', sa.String(), nullable=False),
    sa.Column('status', sa.String(), nullable=False),
    sa.Column('pro_notes', sa.String(), nullable=True),
    sa.Column('patient_notes', sa.String(), nullable=True),
    sa.Column('pro_service_id', sa.Integer(), nullable=False),
    sa.Column('patient_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['patient_id'], ['patients.id'], ),
    sa.ForeignKeyConstraint(['pro_service_id'], ['pro_services.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('bookings')
    op.drop_table('pro_services')
    op.drop_table('locations')
    op.drop_table('inactivity')
    op.drop_table('hours')
    op.drop_table('services')
    op.drop_table('pros')
    op.drop_table('patients')
    # ### end Alembic commands ###
