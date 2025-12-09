from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "users" (
    "id" VARCHAR(36) NOT NULL PRIMARY KEY,
    "name" VARCHAR(64) NOT NULL UNIQUE,
    "email" VARCHAR(255) NOT NULL UNIQUE,
    "is_active" BOOL NOT NULL DEFAULT True,
    "age" INT NOT NULL DEFAULT 0,
    "created_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT "uid_users_name_a574b9" UNIQUE ("name", "email")
);
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSONB NOT NULL
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """


MODELS_STATE = (
    "eJztl21P2zAQx79KlVedxCYopaC9a6ETnWg7QdgmEIrc2E0tHDskDlAhvvvunKRp0qQqT2"
    "NIe5f87y65+9nxXR4sX1Emoi/nEQutr40HSxKfwUVB32pYJAhyFQVNJsI4xuBhFDKJdEhc"
    "DeKUiIiBRFnkhjzQXElQZSwEisoFRy69XIolv4mZo5XH9MwkcnmZZAJG5hMurKsruOSSsn"
    "sWoR1vg2tnypmghcQ5xSCjO3oeGO1wRsJvxhPfP3FcJWJf5t7BXM+UXLhDeqh6TLKQaEaX"
    "KsKE08ozKUkeBB3GbJEkzQXKpiQWeonAhlhcJREplzoyJfrk3hFMenoGt7udx6SYvNTECy"
    "v42T09PO6eNnc7n7ASBeuSrNYotbSM6dE8gmiSPMSAzUlmC7Apy8z/I9LstDeg2WnX0kQT"
    "0szpJdv2CfgWAR+RX2tvbwOA4FVL0NiKCHnkwHnCbyt2YU8pwYis+aiX40o0JxD4HJyZkP"
    "PMD7kM6ILws4Cu4dcbj08waT+KboQRBnaJ4/mw1z9t7hi84MS1kQcju8SUeBU0B1JXk0y9"
    "Swwh47dCuP2CDenhSz63dtr77YPdTvsAXEwiC2V/DeJVUm7IsDiH6FVgR2DR3GfV1IqRJX"
    "g0Df2SXbwVyhd+3lADHUsxT/f1GnT2YNg/s7vDH4UtetS1+2hpGXVeUpvlxrR4SOPXwD5u"
    "4G3jYjzqG4Iq0l5o3pj72RcW5kRirRyp7hxClw65TM3AFBY2DugzF7YY+X9h33VhTfI4Bk"
    "6vl8YXFCbEvb4jIXVWLKql6nxXTX7LLytEwolIU7aYZTomd1nI3ZlVMUCnlrUjNMl9XnWG"
    "fsnIXNsSKifmio6QLti7jiiv0hHqB+Rb+PPBlJ4w5C2FvM6Y9xcOjLcf9PDTeALE1P1jAt"
    "zZ3t4AIHjVAjS20qyipGayop99PxuPaoaUPKQE8lxCgZeUu3qrIXikr/5NrGsoYtWFnpXB"
    "aw67v8tcD0/GvXIzwgf0gPG7tpfHPx0Amwo="
)
