""" Configuration file for creating a default Enthought project.
"""
import datetime
now = datetime.datetime.now()
current_year = now.year

# Project description
package_name = "default_project"
project_name = "Default Enthought project"
project_description = "Default Enthought project"
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
