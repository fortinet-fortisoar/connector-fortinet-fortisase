"""
Copyright start
MIT License
Copyright (c) 2024 Fortinet Inc
Copyright end
"""

import importlib
import pytest

# Import test configuration
from .data import TEST_CONFIG_TOKEN

# Dynamically import the modules
fortisase_operations = importlib.import_module('fortinet-fortisase.operations')
fortisase_auth = importlib.import_module('fortinet-fortisase.fortisase_api_auth')

# Import specific functions
get_service = fortisase_operations.get_service
get_services = fortisase_operations.get_services
create_service = fortisase_operations.create_service
delete_service = fortisase_operations.delete_service
get_host = fortisase_operations.get_host
create_host = fortisase_operations.create_host
delete_host = fortisase_operations.delete_host
create_to_hub_policy = fortisase_operations.create_to_hub_policy
create_from_hub_policy = fortisase_operations.create_from_hub_policy
generic_api_call = fortisase_operations.generic_api_call
check = fortisase_auth.check


# @pytest.fixture(params=[TEST_CONFIG_USER, TEST_CONFIG_TOKEN])
@pytest.fixture(params=[TEST_CONFIG_TOKEN])
def config(request):
    # Check the health of the connection before running tests
    assert check(request.param)
    return request.param


def test_get_service(config):
    result = get_service(config, {"service_name": "HTTP"})
    assert isinstance(result, dict)
    code = result.get('code')
    assert code == 200
    service = result.get('data')
    assert isinstance(service, list)
    assert len(service) == 1
    assert service[0]["primaryKey"] == "HTTP"


def test_get_services(config):
    result = get_services(config)
    assert isinstance(result, dict)
    code = result.get('code')
    assert code == 200
    services = result.get('data')
    assert isinstance(services, list)
    assert len(services) > 0


def test_create_and_delete_service(config):
    # Create a service
    create_params = {
        "primaryKey": "test-service-1",
        "category": "Uncategorized",
        "protocol": "TCP/UDP/SCTP",
        "tcpPortrange": [{"destination": {"low": 8080}}]
    }
    create_result = create_service(config, create_params)
    assert isinstance(create_result, dict)
    code = create_result.get('code')
    assert code == 200
    service = create_result.get('data')
    assert isinstance(service, dict)
    assert "primaryKey" in service
    assert service["primaryKey"] == "test-service-1"

    # Delete the service
    delete_params = {"primaryKey": "test-service-1"}
    delete_result = delete_service(config, delete_params)
    assert isinstance(delete_result, dict)
    code = delete_result.get('code')
    assert code == 200
    service = delete_result.get('data')
    assert isinstance(service, dict)
    assert "primaryKey" in service
    assert service["primaryKey"] == "test-service-1"

    # try to get the service again
    result = get_service(config, {"service_name": "test-service-1"})
    assert isinstance(result, dict)
    code = result.get('code')
    assert code == 404
    error = result.get('error')
    assert isinstance(error, dict)
    error_message = error.get('message')
    assert error_message.startswith('Resource Not Found')


def test_get_host(config):
    # Assume a host named "test-host" exists
    result = get_host(config, {"host_name": "gmail.com"})
    assert isinstance(result, dict)
    code = result.get('code')
    assert code == 200
    host = result.get('data')
    assert isinstance(host, list)
    assert len(host) == 1
    assert host[0]["primaryKey"] == "gmail.com"


def test_create_and_delete_ipmask_host(config):
    create_params = {
        "primaryKey": "test-ipmask-host",
        "type": "ipmask",
        "location": "unspecified",
        "subnet": "192.168.1.0/24"
    }
    _test_create_and_delete_host(config, create_params)


def test_create_and_delete_iprange_host(config):
    create_params = {
        "primaryKey": "test-iprange-host",
        "type": "iprange",
        "location": "unspecified",
        "startIp": "192.168.1.1",
        "endIp": "192.168.1.254"
    }
    _test_create_and_delete_host(config, create_params)


def test_create_and_delete_fqdn_host(config):
    create_params = {
        "primaryKey": "test-fqdn-host",
        "type": "fqdn",
        "location": "unspecified",
        "fqdn": "test.example.com"
    }
    _test_create_and_delete_host(config, create_params)


def test_create_and_delete_geography_host(config):
    create_params = {
        "primaryKey": "test-geography-host",
        "type": "geography",
        "location": "unspecified",
        "countryId": "US"
    }
    _test_create_and_delete_host(config, create_params)


