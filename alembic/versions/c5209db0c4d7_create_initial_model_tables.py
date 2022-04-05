"""create initial model tables

Revision ID: c5209db0c4d7
Revises:
Create Date: 2022-03-26 16:45:03.940900

"""
from alembic import op

# revision identifiers, used by Alembic.
revision = 'c5209db0c4d7'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    """ """
    op.execute(
        """
        BEGIN;
        CREATE TYPE playerclassenum AS ENUM ('druid','mage','hunter','rogue','shaman','paladin','priest','warrior','warlock','deathknight');
        END;

        BEGIN;
        CREATE TABLE instance (
                id SERIAL NOT NULL,
                name VARCHAR(128) NOT NULL,
                created_at TIMESTAMP WITH TIME ZONE DEFAULT now() NOT NULL,
                updated_at TIMESTAMP WITH TIME ZONE DEFAULT now() NOT NULL,
                deleted_at TIMESTAMP WITH TIME ZONE,
                PRIMARY KEY (id)
        );
        END;

        BEGIN;
        CREATE TABLE raid (
                id SERIAL NOT NULL,
                name VARCHAR(128) NOT NULL,
                start_time TIMESTAMP WITH TIME ZONE,
                end_time TIMESTAMP WITH TIME ZONE,
                instance_id INTEGER NOT NULL,
                created_at TIMESTAMP WITH TIME ZONE DEFAULT now() NOT NULL,
                updated_at TIMESTAMP WITH TIME ZONE DEFAULT now() NOT NULL,
                deleted_at TIMESTAMP WITH TIME ZONE,
                PRIMARY KEY (id),
                FOREIGN KEY(instance_id) REFERENCES instance (id)
        );
        END;

        BEGIN;
        CREATE TABLE boss (
                id SERIAL NOT NULL,
                name VARCHAR(128) NOT NULL,
                instance_id INTEGER NOT NULL,
                created_at TIMESTAMP WITH TIME ZONE DEFAULT now() NOT NULL,
                updated_at TIMESTAMP WITH TIME ZONE DEFAULT now() NOT NULL,
                deleted_at TIMESTAMP WITH TIME ZONE,
                PRIMARY KEY (id),
                FOREIGN KEY(instance_id) REFERENCES instance (id)
        );
        END;

        BEGIN;
        CREATE TABLE item (
                id SERIAL NOT NULL,
                name VARCHAR(128) NOT NULL,
                boss_id INTEGER,
                instance_id INTEGER,
                wowhead_url VARCHAR,
                created_at TIMESTAMP WITH TIME ZONE DEFAULT now() NOT NULL,
                updated_at TIMESTAMP WITH TIME ZONE DEFAULT now() NOT NULL,
                deleted_at TIMESTAMP WITH TIME ZONE,
                PRIMARY KEY (id),
                FOREIGN KEY(boss_id) REFERENCES boss (id),
                FOREIGN KEY(instance_id) REFERENCES instance (id)
        );
        END;

        BEGIN;
        CREATE TABLE "user" (
                id SERIAL NOT NULL,
                discord_id BIGINT NOT NULL,
                discord_username VARCHAR NOT NULL,
                created_at TIMESTAMP WITH TIME ZONE DEFAULT now() NOT NULL,
                updated_at TIMESTAMP WITH TIME ZONE DEFAULT now() NOT NULL,
                deleted_at TIMESTAMP WITH TIME ZONE,
                PRIMARY KEY (id)
        );
        END;

        BEGIN;
        CREATE TABLE character (
                id SERIAL NOT NULL,
                name VARCHAR(128) NOT NULL,
                player_class playerclassenum NOT NULL,
                user_id INTEGER NOT NULL,
                created_at TIMESTAMP WITH TIME ZONE DEFAULT now() NOT NULL,
                updated_at TIMESTAMP WITH TIME ZONE DEFAULT now() NOT NULL,
                deleted_at TIMESTAMP WITH TIME ZONE,
                PRIMARY KEY (id),
                FOREIGN KEY(user_id) REFERENCES "user" (id)
        );
        END;

        BEGIN;
        CREATE TABLE auction (
                id SERIAL NOT NULL,
                raid_id INTEGER,
                winner_id INTEGER,
                price INTEGER,
                created_at TIMESTAMP WITH TIME ZONE DEFAULT now() NOT NULL,
                updated_at TIMESTAMP WITH TIME ZONE DEFAULT now() NOT NULL,
                deleted_at TIMESTAMP WITH TIME ZONE,
                PRIMARY KEY (id),
                FOREIGN KEY(raid_id) REFERENCES raid (id),
                FOREIGN KEY(winner_id) REFERENCES character (id)
        );
        END;

        BEGIN;
        CREATE TABLE loot (
                id SERIAL NOT NULL,
                raid_id INTEGER NOT NULL,
                item_id INTEGER NOT NULL,
                auction_id INTEGER,
                created_at TIMESTAMP WITH TIME ZONE DEFAULT now() NOT NULL,
                updated_at TIMESTAMP WITH TIME ZONE DEFAULT now() NOT NULL,
                deleted_at TIMESTAMP WITH TIME ZONE,
                PRIMARY KEY (id),
                FOREIGN KEY(raid_id) REFERENCES raid (id),
                FOREIGN KEY(item_id) REFERENCES item (id),
                FOREIGN KEY(auction_id) REFERENCES auction (id)
        );
        END;

        BEGIN;
        CREATE TABLE auction_loot (
                id SERIAL NOT NULL,
                auction_id INTEGER,
                loot_id INTEGER,
                created_at TIMESTAMP WITH TIME ZONE DEFAULT now() NOT NULL,
                updated_at TIMESTAMP WITH TIME ZONE DEFAULT now() NOT NULL,
                deleted_at TIMESTAMP WITH TIME ZONE,
                PRIMARY KEY (id),
                FOREIGN KEY(auction_id) REFERENCES auction (id),
                FOREIGN KEY(loot_id) REFERENCES loot (id)
        );
        END;
        """
    )


def downgrade():
    """ """
    op.execute(
        """
        BEGIN;
        DROP TABLE IF EXISTS "auction_loot";
        END;
        BEGIN;
        DROP TABLE IF EXISTS "loot";
        END;
        BEGIN;
        DROP TABLE IF EXISTS "auction";
        END;
        BEGIN;
        DROP TABLE IF EXISTS "character";
        END;
        BEGIN;
        DROP TABLE IF EXISTS "user";
        END;
        BEGIN;
        DROP TABLE IF EXISTS "item";
        END;
        BEGIN;
        DROP TABLE IF EXISTS "boss";
        END;
        BEGIN;
        DROP TABLE IF EXISTS "raid";
        END;
        BEGIN;
        DROP TABLE IF EXISTS "instance";
        END;
        BEGIN;
        DROP TYPE IF EXISTS playerclassenum;
        END;
        """
    )
