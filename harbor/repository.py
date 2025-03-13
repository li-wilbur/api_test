from harbor import harbor_model
from config import auth
hm = harbor_model.HarborAPIClient
class HarborRepository(hm):
    def __init__(self, auth):
        super().__init__(auth)

    def repositories(self,project=None,repo=None,page=1,page_size=50):
        if repo is not None and project is  None:
            print('repo be dependent on project!')
            return None
        if project:
            if repo:
                url = self.api + '/projects/' + project + '/repositories/' + repo
            else:
                url = self.api + '/projects/' + project + '/repositories?page=' + str(page) + '&page_size=' + str(page_size)
        else:
            url = self.api + '/repositories?page=' + str(page) + '&page_size=' + str(page_size)
        resp = self.make_request(url)
        return resp

if __name__ == '__main__':
    harbor_auth = auth.HARBOR_BASIC_AUTH
    harbor_repo = HarborRepository(auth=harbor_auth)
    for r in harbor_repo.repositories(repo='frp',page_size=10).json():
        print(r)