def _test_create_and_delete_host(config, create_params):
    # Create the host
    create_result = create_host(config, create_params)
    assert isinstance(create_result, dict)
    code = create_result.get('code')
    assert code == 200, f"Failed to create host. Response: {create_result}"
    host = create_result.get('data')
    assert isinstance(host, dict)
    assert "primaryKey" in host
    assert host["primaryKey"] == create_params["primaryKey"]

    # Delete the host
    delete_params = {"primaryKey": create_params["primaryKey"]}
    delete_result = delete_host(config, delete_params)
    assert isinstance(delete_result, dict)
    code = delete_result.get('code')
    assert code == 200, f"Failed to delete host. Response: {delete_result}"
    host = delete_result.get('data')
    assert isinstance(host, dict)
    assert "primaryKey" in host
    assert host["primaryKey"] == create_params["primaryKey"]

    # Try to get the deleted host
    result = get_host(config, {"host_name": create_params["primaryKey"]})
    assert isinstance(result, dict)
    code = result.get('code')
    assert code == 404, f"Host still exists after deletion. Response: {result}"
    error = result.get('error')
    assert isinstance(error, dict)
    error_message = error.get('message')
    assert error_message.startswith('Resource Not Found')


# def test_create_to_hub_policy(config):
#     policy_params = {
#         "name": "test-to-hub-policy",
#         "enabled": True,
#         "source": {"hosts": [{"key": "test-host-1", "source": "security/hosts"}]},
#         "destination": {"hosts": [{"key": "0.0.0.0/0", "source": "security/hosts"}]},
#         "services": [{"key": "ALL", "source": "security/services"}],
#         "action": "accept"
#     }
#     result = create_to_hub_policy(config, policy_params)
#     assert isinstance(result, dict)
#     assert "name" in result
#     assert result["name"] == "test-to-hub-policy"
#
#
# def test_create_from_hub_policy(config):
#     policy_params = {
#         "name": "test-from-hub-policy",
#         "enabled": True,
#         "source": {"hosts": [{"key": "0.0.0.0/0", "source": "security/hosts"}]},
#         "destination": {"hosts": [{"key": "test-host-1", "source": "security/hosts"}]},
#         "services": [{"key": "HTTP", "source": "security/services"}],
#         "action": "accept"
#     }
#     result = create_from_hub_policy(config, policy_params)
#     assert isinstance(result, dict)
#     assert "name" in result
#     assert result["name"] == "test-from-hub-policy"


def test_get_nonexistent_host(config):
    host = get_host(config, {"host_name": "nonexistent-host"})
    assert isinstance(host, dict)
    code = host.get('code')
    assert code == 404
    error = host.get('error')
    assert isinstance(error, dict)
    error_message = error.get('message')
    assert error_message.startswith('Resource Not Found')


def test_generic_api_call(config):
    # Test GET request
    get_params = {
        "method": "GET",
        "endpoint": "/resource-api/v2/security/services/HTTP"
    }
    get_result = generic_api_call(config, get_params)
    assert isinstance(get_result, dict)
    assert get_result.get('code') == 200
    assert isinstance(get_result.get('data'), list)
    assert len(get_result['data']) == 1
    assert get_result['data'][0]["primaryKey"] == "HTTP"

    # Test POST request (create a new service)
    post_params = {
        "method": "POST",
        "endpoint": "/resource-api/v2/security/services",
        "data": {
            "primaryKey": "test-generic-service",
            "category": "Uncategorized",
            "protocol": "TCP/UDP/SCTP",
            "tcpPortrange": [{"destination": {"low": 9090}}]
        }
    }
    post_result = generic_api_call(config, post_params)
    assert isinstance(post_result, dict)
    assert post_result.get('code') == 200
    assert post_result['data']["primaryKey"] == "test-generic-service"

    # Test DELETE request (delete the created service)
    delete_params = {
        "method": "DELETE",
        "endpoint": "/resource-api/v2/security/services/test-generic-service"
    }
    delete_result = generic_api_call(config, delete_params)
    assert isinstance(delete_result, dict)
    assert delete_result.get('code') == 200
    assert delete_result['data']["primaryKey"] == "test-generic-service"

    # Verify the service is deleted
    get_deleted_params = {
        "method": "GET",
        "endpoint": "/resource-api/v2/security/services/test-generic-service"
    }
    get_deleted_result = generic_api_call(config, get_deleted_params)
    assert isinstance(get_deleted_result, dict)
    assert get_deleted_result.get('code') == 404
    assert 'error' in get_deleted_result
    assert get_deleted_result['error']['message'].startswith('Resource Not Found')
# Add more tests as needed
