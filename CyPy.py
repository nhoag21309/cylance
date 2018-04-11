#!/usr/bin/env python

__authors__ = ["Zack Link"]
__maintainer__ = "Zack Link"
__email__ = "zlink@cylance.com"
__version__ = "0.5"
__credits__ = []
__license__ = "GPL"

from cmd import Cmd
import json
import cylance

class MyPrompt(Cmd):
    tenant = ""
    app_id = ""
    app_secret = ""
    auth_token = ""
    authed = 0

    def do_auth(self, args):
        """Authenticate with console.  Access Tken last 30 minutes."""
        global tenant, app_id, app_secret
        cylance.set_creds(self.tenant, self.app_id, self.app_secret)
    
    def do_getUsers(self, args):
        """Get all Users.\nOptions:\n  email=<string> (contains <string>)\n  first_name=<string>\n  last_name=<string>\n  has_logged_in=<True|False>\n  user_role=<role> (e.g. Administrator is 00000000-0000-0000-0000-000000000002)\n  date_last_login=<date> (e.g.  2018-01- for Jan 2018)\n  date_email_confirmed=<date> (e.g.  2018-01- for Jan 2018)\n  date_created=<date> (e.g.  2018-01- for Jan 2018)\n  date_modified=<date> (e.g.  2018-01- for Jan 2018)\n  out <filename> (suports .json and .csv)\nOptions should be in the format: <field1>=<value1>,<field2>=<value2>,etc"""
        print cylance.get_data("USERS", args)

    def do_getDevices(self, args):
        """Get all Devices.\nOptions:\n  name=<string> (i.e. name contains <string>)\n  date_first_registered=<date> (e.g.  2018-01- for Jan 2018)\n  id=<devicce id>\n  version=<version>\n  state=<Online|Offline>\n  out=<filename> (suports .json and .csv)"""
        print cylance.get_data("DEVICES", args)

    def do_getPolicies(self, args):
        """Get all Policies.\nOptions:\n  name=<string> (i.e. name contains <string>)\n  <field2=XXX>\n  <field3=YYY>\n  <field4=ZZZ>\n  out=<filename> (suports .json and .csv)"""
        # TODO fix comments above for help
        print cylance.get_data("POLICIES", args)

    def do_getZones(self, args):
        """Get all Zones.\nOptions:\n  name=<string> (i.e. name contains <string>)\n  <field2=XXX>\n  <field3=YYY>\n  <field4=ZZZ>\n  out=<filename> (suports .json and .csv)"""
        # TODO fix comments above for help
        print cylance.get_data("ZONES", args)

    def do_getThreats(self, args):
        """Get all Threats.\nOptions:\n  name=<string> (i.e. name contains <string>)\n  <field2=XXX>\n  <field3=YYY>\n  <field4=ZZZ>\n  out=<filename> (suports .json and .csv)"""
        # TODO fix comments above for help
        print cylance.get_data("THREATS", args)

    def do_getRegions(self, args):
        """Get available geographical regions"""
        for x in cylance.get_regions():
            print x

    def do_getCurrentRegion(self, args):
        """Get current setting for selected region"""
        print cylance.get_region()

    def do_setRegion(self, args):
        """"Set region.  For a list of available regions use 'getRegions'"""
        cylance.set_region(args)

    def do_filtering(self, args):
        """All top level attributes can be filtered on.  Multiple filters can be used by putting a comma (no spaces) in between the filters.  Search string uses contains, not exact match.  Searches are case-insensitive\nExample: getDevices state=Online,name=US\n"""
        print ""

    def do_quit(self, args):
        """Quits the program."""
        print "Quitting."
        raise SystemExit

    def do_exit(self, args):
        """Exits the program."""
        print "Exitting."
        raise SystemExit

if __name__ == '__main__':
    prompt = MyPrompt()
    prompt.prompt = 'CyPy> '
    prompt.cmdloop('Starting CyPy...')
