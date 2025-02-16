import os
import requests

from smolagents import Tool



class StreamlitRunnerTool(Tool):
    name = "streamlit_runner"
    description = "Runs a Streamlit application from a Python file"
    inputs = {
        "filepath": {
            "type": "string",
            "description": "Path to the Streamlit Python file to run"
        },
        "port": {
            "type": "integer",
            "description": "Port to run the Streamlit app on",
            "default": 8501,
            "nullable": True
        }
    }
    output_type = "string"

    def forward(self, filepath: str, port: int = 8501) -> str:
        import subprocess
        import os
        
        # Verify file exists
        if not os.path.exists(filepath):
            return f"Error: File {filepath} does not exist"
        
        # Verify file is a Python file
        if not filepath.endswith('.py'):
            return f"Error: {filepath} is not a Python file"
        
        try:
            # Construct the command
            command = f"streamlit run {filepath} --server.port {port}"
            
            # Run the streamlit command in a subprocess
            process = subprocess.Popen(
                command,
                shell=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            
            # Wait a bit for the server to start
            import time
            time.sleep(2)
            
            # Check if process is running
            if process.poll() is None:
                return f"Streamlit app is running at http://localhost:{port}"
            else:
                _, error = process.communicate()
                return f"Error starting Streamlit app: {error}"
                
        except Exception as e:
            return f"Failed to run Streamlit app: {str(e)}"

# Create the tool
streamlit_runner = StreamlitRunnerTool()