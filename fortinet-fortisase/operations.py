import json

from connectors.core.connector import get_logger, ConnectorError

from .fortisase_api_auth import FortiSASE, check

logger = get_logger('fortinet-fortisase')


def get_service(config, params):
    try:
        service_name = params.get('service_name')
        if not service_name:
            raise ConnectorError("Service name is required")

        co = FortiSASE(config)
        endpoint = f"/resource-api/v2/security/services/{service_name}"
        return co.make_rest_call(endpoint, 'GET')
    except Exception as err:
        logger.exception(f"{str(err)}")
        raise ConnectorError(f"{str(err)}")


def get_services(config, params=None):
    co = FortiSASE(config)
    endpoint = "/resource-api/v2/security/services"
    return co.make_rest_call(endpoint, 'GET')


def create_service(config, params):
    co = FortiSASE(config)
    endpoint = "/resource-api/v2/security/services"
    payload = {
        "primaryKey": params.get('primaryKey'),
        "category": params.get('category'),
        "protocol": params.get('protocol'),
        "tcpPortrange": params.get('tcpPortrange')
    }
    return co.make_rest_call(endpoint, 'POST', data=json.dumps(payload))


def delete_service(config, params):
    co = FortiSASE(config)
    endpoint = f"/resource-api/v2/security/services/{params.get('primaryKey')}"
    return co.make_rest_call(endpoint, 'DELETE')


def get_host(config, params):
    try:
        host_name = params.get('host_name')
        if not host_name:
            raise ConnectorError("Host name is required")

        co = FortiSASE(config)
        endpoint = f"/resource-api/v2/network/hosts/{host_name}"
        return co.make_rest_call(endpoint, 'GET')
    except Exception as err:
        logger.exception(f"{str(err)}")
        raise ConnectorError(f"{str(err)}")


def get_hosts(config, params=None):
    co = FortiSASE(config)
    endpoint = "/resource-api/v2/network/hosts"
    return co.make_rest_call(endpoint, 'GET')


def create_host(config, params):
    try:
        co = FortiSASE(config)
        endpoint = "/resource-api/v2/network/hosts"
        payload = {
            "primaryKey": params['primaryKey'],
            "type": params['type'],
            "location": params['location']
        }

        # Add type-specific fields
        host_type = params['type']
        if host_type == 'ipmask':
            payload['subnet'] = params['subnet']
        elif host_type == 'iprange':
            payload['startIp'] = params['startIp']
            payload['endIp'] = params['endIp']
        elif host_type == 'fqdn':
            payload['fqdn'] = params['fqdn']
        elif host_type == 'geography':
            payload['countryId'] = params['countryId']

        return co.make_rest_call(endpoint, 'POST', data=json.dumps(payload))
    except Exception as err:
        logger.exception(f"Error in create_host: {str(err)}")
        raise ConnectorError(f"Error in create_host: {str(err)}")


def delete_host(config, params):
    co = FortiSASE(config)
    endpoint = f"/resource-api/v2/network/hosts/{params.get('primaryKey')}"
    return co.make_rest_call(endpoint, 'DELETE')


def create_to_hub_policy(config, params):
    co = FortiSASE(config)
    endpoint = "/resource-api/v1/security/internal/policies"
    return co.make_rest_call(endpoint, 'POST', data=json.dumps(params))


def create_from_hub_policy(config, params):
    co = FortiSASE(config)
    endpoint = "/resource-api/v1/security/internal-reverse/policies"
    return co.make_rest_call(endpoint, 'POST', data=json.dumps(params))


def generic_api_call(config, params):
    try:
        method = params.get('method')
        endpoint = params.get('endpoint')
        data = params.get('data')

        co = FortiSASE(config)

        if data and isinstance(data, str):
            try:
                data = json.loads(data)
            except json.JSONDecodeError:
                raise ConnectorError("Invalid JSON in 'data' parameter")

        return co.make_rest_call(endpoint, method, data=json.dumps(data) if data else None)
    except Exception as err:
        logger.exception(f"{str(err)}")
        raise ConnectorError(f"{str(err)}")


def _check_health(config):
    try:
        return check(config)
    except Exception as err:
        logger.exception(f"{str(err)}")
        raise ConnectorError(f"{str(err)}")


operations = {
    'get_service': get_service,
    'get_services': get_services,
    'create_service': create_service,
    'delete_service': delete_service,
    "get_host": get_host,
    "get_hosts": get_hosts,
    'create_host': create_host,
    'delete_host': delete_host,
    'create_to_hub_policy': create_to_hub_policy,
    'create_from_hub_policy': create_from_hub_policy,
}
