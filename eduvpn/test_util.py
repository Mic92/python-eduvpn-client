class MockSelection:
    def __init__(self, num_fields):
        self.model = [['test'] * num_fields]
        self.treeiter = 0

    def get_selected(self):
        return self.model, self.treeiter

    def clear(self):
        return


class MochResponse:
    content_json = {
        "create_keypair": {"data": {"certificate": "mockcert", "private_key": "mockkey"}},
        "profile_list": {"data": {}},
        "user_info": {'data': {'is_disabled': False, 'two_factor_enrolled': False}},
        "authorization_type": "test",
        "instances": [],
    }

    status_code = 200

    @property
    def content(self):
        return str(self.content_json)

    def json(self):
        return self.content_json

    def text(self):
        return str(self.content_json)


class MockOAuth:
    def __init__(self, response=MochResponse()):
        self.response = response

    def get(self, url):
        return self.response

    def authorization_url(self, auth_endpoint, code_challenge_method, code_challenge):
        url = "https://mock url"
        state = "mock state"
        return url, state

    def post(self, url, data):
        return MochResponse()


class VerifyMock:
    def verify(self, *args, **kwargs):
        return True