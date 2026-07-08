import json
import os

def load_knowledge_base():
    # Get the path to datasets/knowledge_base.json
    current_dir = os.path.dirname(__file__)
    project_root = os.path.abspath(os.path.join(current_dir, "..", ".."))
    file_path = os.path.join(project_root, "datasets", "knowledge_base.json")

    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    print(f"Loaded {len(data)} records from the Knowledge Base.\n")

    return data


if __name__ == "__main__":
    kb = load_knowledge_base()

    print("Sample Record:\n")
    print(kb[0])