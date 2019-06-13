$(function() {
    $atoms.disk_capacity = [
        {
            tag_code: "eb_ip_input",
            type: "input",
            attrs: {
                name: "IP",
                placeholder: "请输入IP地址",
                hookable: true,
                validation: [
                    {
                        type: "required"
                    }
                ]
            } 
        },
        {
            tag_code: "eb_system_radio",
            type: "radio",
            attrs: {
                name: "系统",
                items: [
                    {value: "1", name: "Linux"},
                    {value: "2", name: "Windows"},
                    {value: "3", name: "MacOS"}
                ],
                default: "1",
                hookable: true,
                validation: {
                    type: "required"
                }
            }
        },
        {
            tag_code: "eb_path_input",
            type: "input",
            attrs: [
                name: "路径",
                placeholder: "文件系统路径",
                hookable: true,
                validation: {
                    type: "required"
                }
            ]
        },
    ]
})();
