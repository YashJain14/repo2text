from git import Repo
import os
import shutil
import sys

def should_skip(file_path, extension=None):
    skip_patterns = ['.git', "__pycache__"]
    for pattern in skip_patterns:
        if pattern in file_path:
            return True
    # Only skip non-matching files if an extension is specified
    if extension and not file_path.endswith('.' + extension):
        return True
    return False

def repo_to_text(repo_url, extension=None):
    repo_name = repo_url.split('/')[-1].split('.git')[0]
    output_file = f"{repo_name}.txt" if not extension else f"{repo_name}_{extension}.txt"
    repo_path = '/tmp/repo'
    if os.path.exists(repo_path):
        shutil.rmtree(repo_path)
    print(f"Cloning repository from {repo_url}...")
    Repo.clone_from(repo_url, repo_path)
    with open(output_file, 'w', encoding='utf-8') as file_output:
        for root, dirs, files in os.walk(repo_path):
            for filename in files:
                file_path = os.path.join(root, filename)
                if should_skip(file_path, extension):
                    continue
                file_output.write(f"========== FILE: {file_path[len(repo_path)+1:]} ==========\n\n")
                try:
                    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file_input:
                        file_output.write(file_input.read())
                except Exception as e:
                    file_output.write(f"Error reading file: {e}")
                file_output.write("\n\n \n\n")
    shutil.rmtree(repo_path)
    print(f"Repository has been written to {output_file}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py [<extension>] <git url>")
        sys.exit(1)
    # Determine if the first argument is a URL or an extension
    if sys.argv[1].startswith('.'):
        if len(sys.argv) != 3:
            print("Usage: repo2text <extension> <git url>")
            sys.exit(1)
        extension = sys.argv[1].strip('.').lower()
        repo_url = sys.argv[2]
    else:
        repo_url = sys.argv[1]
        extension = None
        if len(sys.argv) == 3:
            extension = sys.argv[2].strip('.').lower()

    repo_to_text(repo_url, extension)

if __name__ == '__main__':
    main()
