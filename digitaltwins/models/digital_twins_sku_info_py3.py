# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class DigitalTwinsSkuInfo(Model):
    """Information about the SKU of the DigitalTwinsInstance.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar name: Required. The name of the SKU. Default value: "F1" .
    :vartype name: str
    """

    _validation = {
        'name': {'required': True, 'constant': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
    }

    name = "F1"
