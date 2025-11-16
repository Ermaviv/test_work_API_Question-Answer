from http import HTTPStatus


class TestAuthAPI:

    def test_auth(self, client, user, password):
        response = client.get(
            '/api/',
            data={'username': user.username, 'password': password}
        )
        assert response.status_code != HTTPStatus.UNAUTHORIZED, (
            'Страница `/api/v1/api-token-auth/` не найдена, проверьте этот '
            'адрес в *urls.py*.'
        )
        assert response.status_code == HTTPStatus.OK, (
            'Проверьте, что POST-запрос к `/api/v1/api-token-auth/` '
            'возвращает ответ с кодом 200.'
        )
