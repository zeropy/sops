# -*- coding: utf-8 -*-
from blueapps.utils.esbclient import get_client_by_user

from pipeline.conf import settings
from pipeline.core.flow.activity import Service
from pipeline.component_framework.component import Component
import base64

from conf.default import APP_ID

__group_name__ = u"早鸟原子(earlybird)"


class DiskCapacityService(Service):
    def execute(self, data, parent_data):
        executor = parent_data.get_one_of_inputs('executor')
        biz_cc_id = parent_data.get_one_of_inputs('biz_cc_id')
        client = get_client_by_user(executor)

        ip_input = data.get_one_of_inputs('ip')
        system_radio = data.get_one_of_inputs('system')
        path_input = data.get_one_of_inputs('path')

        api_kwargs = {
            'bk_app_code': APP_ID,
            'bk_username': executor,
            'ip': ip_input,
            'system': system_radio,
            'path': path_input
        }
        resp = client.myapi.get_dfinfo(**api_kwargs)

        if resp['result']:
            disk_usaged = resp['data'][-1]['usaged']
            data.set_outputs('data', disk_usaged)
            return True
        else:
            return False

        # 处理结果

    def outputs_format(self):
        return [
            self.OutpputItem(name=u"磁盘使用率", key='data', type='int')
        ]


class DiskCapacityComponent(Component):
    name = u"磁盘容量查询"
    code = 'diskcapacity'
    bound_service = DiskCapacityService
    form = settings.STATIC_URL + 'custom_atom/disk_capacity/dc.js'
