# API Signature

`from coder_platform.file_processing.src.file_manager import store_files_into_dir, load_files_from_dir`

`store_files_into_dir(agent_response: str, output_dir_path: str) -> str` - Stores the agent response content into a file in the specified directory. Returns the stored file path.

`load_files_from_dir(output_dir_path: str) -> List[Dict[str, str]]` - Loads all files from the specified directory. Returns a list of dictionaries containing file information (filename and content).
