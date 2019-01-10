from airflow.plugins_manager import AirflowPlugin

from telegram_plugin.operators.telegram_operator import TelegramOperator
from telegram_plugin.hooks.telegram_hook import TelegramHook

class TelegramPlugin(AirflowPlugin):
    name = "telegram_plugin"
    operators = [TelegramOperator]
    hooks = [TelegramHook]