from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults
from airflow.exceptions import AirflowException

from telegram_plugin.hooks.telegram_hook import TelegramHook


class TelegramOperator(BaseOperator):
    """
    Telegram Operator

    :param telegram_conn_id:           Telegram connection id.
    :type telegram_conn_id:            string
    :param text:           The message to sent.
    :type text:           string
    """

    template_fields = ('text',)

    @apply_defaults
    def __init__(self,
                 telegram_conn_id,
                 text,
                 parse_mode='HTML',
                 *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.telegram_conn_id = telegram_conn_id
        self.text = text
        self.parse_mode = parse_mode

    def execute(self, **kwargs):
        hook = TelegramHook(telegram_conn_id=self.telegram_conn_id)
        hook.send(self.text, self.parse_mode)