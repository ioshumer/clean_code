request - make_request # реализация http-запроса в классе
app - create_application # функция создания объекта приложения FastAPI с назначенными маршрутами и определёнными middleware
producer - run_producer # запуск в фоне поставщика задач
processor - run_processor # запуск в фоне обработкичка задач
was_long_time_without_errors - is_stable_perios # метод проверки на наличие ошибок за период времени
access_token_expired - notify_token_expiration # метод уведомления об окончании времени жизни Access Token
status - set_state # функция установки состояния объекта класса
register_and_enable_account - register_account, enable_account # разделение логики по зонам ответственности
coroutine_fabric - generate_coroutine # фабрика для генерации корутин
task - process_task # метод обработки входящих задач
endpoint_request_execute - call_api # вызов endpoin'а внешнего сервиса
periodic_fetch - run_background_tasks # набор асинхронных периодических задач