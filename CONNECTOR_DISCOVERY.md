# Clover POS Connector — Discovery

**Vendor:** Clover POS (https://clover.com)  
**API Base URL:** `https://api.clover.com/v3/merchants/{mId}`  
**Authentication:** API Bearer Token / OAuth 2.0

## Архитектура API
- **Ключевые сущности:** мерчанты, заказы (/orders), строки чеков (/line_items), меню и товары (/items, /categories), платежи (/payments)
- **Формат обмена данными:** JSON / HTTPS REST.
- **Обработка ошибок:** Стандартные HTTP-коды (400, 401, 403, 404, 429, 500) с типизацией ответа.
- **Тестовая точка проверки подключения:** `GET /v3/merchants/{mId}`.
