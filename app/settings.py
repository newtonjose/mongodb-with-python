from pydantic_settings import BaseSettings


class Settings(BaseSettings):    
    mongodb_uri: str  = 'mongodb://user:pass@localhost/mydatabase'  # TODO: type MongoDsn raise "mongodb+srv:// URIs must not include a port number"
    
    class Config:
        env_file = '.env'

settings = Settings()
