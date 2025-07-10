import os
from google.genai import types

def get_files_info(working_directory, directory=None):
   
    working_dir_abs = os.path.abspath(working_directory)
    target_dir_abs = os.path.abspath(os.path.join(working_directory, directory or "."))

    if not target_dir_abs.startswith(working_dir_abs):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    if not os.path.isdir(target_dir_abs):
        return f'Error: "{directory}" is not a directory'
    
    try:
        list_directory = os.listdir(target_dir_abs)
        string_list = []
        for file in list_directory:
            joined_path = os.path.join(target_dir_abs, file)
            line = f"- {file}: file_size={os.path.getsize(joined_path)}, is_dir={os.path.isdir(joined_path)}"
            string_list.append(line)
    except Exception as e:
        return f"Error: {e}"
    
    return "\n".join(string_list)


schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    )
)