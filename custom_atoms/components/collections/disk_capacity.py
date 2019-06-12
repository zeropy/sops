# -*- coding: utf-8 -*-
from blueapps.utils.esbclient import get_client_by_user

from pipeline.conf import settings
from pipeline.core.flow.activity import Service
from pipeline.component_framework.component import Component

__group_name__ = u"早鸟原子(earlybird)"


class DiskCapacityService(Service):
    def execute(self, data, parent_data):
        executor = parent_data.get_one_of_inputs('executor')
        biz_cc_id = parent_data.get_one_of_inputs('biz_cc_id')
        client = get_client_by_user(executor)

        ip_input = data.get_one_of_inputs('ip')
        system_radio = data.get_one_of_inputs('system')
        path = data.get_one_of_inputs('path')

        api_kwargs = {}
        resp = client.job.fast_execute_script(**api_kwargs)

        # 处理结果

    def schedule(self):
        pass

    def outputs_format(self):
        return []


class DiskCapacityComponent(Component):
    name = u"磁盘容量查询"
    code = 'diskcapacity'
    bound_service = DiskCapacityService
    form = settings.STATIC_URL + 'custom_atom/disk_capacity/dc.js'
