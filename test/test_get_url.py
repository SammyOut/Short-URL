from test import TCBase, check_status_code


class GetUrlTest(TCBase):

    def setUp(self):
        super(GetUrlTest, self).setUp()
        self.short_url = self.save_url_request()

    @check_status_code(302)
    def test_success_get_url(self):
        rv = self.get_url_request('b')

        self.assertEqual(rv.headers['location'], 'https://github.com/Nerd-Bear')

        return rv

    @check_status_code(204)
    def test_wrong_key(self):
        return self.get_url_request('Chicken')
