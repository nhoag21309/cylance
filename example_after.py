import cylance as cy
import time

# Script to get device list avery 60 seconds

# CONF
tenant = ""         # Tenant ID
app = ""            # Application ID
secret = ""         # Application Secret

# ***** PART 1 - GENERATE JWT TOKEN ***** #

def main_loop():
    cy.set_creds(tenant, app, secret)
    # Note, get_token() only needs to be called once, the cylance module takes care of expiration and renewal of token automagically
    cy.get_token()

# ***** PART 2 - GET DEVICES  ***** #
    print cy.get_data("DEVICES")

while True:
    main_loop()
    time.sleep(60)