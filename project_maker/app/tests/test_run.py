import shutil
import os
from nose.tools import assert_in

def test_run():
    from project_maker.utils import config
    from project_maker.app import run

    TEMP_DIR = "TEMP_DIR"
    os.mkdir(TEMP_DIR)
    os.chdir(TEMP_DIR)
    try:
        run.make_project(config)
        expected_content = [config.package_name, "LICENSE.txt", "CHANGES.txt",
                            "README.rst"]
        for entry in expected_content:
            assert_in(entry, os.listdir("."))
    finally:
        os.chdir("..")
        shutil.rmtree(TEMP_DIR)
