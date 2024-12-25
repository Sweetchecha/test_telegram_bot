from alembic import op
import sqlalchemy as sa

# ID ревизии и её зависимость
revision = 'initial_migration'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    # Создание таблицы пользователей
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('telegram_id', sa.Integer, unique=True, nullable=False),
        sa.Column('first_name', sa.String(100)),
        sa.Column('username', sa.String(100))
    )

    # Создание таблицы логов сообщений
    op.create_table(
        'messages',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('user_id', sa.Integer, nullable=False),
        sa.Column('message_text', sa.Text, nullable=False),
        sa.Column('timestamp', sa.DateTime, nullable=False, server_default=sa.func.now())
    )

def downgrade():
    op.drop_table('messages')
    op.drop_table('users')
