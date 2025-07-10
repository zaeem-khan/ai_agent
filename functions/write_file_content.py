import os
from google.genai import types

def write_file(working_directory, file_path, content):
    working_directory_abs = os.path.abspath(working_directory)
    file_path_abs = os.path.abspath(os.path.join(working_directory, file_path))

    if not file_path_abs.startswith(working_directory_abs):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

    if not os.path.exists(file_path_abs):
        try:
            os.makedirs(os.path.dirname(file_path_abs), exist_ok=True)
        except Exception as e:
            return f"Error: Could not create directory: {e}"
    
    if os.path.exists(file_path_abs) and os.path.isdir(file_path_abs):
        return f'Error: Cannot write to "{file_path}" as it is a directory'
    
    try:
        with open(file_path_abs, 'w') as file:
            file.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f"Error: {e}"

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes content to a specified file, creating directories as needed, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the file to write, relative to the working directory.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content to write to the file.",
            ),
        },
        required=["file_path", "content"],
    )
)
