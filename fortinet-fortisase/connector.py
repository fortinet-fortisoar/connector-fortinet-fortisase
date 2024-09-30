"""
Copyright start
MIT License
Copyright (c) 2024 Fortinet Inc
Copyright end
"""

from connectors.core.connector import get_logger, ConnectorError, Connector
from .operations import operations, _check_health

logger = get_logger('fortinet-fortisase')


class FortiSASE(Connector):
    def execute(self, config, operation, params, **kwargs):
        try:
            operation = operations.get(operation)
        except Exception as err:
            logger.exception(err)
            raise ConnectorError(err)
        return operation(config, params)

    def check_health(self, config):
        return _check_health(config)
