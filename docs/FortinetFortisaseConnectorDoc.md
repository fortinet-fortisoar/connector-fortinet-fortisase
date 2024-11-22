## About the connector
FortiSASE is a cloud-delivered security service edge (SSE) solution that provides always-on secure access to private applications. This connector facilitates automated operations to manage services, hosts, host groups, and policies.
<p>This document provides information about the Fortinet FortiSASE Connector, which facilitates automated interactions, with a Fortinet FortiSASE server using FortiSOAR&trade; playbooks. Add the Fortinet FortiSASE Connector as a step in FortiSOAR&trade; playbooks and perform automated operations with Fortinet FortiSASE.</p>

### Version information

Connector Version: 1.0.0

FortiSOAR&trade; Version Tested on: 7.6.0-5012

Fortinet FortiSASE Version Tested on: v24.4.32

Authored By: Fortinet CSE

Certified: Yes
## Installing the connector
<p>Use the <strong>Content Hub</strong> to install the connector. For the detailed procedure to install a connector, click <a href="https://docs.fortinet.com/document/fortisoar/0.0.0/installing-a-connector/1/installing-a-connector" target="_top">here</a>.</p><p>You can also use the <code>yum</code> command as a root user to install the connector:</p>
<pre>yum install cyops-connector-fortinet-fortisase</pre>

## Prerequisites to configuring the connector
- You must have the credentials of Fortinet FortiSASE server to which you will connect and perform automated operations.
- The FortiSOAR&trade; server should have outbound connectivity to port 443 on the Fortinet FortiSASE server.

## Minimum Permissions Required
- Not applicable

## Configuring the connector
For the procedure to configure a connector, click [here](https://docs.fortinet.com/document/fortisoar/0.0.0/configuring-a-connector/1/configuring-a-connector)
### Configuration parameters
<p>In FortiSOAR&trade;, on the Connectors page, click the <strong>Fortinet FortiSASE</strong> connector row (if you are in the <strong>Grid</strong> view on the Connectors page) and in the <strong>Configurations</strong> tab enter the required configuration details:</p>
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Server URL</td><td>Specify the URL of the FortiSASE server to connect and perform automated operations.
</td>
</tr><tr><td>Authentication Method</td><td>Select the authentication method. You can choose from the following options: Username/Password (Default), Token.
<br><strong>If you choose 'Username/Password'</strong><ul><li>Username: Username to access the Fortinet FortiSASE server to which you will connect and perform the automated operations.</li><li>Password: Password to access the Fortinet FortiSASE server to which you will connect and perform the automated operations.</li><li>Client ID: Client to access the Fortinet FortiSASE server to which you will connect and perform the automated operations.</li></ul><strong>If you choose 'Token'</strong><ul><li>Token: Authorization token to access the Fortinet FortiSASE server to which you will connect and perform the automated operations.</li></ul></td>
</tr><tr><td>Verify SSL</td><td>Specifies whether the SSL certificate for the server is to be verified or not. <br/>By default, this option is set to True.</td></tr>
</tbody></table>

## Actions supported by the connector
The following automated operations can be included in playbooks and you can also use the annotations to access operations from FortiSOAR&trade; release 4.10.0 and onwards:
<table border=1><thead><tr><th>Function</th><th>Description</th><th>Annotation and Category</th></tr></thead><tbody><tr><td>Get Service</td><td>Retrieves a service based on the service name you have specified.</td><td>get_service <br/>Investigation</td></tr>
<tr><td>Get Services List</td><td>Retrieves a list of all services.</td><td>get_services <br/>Investigation</td></tr>
<tr><td>Create Service</td><td>Creates a new service based on the primary key, category, protocol and port range you have specified.</td><td>create_service <br/>Investigation</td></tr>
<tr><td>Delete Service</td><td>Deletes a service based on the primary key you have specified.</td><td>delete_service <br/>Investigation</td></tr>
<tr><td>Get Host</td><td>Retrieves a host based on the host name you have specified.</td><td>get_host <br/>Investigation</td></tr>
<tr><td>Create Host</td><td>Creates a new host based on the host name, type and location you have specified.</td><td>create_host <br/>Investigation</td></tr>
<tr><td>Delete Host</td><td>Deletes a host based on the primary key you have specified.</td><td>delete_host <br/>Investigation</td></tr>
<tr><td>Generic API Call</td><td>Make a generic API call to Fortinet FortiSASE.</td><td>generic_api_call <br/>Investigation</td></tr>
</tbody></table>

### operation: Get Service
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Service Name</td><td>Specify the name of the service to retrieve.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "primaryKey": "",
    "category": "",
    "protocol": "",
    "tcpPortrange": ""
}</pre>
### operation: Get Services List
#### Input parameters
None.
#### Output
The output contains the following populated JSON schema:

