from celery import Celery

cele = Celery('demo')                                # 创建 Celery 实例
cele.config_from_object('chat.celery_config')