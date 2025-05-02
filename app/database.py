from pymongo import errors, MongoClient

from .settings import settings
from .utils import get_logger

logger = get_logger(__name__)

try:
    client = MongoClient(settings.mongodb_uri)

    for db_name in client.list_database_names():
        print(db_name)

    client.close()
except errors.InvalidURI as e:
    logger.warning(e)
except errors.ConfigurationError as e:
    logger.warning(e)
except errors.OperationFailure as e:
    logger.error(e)
except errors.ServerSelectionTimeoutError:
    logger.error("Cluster not reachable. Please check your network connection and IP whitelisting")
