from test import TCBase, check_status_code


class SaveUrlTest(TCBase):

    @check_status_code(201)
    def test_success_save_url(self):
        rv = self.save_url_request()
        self.assertEqual(rv.json['url'], 'http://localhost/b')

        return rv

    @check_status_code(201)
    def test_exist_url(self):
        rv = self.save_url_request()
        url = rv.json['url']
        self.assertEqual(rv.status_code, 201)

        rv2 = self.save_url_request()
        self.assertEqual(rv.json['url'], url)

        return rv2
