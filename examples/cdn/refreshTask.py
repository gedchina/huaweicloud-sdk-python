# -*- coding:utf-8 -*-
# Copyright 2018 Huawei Technologies Co.,Ltd.
# 
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use
# this file except in compliance with the License.  You may obtain a copy of the
# License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software distributed
# under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR
# CONDITIONS OF ANY KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations under the License.

import os
import sys
from openstack import connection

os.environ.setdefault('OS_CDN_ENDPOINT_OVERRIDE', 'https://cdn.myhwclouds.com/v1.0')

username = "xxxxxxxxxxx"
password = "xxxxxxxxxxx"
projectId = "xxxxxxxxxxx"
userDomainId = "xxxxxxxxxxx"
auth_url = "https://iam.cn-north-1.myhuaweicloud.com/v3"

conn = connection.Connection(
    auth_url=auth_url,
    user_domain_id=userDomainId,
    project_id=projectId,
    username=username,
    password=password
)

def refreshTask(refreshTask):
    print("refresh files or dirs:")
    refreshtask = conn.cdn.create_refresh_task(**refreshTask)
    print(refreshtask)



if __name__ == "__main__":
    refreshFileTask={
        "type": "file",
        "urls": ["http://cdn-python-sdk.example.com/img/a5.jpg",
                 "http://cdn-python-sdk.example.com/img/a7.jpg"]
    }
    refreshDirTask={
        "type": "directory",
        "urls": ["http://cdn-python-sdk.example.com/img/",
                "http://cdn-python-sdk.example.com/js/plugins/"]
    }
    refreshTask(refreshFileTask)
    refreshTask(refreshDirTask)

