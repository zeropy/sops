# -*- coding: utf-8 -*-

from ..base import ComponentAPI


class CollectionsMyAPI(object):
    def __init_(self, client):
        self.client = client

        self.get_dfinfo = ComponentAPI(
            client=self.client, method='GET',
            path='/api/c/self-service-api/host/get_dfinfo_lanhaibin/',
            description=u"内存使用率查询"
        )
