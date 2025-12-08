from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "users" (
    "id" VARCHAR(36) NOT NULL PRIMARY KEY,
    "username" VARCHAR(50) NOT NULL UNIQUE,
    "email" VARCHAR(255) NOT NULL UNIQUE,
    "is_active" BOOL NOT NULL DEFAULT True,
    "created_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
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
    "eJztlm1v2jAQx78K4hWTuorHtto7oExlKjDRsE2tqsjEJlg4dpo4bVHFd5/PJOQBgoCto0"
    "h7l/zvzr77nRPfW9ERmDD/fOQTr/il8FbkyCHqIaWfFYrIdWMVBInGTDsGykMraOxLD1lS"
    "iRPEfKIkTHzLo66kgiuVB4yBKCzlSLkdSwGnTwExpbCJnOpEHh6VTDkmr8SPXt2ZOaGE4V"
    "SeFMPeWjfl3NVae4q8r9oTthublmCBw2Nvdy6ngq/cVTag2oQTD0mCEwVAfmGhkbTMVQnS"
    "C8gqSRwLmExQwGSi4B0pWIIDQcqlr0t00KvJCLflVL3WLhbLYuJSl15QwY/msH3THJZqF5"
    "+gEqHasGxOP7RUtWmhl0ASLRfRYGOS0Ej9vAfPZMwpUm2Ud6DaKOdSBRNQjSkSB1G2D8JV"
    "wCnyqzYaOwBUXrkEtS2NkPqm+o3Q5w0nsSUEI4jnfNzJuAzNsQo8BGckxDzjf1sEdEX4IK"
    "Bb+LUGg1tI2vH9J6aFrpHhOOq1OsNSReNVTlRquds3Mkwtj0DVJpLrUK+VRVKHbKaajsxg"
    "xWHoefTwXoz/8NCqGvCAs3nYrS3MjW6vc2c0e99T4K+bRgcsVa3OM2op+9tdLVL42TVuCv"
    "BauB/0O5qg8KXt6R1jP+O+CDmhQAqTixcT4cSnG6kRmFRjAxcf2Nh05P/GHrWxOnkYciaz"
    "xOUMwhhZsxfkYXPNIqoiz3fd5FSdrII4snVXgC1kGc58TeJRa7ppGgwtW+dBFPt8mIGwy+"
    "Ue86A6XNnTHjbsqBevDbt8rlbql/Wr2kX9SrnoTFbK5ZbTH90I+ePfsxrjIaU9RpdEyN8Z"
    "Xv7BD+P9xxf4NPaAGLqfJsBKeZcBWnnlAtS2zKwiuCR8w3327W7QzxlS4pAMyBFXBT5gas"
    "mzAqO+fPyYWLdQhKpTd1YEr9Rr/spybd8OWtnLCBZoKcZHvV4WvwEuLz0r"
)
