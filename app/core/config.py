import os


class BaseConfig:
	PX_API_TOKEN=''
	PX_SUB_ID=''
	PX_SOURCE=''
	REDIS_URL = os.environ.get('REDIS_URL', 'redis://localhost:6379')


class DevConfig(BaseConfig):
	POSTGRES_HOST:str = os.environ.get("POSTGRES_HOST")
	POSTGRES_USER:str = os.environ.get("POSTGRES_USER")
	POSTGRES_PASSWORD:str =os.environ.get("POSTGRES_PASSWORD")
	POSTGRES_PORT:int = os.environ.get("POSTGRES_PORT")
	POSTGRES_DB:str = os.environ.get("POSTGRES_DB")
	DATABASE_URL:str = f"postgresql+asyncpg://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
	@property
	def SYNC_DB_URL(self):
		return self.DATABASE_URL.replace('postgresql+asyncpg://','postgresql://')


class ProductionConfig(BaseConfig):
	POSTGRES_HOST:str = os.environ.get("POSTGRES_HOST")
	POSTGRES_USER:str = os.environ.get("POSTGRES_USER")
	POSTGRES_PASSWORD:str =os.environ.get("POSTGRES_PASSWORD")
	POSTGRES_PORT:int = os.environ.get("POSTGRES_PORT")
	POSTGRES_DB:str = os.environ.get("POSTGRES_DB")
	DATABASE_URL = f"postgresql+asyncpg://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"

	@property
	def SYNC_DB_URL(self):
		return self.DATABASE_URL.replace('postgresql+asyncpg://','postgresql://')


if os.environ.get('CONFIG_TYPE') == 'PRODUCTION':
	config = ProductionConfig()
else:
	config = DevConfig()
