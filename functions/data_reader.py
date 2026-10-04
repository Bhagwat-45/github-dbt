import yaml

def yaml_reader(file_path: str) -> list | None:
    with open(file_path, 'r') as f:
        data = yaml.full_load(f)

    if data: return data
    else: return None