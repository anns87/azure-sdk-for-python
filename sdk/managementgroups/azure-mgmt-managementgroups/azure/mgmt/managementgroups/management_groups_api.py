# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.service_client import SDKClient
from msrest import Serializer, Deserializer
from msrestazure import AzureConfiguration
from .version import VERSION
from msrest.pipeline import ClientRawResponse
from msrest.polling import LROPoller, NoPolling
from msrestazure.polling.arm_polling import ARMPolling
import uuid
from .operations.management_groups_operations import ManagementGroupsOperations
from .operations.management_group_subscriptions_operations import ManagementGroupSubscriptionsOperations
from .operations.operations import Operations
from .operations.entities_operations import EntitiesOperations
from . import models


class ManagementGroupsAPIConfiguration(AzureConfiguration):
    """Configuration for ManagementGroupsAPI
    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, base_url=None):

        if credentials is None:
            raise ValueError("Parameter 'credentials' must not be None.")
        if not base_url:
            base_url = 'https://management.azure.com'

        super(ManagementGroupsAPIConfiguration, self).__init__(base_url)

        self.add_user_agent('azure-mgmt-managementgroups/{}'.format(VERSION))
        self.add_user_agent('Azure-SDK-For-Python')

        self.credentials = credentials


class ManagementGroupsAPI(SDKClient):
    """The Azure Management Groups API enables consolidation of multiple subscriptions/resources into an organizational hierarchy and centrally manage access control, policies, alerting and reporting for those resources.

    :ivar config: Configuration for client.
    :vartype config: ManagementGroupsAPIConfiguration

    :ivar management_groups: ManagementGroups operations
    :vartype management_groups: azure.mgmt.managementgroups.operations.ManagementGroupsOperations
    :ivar management_group_subscriptions: ManagementGroupSubscriptions operations
    :vartype management_group_subscriptions: azure.mgmt.managementgroups.operations.ManagementGroupSubscriptionsOperations
    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.managementgroups.operations.Operations
    :ivar entities: Entities operations
    :vartype entities: azure.mgmt.managementgroups.operations.EntitiesOperations

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, base_url=None):

        self.config = ManagementGroupsAPIConfiguration(credentials, base_url)
        super(ManagementGroupsAPI, self).__init__(self.config.credentials, self.config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self.api_version = '2018-03-01-preview'
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.management_groups = ManagementGroupsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.management_group_subscriptions = ManagementGroupSubscriptionsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.operations = Operations(
            self._client, self.config, self._serialize, self._deserialize)
        self.entities = EntitiesOperations(
            self._client, self.config, self._serialize, self._deserialize)

    def check_name_availability(
            self, check_name_availability_request, custom_headers=None, raw=False, **operation_config):
        """Checks if the specified management group name is valid and unique.

        :param check_name_availability_request: Management group name
         availability check parameters.
        :type check_name_availability_request:
         ~azure.mgmt.managementgroups.models.CheckNameAvailabilityRequest
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: CheckNameAvailabilityResult or ClientRawResponse if raw=true
        :rtype:
         ~azure.mgmt.managementgroups.models.CheckNameAvailabilityResult or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<azure.mgmt.managementgroups.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.check_name_availability.metadata['url']

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct body
        body_content = self._serialize.body(check_name_availability_request, 'CheckNameAvailabilityRequest')

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters, body_content)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('CheckNameAvailabilityResult', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    check_name_availability.metadata = {'url': '/providers/Microsoft.Management/checkNameAvailability'}

    def start_tenant_backfill(
            self, custom_headers=None, raw=False, **operation_config):
        """Starts backfilling subscriptions for the Tenant.

        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: TenantBackfillStatusResult or ClientRawResponse if raw=true
        :rtype: ~azure.mgmt.managementgroups.models.TenantBackfillStatusResult
         or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<azure.mgmt.managementgroups.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.start_tenant_backfill.metadata['url']

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('TenantBackfillStatusResult', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    start_tenant_backfill.metadata = {'url': '/providers/Microsoft.Management/startTenantBackfill'}

    def tenant_backfill_status(
            self, custom_headers=None, raw=False, **operation_config):
        """Gets tenant backfill status.

        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: TenantBackfillStatusResult or ClientRawResponse if raw=true
        :rtype: ~azure.mgmt.managementgroups.models.TenantBackfillStatusResult
         or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<azure.mgmt.managementgroups.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.tenant_backfill_status.metadata['url']

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('TenantBackfillStatusResult', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    tenant_backfill_status.metadata = {'url': '/providers/Microsoft.Management/tenantBackfillStatus'}
