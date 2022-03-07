# Open Source Context Python Library (PyCurl)

### This project provides users with a common code base to use when interacting with the Open Source Context API using Python and PyCurl

In order to use this library users will need the following:

* An API key for the Open Source Conetext API. More information available at https://oscontext.com
* Installed, working Python3 installation
* Installed, working PyCurl library
* A copy of the API specification provided by your Open Source Context representative (for reference).

This library is primarily developed and maintained on linux (Ubuntu and Fedora) and Apple MacOS (Big Sur and Monterey) systems. Limited testing is done on Windows based systems.

##PassiveDNS Functionality
There are four "simple" methods for querying pDNS in this library.

### d\_ip\_query
This funsction allows for the simple querying of an IP address or CIDR range.

* query (required) - This should be the IP address or CIDR range being queried. (I.e. '192.168.0.1' or '192.168.0.0/24')
* apikey (required) - The API key assigned to you by Open Source Context (more info at https://oscontext.com)
* size (optional) - The number of results you would like returned, up to 100,000. The default is 100.
* url (optional) - THe base URI for the pDNS endpoint. The default setting will be correct for anyone who has not been assigned a custom endpoint.
* sort (optional) - The field and order you would like the results sorted by. The default is last_seen:desc
* fields (optional) - This is where the user can specify the fields
