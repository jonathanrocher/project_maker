import datetime
now = datetime.datetime.now()
current_year = now.year

proprietary = """#
# This file is confidential and NOT open source. Do not distribute.
#
"""

enthought_products = """#
# Enthought product code
#
# (C) Copyright %s Enthought, Inc., Austin, TX
# All right reserved.
#
# This file is confidential and NOT open source. Do not distribute.
""" % current_year


open_source = """#
# Enthought product code
#
# (C) Copyright %s Enthought, Inc., Austin, TX
# All right reserved.
#
# This file is open source. Please see LICENSE.txt for more details.
""" % current_year
