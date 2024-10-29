import os
from pathlib import Path
import click
import jinja2

TUTORIAL_PATH = Path(__file__).parent / "templates" / "tutorial-example"

def generate_tutorial(path: Path, module_prefix: str) -> None:
    """Generate the tutorial example at a given directory."""
    click.echo(f"Creating an airlift tutorial project at {path}.")
    normalized_path = os.path.normpath(path)
    os.mkdir(normalized_path)

    loader = jinja2.FileSystemLoader(searchpath=TUTORIAL_PATH)
    env = jinja2.Environment(loader=loader)

    for root, dirs, files in os.walk(TUTORIAL_PATH):
        # For each subdirectory in the source template, create a subdirectory in the destination.
        for dirname in dirs:
            src_dir_path = os.path.join(root, dirname)
            src_relative_dir_path = os.path.relpath(src_dir_path, project_template_path)
            dst_relative_dir_path = src_relative_dir_path.replace(
                name_placeholder,
                code_location_name,
                1,
            )
            dst_dir_path = os.path.join(normalized_path, dst_relative_dir_path)

            os.mkdir(dst_dir_path)

        # For each file in the source template, render a file in the destination.
        for filename in files:
            src_file_path = os.path.join(root, filename)
            if _should_skip_file(src_file_path):
                continue

            src_relative_file_path = os.path.relpath(src_file_path, project_template_path)
            dst_relative_file_path = src_relative_file_path.replace(
                name_placeholder,
                code_location_name,
                1,
            )
            dst_file_path = os.path.join(normalized_path, dst_relative_file_path)

            if dst_file_path.endswith(".tmpl"):
                dst_file_path = dst_file_path[: -len(".tmpl")]

            with open(dst_file_path, "w", encoding="utf8") as f:
                # Jinja template names must use the POSIX path separator "/".
                template_name = src_relative_file_path.replace(os.sep, posixpath.sep)
                template = env.get_template(name=template_name)
                f.write(
                    template.render(
                        repo_name=code_location_name,  # deprecated
                        code_location_name=code_location_name,
                        dagster_version=dagster_version,
                    )
                )
                f.write("\n")

    click.echo(f"Generated files for airlift project in {path}.")