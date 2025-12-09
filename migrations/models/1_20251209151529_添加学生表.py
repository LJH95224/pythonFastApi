from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "students" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "name" VARCHAR(64) NOT NULL UNIQUE,
    "email" VARCHAR(255) UNIQUE,
    "age" INT NOT NULL DEFAULT 0,
    "created_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT "uid_students_name_993877" UNIQUE ("name", "email")
);
COMMENT ON COLUMN "students"."id" IS '学生ID, 主键';
COMMENT ON COLUMN "students"."name" IS '学生姓名, 唯一';
COMMENT ON COLUMN "students"."email" IS '学生邮箱, 唯一';
COMMENT ON TABLE "students" IS '学生模型';"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        DROP TABLE IF EXISTS "students";"""


MODELS_STATE = (
    "eJztmVtP4kAUx78K6RObuAbKTfcNlI1sBDaKuxvFNNPOABPbKbZTlRi/+86ZtpSWFisreF"
    "leTHsuw5nfXM4ffFQsGxPT3T/nHiaMK98KjwpDFhEPSddeQUHTaeQAA0e6KWNdP0gake5y"
    "Bxkw2AiZLhEmTFzDoVNObQbRQ6+m1+tDr1Erj4ZeHallYWkc6JCNbUOkUzZ+LtBj9NYjGr"
    "fHhE+II8KvrvzahZNYiJrK9bV4pAyTB+KCH16nN9qIEhPHpkoxJEm7xmdTaesw/l0GQlG6"
    "ZtimZ7EoeDrjE5vNo6lPaEwYcRAnMDx3PJg780wzwBTi8EuPQvwSF3IwGSHPBIKQvRpg53"
    "ivMPSqpKIPvcOaSpIQgxEMm8GyUFgkmPoYPv+rWq42qgeVevVAhMga55bGkz/xiIqfKNn0"
    "BsqT9COO/AgJOCIaLkSc6dEEOelQw/gEVlFyEmsIcdNcxfMhroi/1RIGwrWaOgLOpVJOwh"
    "Z60EzCxnwiXuvVFTh/Nc+OTppnxXr1C4xti9PjH6te4FGlC4hHhP0t/gLE84S1GAcEXxnx"
    "YQkR8azr5X9HrNZqORiLqEzI0henjMYp2zjzagiin78b8mzi0BAhjq7TkHFpCXBIfUs3QE"
    "TKcAhMTkN8Gdix8HBqkXRq8cwEPByk7ocPm0KZul3z0xRzwH1mzoKTsALdoNNtnw+a3Z8w"
    "E8t1b02JqDlog0eV1lnCWqwnNu18kMLvzuCkAK+Fy36vLQnaLh878hOjuMGlAjUhj9sas+"
    "81hBcObWgNwcQW1pviNRc2nrlb2DddWFk8KKDRzULHBoOOjJt75GBtyWOrdlbssstSraQF"
    "MXEj4oAtVBloygtXCrYlrSntK4WmJyLyqczsFd60csxuwanScbsaJ//GjzXXSj1Hb60kN3"
    "PUWsH1CRXjmjQ/vBp8Y34bkXrU1cR9Qu9SdmHLtk2CWMahXsxL0NRF4qb62pzwWkBX8Gv1"
    "+6exFtbqDBIcL7qt9lmxLPGKIMpJuijcyeedfP6vVNZOPn/ShX1P8rlJHGpMlBQBHXhWSm"
    "gUxbyqhv6kP7ZuuSNkC+Q78c0HSnqByFtIeR2Zt4ULYwu/6Ymj8QKIQfjHBFgulXIAFFGZ"
    "AKUvoVVsxoN/CcUh/jjv9zJESpSSAHnBxASvMDX4XsGkLr9+n1hXUIRZx3pWCK/Ybf5Jcj"
    "067beSzQgGaAnGb9penv4CyUHlWA=="
)
