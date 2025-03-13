from harbor.config import auth
from harbor.harbor_model import HarborAPIClient,ListProject,CheckHealth

if __name__ == '__main__':
    harbor_auth = auth.HARBOR_BASIC_AUTH

    # 列出项目
    project_list = ListProject(auth=harbor_auth)
    projects = project_list.list_project()
    if projects:
        print("Projects:")
        for project in projects:
            print(project)
    else:
        print("Failed to retrieve projects.")

    # 检查健康状态
    health_check = CheckHealth(auth=harbor_auth)
    components = health_check.check_health()
    if components:
        print("Health Components:")
        for component in components:
            print(component)
    else:
        print("Failed to retrieve health components.")

    print(f"Ping result: {health_check.ping()}")