import os
from google.genai import types

MAX_CHARS = 10000

def get_file_content(working_directory, file_path):
    working_directory_abs = os.path.abspath(working_directory)
    file_path_abs = os.path.abspath(os.path.join(working_directory, file_path))

    if not file_path_abs.startswith(working_directory_abs):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

    if not os.path.isfile(file_path_abs):
        return f'Error: File not found or is not a regular file: "{file_path}"'

    try:
        with open(file_path_abs, 'r') as file:
            file_content = file.read(MAX_CHARS)
            if len(file_content) >= MAX_CHARS:
                file_content += f'\n[...File "{file_path}" truncated at 10000 characters]'
            return file_content
    except Exception as e:
        return f"Error: {e}"

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Retrieves the content of a specified file, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the file to read, relative to the working directory.",
            ),
        },
        required=["file_path"],
    )
)