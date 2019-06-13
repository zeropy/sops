# -*- coding: utf-8 -*-
from blueapps.utils.esbclient import get_client_by_user

from pipeline.conf import settings
from pipeline.core.flow.activity import Service
from pipeline.component_framework.component import Component
import base64

from conf.default import APP_ID, APP_TOKEN

__group_name__ = u"早鸟原子(earlybird)"


class DiskCapacityService(Service):
    def _get_job_log(self, job_id):
        pass

    def execute(self, data, parent_data):
        executor = parent_data.get_one_of_inputs('executor')
        biz_cc_id = parent_data.get_one_of_inputs('biz_cc_id')
        client = get_client_by_user(executor)

        ip_input = data.get_one_of_inputs('ip')
        system_radio = data.get_one_of_inputs('system')
        path = data.get_one_of_inputs('path')

        script_content = "df %s |awk '{if(+$5>0) print +$5}'" % path
        script_content = base64.b64encode(script_content.encode('utf-8')).decode('utf-8')

        api_kwargs = {
            'bk_biz_id': biz_cc_id,
            'bk_username': executor,
            'bk_app_code': APP_ID,
            'script_content': script_content,
            'account': 'root',
            'script_type': 1,
            'ip_list': [
                {'bk_cloud_id': 0, 'ip': ip_input}
            ]
        }
        resp = client.job.fast_execute_script(**api_kwargs)

        if resp['result']:
            job_id = resp['data']['job_instance_id']
            disk_usaged, _ = self._get_job_log(job_id)
        else:
            return False

        # 处理结果

    def outputs_format(self):
        return []


class DiskCapacityComponent(Component):
    name = u"磁盘容量查询"
    code = 'diskcapacity'
    bound_service = DiskCapacityService
    form = settings.STATIC_URL + 'custom_atom/disk_capacity/dc.js'