<pre>{
    "services": []
}</pre>
### operation: Create Service
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Primary Key</td><td>Specify the unique identifier for the service that you want to create.
</td></tr><tr><td>Category</td><td>Specify the category that you want to assign to the service you want to create.
</td></tr><tr><td>Protocol</td><td>Specify the protocol used by the service you want to create.
</td></tr><tr><td>Port Range</td><td>Specify the port range that you want to assign to the service you want to create. e.g. {"tcpPortrange": [{"destination": {"low": 1, "high": 2}}]} or {"udpPortrange": [{"destination": {"low": 1, "high": 2}}]}
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "service": {}
}</pre>
### operation: Delete Service
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Primary Key</td><td>Unique identifier of the service to delete.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "result": ""
}</pre>
### operation: Get Host
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Host Name</td><td>Specify the name of the host to retrieve.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "primaryKey": "",
    "type": "",
    "location": "",
    "subnet": ""
}</pre>
### operation: Create Host
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Host Name</td><td>Specify the unique identifier for the host that you want to create.
</td></tr><tr><td>Location</td><td>Select the location of the host that you want to create. You can choose from the following options: "Ingress", "Internet", "Private Access Hub", "Unspecified" (Default)
<br><strong>If you choose 'Ingress'</strong><ul><li>Host Type: Select the type of the host that you want to create. You can choose from the following options: "IP Mask" (Default), "IP Range"</li><strong>If you choose 'IP Mask'</strong><ul><li>Subnet: Subnet of the host (required for ipmask type)</li></ul><strong>If you choose 'IP Range'</strong><ul><li>Start IP: Start IP address (required for iprange type)</li><li>End IP: End IP address (required for iprange type)</li></ul></ul><strong>If you choose 'Internet'</strong><ul><li>Host Type: Select the type of the host that you want to create. You can choose from the following options: "IP Mask" (Default), "IP Range", "FQDN", "Geography"</li><strong>If you choose 'IP Mask'</strong><ul><li>Subnet: Subnet of the host (required for ipmask type)</li></ul><strong>If you choose 'IP Range'</strong><ul><li>Start IP: Start IP address (required for iprange type)</li><li>End IP: End IP address (required for iprange type)</li></ul><strong>If you choose 'FQDN'</strong><ul><li>FQDN: Fully Qualified Domain Name (required for fqdn type)</li></ul><strong>If you choose 'Geography'</strong><ul><li>Country ID: Two-letter country code (required for geography type)</li></ul></ul><strong>If you choose 'Private Access Hub'</strong><ul><li>Host Type: Select the type of the host that you want to create. You can choose from the following options: "IP Mask" (Default), "IP Range", "FQDN", "Geography"</li><strong>If you choose 'IP Mask'</strong><ul><li>Subnet: Subnet of the host (required for ipmask type)</li></ul><strong>If you choose 'IP Range'</strong><ul><li>Start IP: Start IP address (required for iprange type)</li><li>End IP: End IP address (required for iprange type)</li></ul><strong>If you choose 'FQDN'</strong><ul><li>FQDN: Fully Qualified Domain Name (required for fqdn type)</li></ul><strong>If you choose 'Geography'</strong><ul><li>Country ID: Two-letter country code (required for geography type)</li></ul></ul><strong>If you choose 'Unspecified'</strong><ul><li>Host Type: Select the type of the host that you want to create. You can choose from the following options: "IP Mask" (Default), "IP Range", "FQDN", "Geography"</li><strong>If you choose 'IP Mask'</strong><ul><li>Subnet: Subnet of the host (required for ipmask type)</li></ul><strong>If you choose 'IP Range'</strong><ul><li>Start IP: Start IP address (required for iprange type)</li><li>End IP: End IP address (required for iprange type)</li></ul><strong>If you choose 'FQDN'</strong><ul><li>FQDN: Fully Qualified Domain Name (required for fqdn type)</li></ul><strong>If you choose 'Geography'</strong><ul><li>Country ID: Two-letter country code (required for geography type)</li></ul></ul></td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "host": {}
}</pre>
### operation: Delete Host
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Primary Key</td><td>Unique identifier of the service to delete.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "result": ""
}</pre>
### operation: Generic API Call
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>HTTP Method</td><td>The HTTP method for the API call (e.g., GET, POST, PUT, DELETE)
</td></tr><tr><td>API Endpoint</td><td>The API endpoint to call (e.g., /resource-api/v2/security/services)
</td></tr><tr><td>Request Data</td><td>JSON data to send with the request (for POST, PUT methods)
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "result": {}
}</pre>
## Included playbooks
The `Sample - fortinet-fortisase - 1.0.0` playbook collection comes bundled with the Fortinet FortiSASE connector. These playbooks contain steps using which you can perform all supported actions. You can see bundled playbooks in the **Automation** > **Playbooks** section in FortiSOAR&trade; after importing the Fortinet FortiSASE connector.

- Create Host
- Create Service
- Delete Host
- Delete Service
- Generic API Call
- Get Host
- Get Service
- Get Services List

**Note**: If you are planning to use any of the sample playbooks in your environment, ensure that you clone those playbooks and move them to a different collection since the sample playbook collection gets deleted during connector upgrade and delete.
