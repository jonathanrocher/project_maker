""" Usage: copy the sample config file where you want to create a new project,
modify it with info about your project and run:
    % python project_maker MY_CONFIG_FILE
"""

import os
from argparse import ArgumentParser
from os.path import abspath, exists, join, split, splitext
from importlib import import_module
import shutil

from project_maker.utils.setup_content import setup_content
from project_maker.utils import license_notices
from project_maker.utils.gitignore_content import std_gitignore_content
from project_maker.utils import copyright_notices


def run():
    # argument parsing
    parser = ArgumentParser(description="Create the shell of a new Enthought project")
    parser.add_argument("config", help="Config file describing the project")
    args = parser.parse_args()
    path, basename = split(abspath(args.config))
    mod_name = splitext(basename)[0]
    config_module = import_module(mod_name, path)
    make_project(config_module)


def make_project(config, do_hidden=False):
    # General tree structure and setup.py
    make_tree_structure(config)

    # Make all standard txt files: Readme, license, change log, dependencies
    make_std_txt_files(config)

    if do_hidden:
        # Make all hidden files: gitignore, CI, ...
        make_std_hidden_files(config)


def make_tree_structure(config, overwrite=False):
    """
    """
    copyright_type = config.copyright_type
    if copyright_type == "custom":
        copyright_content = config.custom_copyright
    else:
        copyright_content = getattr(copyright_notices, copyright_type)

    package_location = join(config.project_path, config.package_name)
    if exists(package_location) and not overwrite:
        raise IOError("Package folder %s already exists."
                      % abspath(package_location))
    if exists(package_location):
        shutil.rmtree(package_location)
    os.mkdir(package_location)
    with open(join(package_location, "__init__.py"), "w") as f:
            f.write(copyright_content)

    setup = join(config.project_path, "setup.py")
    if exists(setup) and not overwrite:
        raise IOError("%s already exists." % abspath(setup))

    with open(setup, "w") as f:
            f.write(build_setup(config))

    project_type = config.project_type
    tree_structure_name = "tree_" + project_type
    tree_structure = getattr(config, tree_structure_name)
    for folder_name in tree_structure:
        folder_path = join(package_location, folder_name)
        os.mkdir(folder_path)
        with open(join(folder_path, "__init__.py"), "w") as f:
            f.write(copyright_content)

        if folder_name != "doc":
            tests_folder_path = join(folder_path, "tests")
            os.mkdir(tests_folder_path)
            with open(join(tests_folder_path, "__init__.py"), "w") as f:
                f.write(copyright_content)


def build_setup(config):
    return setup_content % (config.package_name, config.package_version,
                            config.license, config.project_description)

def make_std_txt_files(config):
    license_type = config.license
    license_content = getattr(license_notices, license_type + "_license")
    with open(join(config.project_path, "LICENSE.txt"), "w") as f:
        f.write(license_content)

    readme_content = create_readme_content(config)
    with open(join(config.project_path, "README.rst"), "w") as f:
        f.write(readme_content)

    changelog_content = "Change log for %s\n" % config.project_name
    with open(join(config.project_path, "CHANGES.txt"), "w") as f:
        f.write(changelog_content)

    manifest_content = "\n"
    with open(join(config.project_path, "MANIFEST.in"), "w") as f:
        f.write(manifest_content)

def make_std_hidden_files(config):
    gitignore_content = std_gitignore_content
    with open(join(config.project_path, ".gitignore"), "w") as f:
        f.write(gitignore_content)


def create_readme_content(config):
    readme_content = "=" * len(config.project_name) + "\n"
    readme_content += config.project_name + "\n"
    readme_content += "=" * len(config.project_name) + "\n\n"
    readme_content += config.project_description + "\n\n"
    readme_content += "Usage\n-----\n\n"
    readme_content += "Dependencies\n------------\n\n"
    readme_content += "Installation\n------------\n\n"
    readme_content += "Code structure\n--------------\n\n"
    return readme_content

if __name__ == "__main__":
    run()
