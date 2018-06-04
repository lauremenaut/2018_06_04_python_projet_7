from app import App


class TestApp:
    appl = App()

    def test_get_user_query(self):
        user_query = self.appl.get_user_query()
        assert type(user_query) == str

    def test_cut_user_query(self):
        words = self.appl.cut_user_query(self.appl.user_query)
        assert type(words) == list
