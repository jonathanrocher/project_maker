""" Configuration file for creating a default Enthought project.
"""
import datetime
now = datetime.datetime.now()
current_year = now.year

# Project description
package_name = "project_maker"
project_name = "Project maker tool"
project_description = ("Tool to create a project from scratch: tree structure,"
                       " CI tools, environment tools, ...")
author = "Enthought Inc."
project_path = "."
package_version = "0.1dev"

# Copyright notice, options are "proprietary", "enthought_products", or
# "open_source" or custom (if so, modify custom_copyright below)
copyright_type = "proprietary"
custom_copyright = ""

# License: Options are "proprietary", "bsd", ...
license = "proprietary"

# CI?


# Project type. Options are "std", "canopy_data" or anything else.
# Create a custom one and create the corresponding tree_<CUSTOM> below.
project_type = "std"

# Possible tree structures
tree_std = ["app", "model", "view", "io", "utils", "doc"]
tree_canopy_data = ["addon", "addon/model", "addon/view", "addon/io", "model",
                    "view", "io", "utils", "doc"]
testing = True

# Logger?
build_logger=False
