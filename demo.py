#Connect to a vCenter Server
import requests
import urllib3
from vmware.vapi.vsphere.client import create_vsphere_client
session = requests.session()

# Disable cert verification for demo purpose.
# This is not recommended in a production environment.
session.verify = False

# Disable the secure connection warning for demo purpose.
# This is not recommended in a production environment.
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Connect to a vCenter Server using username and password
vsphere_client = create_vsphere_client(server='<vc_ip>', username='<vc_username>', password='<vc_password>', session=session)

# List all VMs inside the vCenter Server
vsphere_client.vcenter.VM.list()


#Connect to VMware Cloud on AWS
from vmware.vapi.vmc.client import create_vmc_client

# Connect to VMware Cloud on AWS using refresh token
vmc_client = create_vmc_client('<refresh_token>')

# Get organizations associated with calling user.
vmc_client.Orgs.list()