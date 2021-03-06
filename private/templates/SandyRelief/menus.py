# -*- coding: utf-8 -*-

from gluon import *
from s3 import *
from eden.layouts import *
try:
    from .layouts import *
except ImportError:
    pass
import eden.menus as default

# =============================================================================
class S3OptionsMenu(default.S3OptionsMenu):
    """
        Custom Controller Menus

        The options menu (left-hand options menu) is individual for each
        controller, so each controller has its own options menu function
        in this class.

        Each of these option menu functions can be customized separately,
        by simply overriding (re-defining) the default function. The
        options menu function must return an instance of the item layout.

        The standard menu uses the M item layout class, but you can of
        course also use any other layout class which you define in
        layouts.py (can also be mixed).

        Make sure additional helper functions in this class don't match
        any current or future controller prefix (e.g. by using an
        underscore prefix).
    """

    # -------------------------------------------------------------------------
    def inv(self):
        """ INV / Inventory """

        ADMIN = current.session.s3.system_roles.ADMIN

        #current.s3db.inv_recv_crud_strings()
        #crud_strings = current.response.s3.crud_strings
        #inv_recv_list = crud_strings.inv_recv.title_list
        #inv_recv_search = crud_strings.inv_recv.title_search

        return M()(
                    M("Facilities", c="org", f="facility")(
                        M("New", m="create"),
                        M("List All"),
                        M("Map", m="map"),
                        M("Search", m="search"),
                        M("Import", m="import")
                    ),
                    M("Warehouse Stock", c="inv", f="inv_item")(
                        M("Search", f="inv_item", m="search"),
                        #M("Search Shipped Items", f="track_item", m="search"),
                        M("Stock Count", f="adj"),
                        #M("Kitting", f="kit"),
                        M("Import", f="inv_item", m="import", p="create"),
                    ),
                    M("Reports", c="inv", f="inv_item")(
                        M("Warehouse Stock", f="inv_item",m="report"),
                        M("Expiration Report", c="inv", f="track_item",
                          m="search", vars=dict(report="exp")),
                        #M("Monetization Report", c="inv", f="inv_item",
                        #  m="search", vars=dict(report="mon")),
                        #M("Utilization Report", c="inv", f="track_item",
                        #  m="search", vars=dict(report="util")),
                        #M("Summary of Incoming Supplies", c="inv", f="track_item",
                        #  m="search", vars=dict(report="inc")),
                        #M("Summary of Releases", c="inv", f="track_item",
                        #  m="search", vars=dict(report="rel")),
                    ),
                    #M(inv_recv_list, c="inv", f="recv")(
                    #    M("New", m="create"),
                    #    M("List All"),
                    #    M("Search", m="search"),
                    #),
                    #M("Sent Shipments", c="inv", f="send")(
                    #    M("New", m="create"),
                    #    M("List All"),
                    #    M("Search Shipped Items", f="track_item", m="search"),
                    #),
                    M("Items", c="supply", f="item")(
                        M("New", m="create"),
                        M("List All"),
                        M("Search", m="search"),
                        M("Report", m="report"),
                        M("Import", f="catalog_item", m="import", p="create"),
                    ),
                    M("Item Categories", c="supply", f="item_category",
                      restrict=[ADMIN])(
                        M("New", m="create"),
                        M("List All"),
                    ),
                )

    # -------------------------------------------------------------------------
    def org(self):
        """ ORG / Organization Registry """

        #ADMIN = current.session.s3.system_roles.ADMIN

        return M(c="org")(
                    M("Facilities", f="facility")(
                        M("New", m="create"),
                        M("List All"),
                        M("Map", m="map"),
                        M("Search", m="search"),
                        M("Import", m="import")
                    ),
                    M("Organizations", f="organisation")(
                        M("Add Organization", m="create"),
                        M("List All"),
                        M("Search", m="search"),
                        M("Import", m="import")
                    ),
                    M("Facility Types", f="facility_type",
                      #restrict=[ADMIN]
                      )(
                        M("New", m="create"),
                        M("List All"),
                    ),
                    M("Organization Types", f="organisation_type",
                      #restrict=[ADMIN]
                      )(
                        M("New", m="create"),
                        M("List All"),
                    ),
                )

    # -------------------------------------------------------------------------
    def req(self):
        """ REQ / Request Management """

        ADMIN = current.session.s3.system_roles.ADMIN

        return M(c="req")(
                    M("Requests", f="req")(
                        M("New", m="create"),
                        M("List All"),
                        M("List Recurring Requests", f="req_template"),
                        M("Search", m="search"),
                        M("Map", m="map"),
                        M("Report", m="report"),
                        M("Search All Requested Items", f="req_item", m="search"),
                        M("Search All Requested Skills", f="req_skill", m="search"),
                    ),
                    M("Priority Items", f="summary_option")(
                        M("New", m="create"),
                        M("List All"),
                    ),
                    M("Items", c="supply", f="item")(
                        M("New", m="create"),
                        M("List All"),
                        M("Search", m="search"),
                        M("Report", m="report"),
                        M("Import", f="catalog_item", m="import", p="create"),
                    ),
                    M("Item Categories", c="supply", f="item_category",
                      restrict=[ADMIN])(
                        M("New", m="create"),
                        M("List All"),
                    ),
                )

# END =========================================================================
