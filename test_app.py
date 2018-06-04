from app import App


class TestApp:
    app = App()

    def test_get_user_query(self):
        user_query = self.app.get_user_query()
        assert user_query
