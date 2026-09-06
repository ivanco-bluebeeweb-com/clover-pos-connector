# Clover POS Connector — Auth & Credentials Standard

**Compliance:** AUTH_AND_CREDENTIALS_STANDARD.md (B1–B10)

## Схема аутентификации
- **Метод:** API Bearer Token / OAuth 2.0
- **Хранение:** Секреты сохраняются изолированно в хранилище секретов платформы Imperal.
- **Валидация:** При сохранении ключа выполняется тестовый запрос `GET /v3/merchants/{mId}`.
- **Отключение:** Удаление локальных ключей без воздействия на аккаунт вендора.
