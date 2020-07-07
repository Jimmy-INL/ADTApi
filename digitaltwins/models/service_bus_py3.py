# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .digital_twins_endpoint_resource_properties_py3 import DigitalTwinsEndpointResourceProperties


class ServiceBus(DigitalTwinsEndpointResourceProperties):
    """properties related to servicebus.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar provisioning_state: The provisioning state. Possible values include:
     'Provisioning', 'Deleting', 'Succeeded', 'Failed', 'Canceled'
    :vartype provisioning_state: str or
     ~digitaltwins.models.EndpointProvisioningState
    :ivar created_time: Time when the Endpoint was added to
     DigitalTwinsInstance.
    :vartype created_time: datetime
    :param tags: The resource tags.
    :type tags: dict[str, str]
    :param endpoint_type: Required. Constant filled by server.
    :type endpoint_type: str
    :param primary_connection_string: Required. PrimaryConnectionString of the
     endpoint. Will be obfuscated during read
    :type primary_connection_string: str
    :param secondary_connection_string: Required. SecondaryConnectionString of
     the endpoint. Will be obfuscated during read
    :type secondary_connection_string: str
    """

    _validation = {
        'provisioning_state': {'readonly': True},
        'created_time': {'readonly': True},
        'endpoint_type': {'required': True},
        'primary_connection_string': {'required': True},
        'secondary_connection_string': {'required': True},
    }

    _attribute_map = {
        'provisioning_state': {'key': 'provisioningState', 'type': 'str'},
        'created_time': {'key': 'createdTime', 'type': 'iso-8601'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'endpoint_type': {'key': 'endpointType', 'type': 'str'},
        'primary_connection_string': {'key': 'primaryConnectionString', 'type': 'str'},
        'secondary_connection_string': {'key': 'secondaryConnectionString', 'type': 'str'},
    }

    def __init__(self, *, primary_connection_string: str, secondary_connection_string: str, tags=None, **kwargs) -> None:
        super(ServiceBus, self).__init__(tags=tags, **kwargs)
        self.primary_connection_string = primary_connection_string
        self.secondary_connection_string = secondary_connection_string
        self.endpoint_type = 'ServiceBus'