from smolagents import Tool
import os
from typing import Dict, Any, List, Union
import dotenv
from pymongo import MongoClient
from pymongo.errors import PyMongoError

dotenv.load_dotenv()

class MongoDBQueryTool(Tool):
    name = "mongodb_query"
    description = "Executes queries on a MongoDB database."
    
    inputs = {
        "collection": {
            "type": "string",
            "description": "The name of the MongoDB collection to query"
        },
        "operation": {
            "type": "string",
            "description": "The type of operation to perform (find, insert_one, insert_many, update_one, update_many, delete_one, delete_many)"
        },
        "query": {
            "type": "object",
            "description": "The query parameters as a dictionary. For find operations, this is the filter. For updates, this is the filter criteria."
        },
        "data": {
            "type": "object",
            "description": "The data to insert or update (required for insert and update operations)",
            "required": False,
            "nullable": True
        }
    }
    output_type = "object"

    def __init__(self, mongo_uri: str = None, db_name: str = None):
        """Initialize the MongoDB query tool with connection details.
        
        Args:
            mongo_uri (str, optional): MongoDB connection URI. Defaults to environment variable MONGODB_URI or localhost.
            db_name (str, optional): Database name. Defaults to environment variable MONGODB_DB or 'default_db'.
        """
        super().__init__()
        
        # Get database connection details from parameters or environment variables
        self.mongo_uri = mongo_uri or os.environ.get("MONGODB_URI", "mongodb://localhost:27017")
        self.db_name = db_name or os.environ.get("MONGODB_DB", "default_db")
        
        # Initialize as None - will be lazily initialized on first use
        self.client = None
        self.db = None

    def _get_connection(self) -> MongoClient:
        """Create and return a MongoDB client connection."""
        try:
            return MongoClient(self.mongo_uri)
        except PyMongoError as e:
            raise ConnectionError(f"Failed to connect to MongoDB: {str(e)}")

    def forward(self, collection: str, operation: str, query: Dict[str, Any], data: Dict[str, Any] = None) -> Dict[str, Any]:
        """
        Executes the MongoDB operation on the specified collection.
        
        Args:
            collection (str): Name of the collection
            operation (str): Type of operation to perform
            query (Dict[str, Any]): Query parameters
            data (Dict[str, Any], optional): Data for insert/update operations
            
        Returns:
            Dict containing:
                - success (bool): Whether the operation executed successfully
                - data (List[Dict]): Query results (for find operations)
                - affected_count (int): Number of affected documents
                - error (str): Error message if operation failed
        """
        try:
            # Initialize connection if not already done
            if self.client is None:
                self.client = self._get_connection()
                self.db = self.client[self.db_name]
            
            collection = self.db[collection]
            
            if operation == "find":
                cursor = collection.find(query)
                results = list(cursor)
                return {
                    "success": True,
                    "data": results,
                    "affected_count": len(results),
                    "error": None
                }
                
            elif operation == "insert_one":
                result = collection.insert_one(data)
                return {
                    "success": True,
                    "data": {"inserted_id": str(result.inserted_id)},
                    "affected_count": 1,
                    "error": None
                }
                
            elif operation == "insert_many":
                result = collection.insert_many(data)
                return {
                    "success": True,
                    "data": {"inserted_ids": [str(id) for id in result.inserted_ids]},
                    "affected_count": len(result.inserted_ids),
                    "error": None
                }
                
            elif operation == "update_one":
                result = collection.update_one(query, {"$set": data})
                return {
                    "success": True,
                    "data": None,
                    "affected_count": result.modified_count,
                    "error": None
                }
                
            elif operation == "update_many":
                result = collection.update_many(query, {"$set": data})
                return {
                    "success": True,
                    "data": None,
                    "affected_count": result.modified_count,
                    "error": None
                }
                
            elif operation == "delete_one":
                result = collection.delete_one(query)
                return {
                    "success": True,
                    "data": None,
                    "affected_count": result.deleted_count,
                    "error": None
                }
                
            elif operation == "delete_many":
                result = collection.delete_many(query)
                return {
                    "success": True,
                    "data": None,
                    "affected_count": result.deleted_count,
                    "error": None
                }
                
            else:
                return {
                    "success": False,
                    "data": None,
                    "affected_count": 0,
                    "error": f"Unsupported operation: {operation}"
                }
                
        except PyMongoError as e:
            return {
                "success": False,
                "data": None,
                "affected_count": 0,
                "error": str(e)
            }

    def get_collection_info(self, collection_name: str) -> Dict[str, Any]:
        """
        Get information about a specific collection.
        
        Args:
            collection_name (str): Name of the collection
            
        Returns:
            Dict containing collection information including indexes and stats
        """
        try:
            # Initialize connection if not already done
            if self.client is None:
                self.client = self._get_connection()
                self.db = self.client[self.db_name]

            collection = self.db[collection_name]
            
            # Get collection stats
            stats = self.db.command("collstats", collection_name)
            
            # Get indexes
            indexes = list(collection.list_indexes())
            
            return {
                "success": True,
                "collection_name": collection_name,
                "stats": stats,
                "indexes": indexes,
                "error": None
            }
        except PyMongoError as e:
            return {
                "success": False,
                "stats": None,
                "indexes": None,
                "error": str(e)
            }

    def __del__(self):
        """Cleanup method to close MongoDB connection when object is destroyed."""
        if self.client is not None:
            self.client.close()