import os


class BaseConfig:
	PX_API_TOKEN=''
	PX_SUB_ID=''
	PX_SOURCE=''
	REDIS_URL = os.environ.get('REDIS_URL', 'redis://localhost:6379')


class ProductionConfig(BaseConfig):
	CONFIG_TYPE='PRODUCTION'
	POSTGRES_HOST:str = os.environ.get("POSTGRES_HOST",'affiatetracking-db.returnoftm.com')
	POSTGRES_USER:str = os.environ.get("POSTGRES_USER",'postgres')
	POSTGRES_PASSWORD:str =os.environ.get("POSTGRES_PASSWORD",'Deskjet1$')
	POSTGRES_PORT:int = os.environ.get("POSTGRES_PORT",'5555')
	POSTGRES_DB:str = os.environ.get("POSTGRES_DB",'postgres')
	DATABASE_URL = f"postgresql+asyncpg://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"

	@property
	def SYNC_DB_URL(self):
		return self.DATABASE_URL.replace('postgresql+asyncpg://','postgresql://')

config = ProductionConfig()
