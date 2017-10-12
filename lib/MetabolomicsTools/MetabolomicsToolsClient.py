# -*- coding: utf-8 -*-
############################################################
#
# Autogenerated by the KBase type compiler -
# any changes made here will be overwritten
#
############################################################

from __future__ import print_function
# the following is a hack to get the baseclient to import whether we're in a
# package or not. This makes pep8 unhappy hence the annotations.
try:
    # baseclient and this client are in a package
    from .baseclient import BaseClient as _BaseClient  # @UnusedImport
except:
    # no they aren't
    from baseclient import BaseClient as _BaseClient  # @Reimport


class MetabolomicsTools(object):

    def __init__(
            self, url=None, timeout=30 * 60, user_id=None,
            password=None, token=None, ignore_authrc=False,
            trust_all_ssl_certificates=False,
            auth_svc='https://kbase.us/services/authorization/Sessions/Login'):
        if url is None:
            raise ValueError('A url is required')
        self._service_ver = None
        self._client = _BaseClient(
            url, timeout=timeout, user_id=user_id, password=password,
            token=token, ignore_authrc=ignore_authrc,
            trust_all_ssl_certificates=trust_all_ssl_certificates,
            auth_svc=auth_svc)

    def get_mona_spectra(self, params, context=None):
        """
        :param params: instance of type "GetMonaSpectraParams" -> structure:
           parameter "workspace_name" of String, parameter "compound_object"
           of type "obj_ref" (A reference to a FBAModel, CompoundSet or FBA
           object), parameter "spectra_source" of String, parameter
           "spectra_query" of String, parameter "use_inchi" of type "bool",
           parameter "use_name" of type "bool"
        :returns: instance of type "SpectraResults" -> structure: parameter
           "report_name" of String, parameter "report_ref" of String
        """
        return self._client.call_method(
            'MetabolomicsTools.get_mona_spectra',
            [params], self._service_ver, context)

    def get_mine_spectra(self, params, context=None):
        """
        :param params: instance of type "GetMineSpectraParams" -> structure:
           parameter "workspace_name" of String, parameter "compound_object"
           of type "obj_ref" (A reference to a FBAModel, CompoundSet or FBA
           object), parameter "charge" of type "bool", parameter
           "energy_levels" of list of String, parameter "use_inchi" of type
           "bool", parameter "use_name" of type "bool", parameter
           "use_source" of type "bool"
        :returns: instance of type "SpectraResults" -> structure: parameter
           "report_name" of String, parameter "report_ref" of String
        """
        return self._client.call_method(
            'MetabolomicsTools.get_mine_spectra',
            [params], self._service_ver, context)

    def status(self, context=None):
        return self._client.call_method('MetabolomicsTools.status',
                                        [], self._service_ver, context)
