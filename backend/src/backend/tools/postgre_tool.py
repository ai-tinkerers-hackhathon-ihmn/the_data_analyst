from smolagents import Tool
import os
import psycopg2
from psycopg2.extras import RealDictCursor
from typing import Dict, Any, List, Union
import dotenv

dotenv.load_dotenv()

# Tools def
class PostgresQueryTool(Tool):
    # description
    name = "postgres_query"
    description = "Executes SQL queries on a PostgreSQL database."
    
    inputs = {
        "query": {
            "type": "string",
            "description": "The SQL query to execute. For example 'SELECT * FROM users LIMIT 5'"
        },
        "params": {
            "type": "object", 
            "description": "Optional query parameters for parameterized queries",
            "required": False,
            "nullable": True
        }
    }
    output_type = "object"

    def __init__(self):
        """Initialize the PostgreSQL query tool with connection details from environment variables."""
        super().__init__()
        
        # Get database connection details from environment variables
        self.db_config = {
            "dbname": os.environ.get("POSTGRES_DB", "postgres"),
            "user": os.environ.get("POSTGRES_USER", "postgres"),
            "password": os.environ.get("POSTGRES_PASSWORD", "postgres"),
            "host": os.environ.get("POSTGRES_HOST", "localhost"),
            "port": os.environ.get("POSTGRES_PORT", "5432")
        }
        
        # Initialize database connection
        self.conn = self._get_connection()

    def _get_connection(self):
        """Create and return a database connection."""
        try:
            return psycopg2.connect(
                **self.db_config,
                cursor_factory=RealDictCursor  # Returns results as dictionaries
            )
        except psycopg2.Error as e:
            raise ConnectionError(f"Failed to connect to database: {str(e)}")

    def forward(self, query: str, params: Dict[str, Any] = None) -> Dict[str, Any]:
        """
        Executes the SQL query on the PostgreSQL database.
        
        Args:
            query (str): The SQL query to execute
            params (Dict[str, Any], optional): Parameters for parameterized queries
            
        Returns:
            Dict containing:
                - success (bool): Whether the query executed successfully
                - data (List[Dict]): Query results (for SELECT queries)
                - affected_rows (int): Number of affected rows (for INSERT/UPDATE/DELETE)
                - error (str): Error message if query failed
        """
        try:
            # Reuse existing connection or create new if closed
            if self.conn.closed:
                self.conn = self._get_connection()
                
            cursor = self.conn.cursor()
            
            # Execute query with optional parameters
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            
            # Handle different query types
            if query.strip().upper().startswith("SELECT"):
                # For SELECT queries, return the results
                results = cursor.fetchall()
                return {
                    "success": True,
                    "data": [dict(row) for row in results],
                    "affected_rows": len(results),
                    "error": None
                }
            else:
                # For INSERT/UPDATE/DELETE queries, return affected rows
                self.conn.commit()
                return {
                    "success": True,
                    "data": None,
                    "affected_rows": cursor.rowcount,
                    "error": None
                }
                
        except psycopg2.Error as e:
            # Roll back transaction on error
            self.conn.rollback()
            return {
                "success": False,
                "data": None,
                "affected_rows": 0,
                "error": str(e)
            }
            
        finally:
            cursor.close()

    def get_table_schema(self, table_name: str) -> Dict[str, Any]:
        """
        Get the schema information for a specific table.
        
        Args:
            table_name (str): Name of the table
            
        Returns:
            Dict containing table schema information
        """
        query = """
            SELECT column_name, data_type, is_nullable, column_default
            FROM information_schema.columns
            WHERE table_name = %s
            ORDER BY ordinal_position;
        """
        
        result = self.forward(query, {"table_name": table_name})
        if result["success"]:
            return {
                "success": True,
                "table_name": table_name,
                "columns": result["data"]
            }
        return result