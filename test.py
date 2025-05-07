import json
import requests
import os
import re
import time
from biz.utils.log import logger


class WaveNotifier:
    def __init__(self, webhook_url=None):
        self.webhook_url = webhook_url or "http://deepseek_bot:8888/callback"

    def send_message(self, content, msg_type='text', title=None, is_at_all=False, project_name=None, url_slug=None):
        try:
            # 构建新的请求格式
            wave_data = {
                "schema": "2.0",
                "header": {
                    "event_type": "custom.task.event",
                    "event_id": f"event_{int(time.time())}",
                    "create_time": str(int(time.time()))
                },
                "event": {
                    "task_id": f"task_{int(time.time())}",
                    "content": content,
                    "timestamp": str(int(time.time()))
                }
            }
            
            # 发送请求
            response = requests.post(
                self.webhook_url,
                json=wave_data,
                headers={'Content-Type': 'application/json'}
            )
            logger.info(f"wave_data: {wave_data}")
            
            if response.status_code == 200:
                logger.info(f"消息发送成功: {content}")
            else:
                logger.error(f"消息发送失败: {response.text}")

        except Exception as e:
            logger.error(f"消息发送失败: {str(e)}")

        
