# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from blueking.component.shortcuts import get_client_by_user

from pipeline.conf import settings
from pipeline.core.flow.activity import Service
from pipeline.component_framework.component import Component

from conf.default import APP_ID

# from django.utils.translation import ugettext_lazy as _

__group_name__ = u"测试原子(TEST)"
# __group_name__ = _(u"测试原子(TEST)")


class TestCustomService(Service):
    def execute(self, data, parent_data):
        executor = parent_data.get_one_of_inputs('executor')
        biz_cc_id = parent_data.get_one_of_inputs('biz_cc_id')
        client = get_client_by_user(executor)

        ip_input = data.get_one_of_inputs('eb_ip_input')
        system_radio = data.get_one_of_inputs('eb_system_radio')
        path_input = data.get_one_of_inputs('eb_path_input')

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

    def outputs_format(self):
        return [
            self.OutpputItem(name=u"磁盘使用率", key='data', type='int')
        ]


class TestCustomComponent(Component):
    name = u"磁盘容量查询"
    # name = _(u"磁盘容量查询")
    code = 'test_custom'
    bound_service = TestCustomService
    form = settings.STATIC_URL + 'custom_atoms/test/test_custom.js'
