class PythonFileCreatorTool(Tool):
    name = "python_file_creator"
    description = "Creates a Python file locally with the specified content"
    inputs = {
        "filename": {
            "type": "string",
            "description": "Name of the Python file to create (with .py extension)"
        },
        "content": {
            "type": "string",
            "description": "Content to write in the Python file"
        },
        "directory": {
            "type": "string",
            "description": "Directory where to create the file (default: current directory)",
            "default": ".",
            "nullable": True
        }
    }
    output_type = "string"

    def forward(self, filename: str, content: str, directory: str = ".") -> str:
        import os
        
        # Ensure filename has .py extension
        if not filename.endswith('.py'):
            filename += '.py'
        
        # Create full path
        filepath = os.path.join(directory, filename)
        
        # Create directory if it doesn't exist
        os.makedirs(directory, exist_ok=True)
        
        # Write content to file
        with open(filepath, 'w') as f:
            f.write(content)
        
        return f"Successfully created Python file at: {filepath}"

# Create and test the tool
file_creator = PythonFileCreatorTool()