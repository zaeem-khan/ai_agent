import os
import subprocess
from google.genai import types

def run_python_file(working_directory, file_path):
    working_directory_abs = os.path.abspath(working_directory)
    file_path_abs = os.path.abspath(os.path.join(working_directory, file_path))

    if not file_path_abs.startswith(working_directory_abs):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

    if not os.path.exists(file_path_abs):
        return f'Error: File "{file_path}" not found.'
    
    path_root, path_ext = os.path.splitext(file_path_abs)
    if path_ext != '.py':
        return f'Error: "{file_path}" is not a Python file.'
    
    try:
        result = subprocess.run(['python', file_path_abs], capture_output=True, cwd=working_directory_abs, timeout=30)

        if result.returncode != 0:
            return f'Process exited with code {result.returncode}'
        if result.stdout == '':
            return 'No output produced'
        output = f'STDOUT: {result.stdout}'
        if result.stderr:
            output += f'\nSTDERR: {result.stderr}'
        return output
    except Exception as e:
        return f'Error: {e}'

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Executes a Python file in the specified working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the Python file to execute, relative to the working directory.",
            ),
        },
        required=["file_path"],
    )
)