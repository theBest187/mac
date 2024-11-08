import yaml
import os

def generate_cmake(yaml_file):
    with open(yaml_file, 'r') as f:
        data = yaml.safe_load(f)

    project_name = data['project_name']
    source_dir = data['source_dir']
    source_patterns = data['source_patterns']
    dependencies = data['dependencies']

    source_files = []
    for pattern in source_patterns:
        for root, _, files in os.walk(source_dir):
            for file in files:
                source_files.append(os.path.join(root, file))

    cmake_content = f"""
cmake_minimum_required(VERSION 3.15)

project({project_name})

set(CMAKE_SYSTEM_NAME iOS)
set(CMAKE_OSX_ARCHITECTURES "arm64")
set(CMAKE_OSX_DEPLOYMENT_TARGET "12.0")

add_executable({project_name} {" ".join(source_files)})

target_link_libraries({project_name} {" ".join(dependencies)})
    """

    with open('CMakeLists.txt', 'w') as f:
        f.write(cmake_content)

if __name__ == '__main__':
    yaml_file = 'fixer.yaml'
    generate_cmake(yaml_file)
