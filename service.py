from kubernetes import client


class Service():
    def __init__(self):
        self.k8s_core_v1 = client.CoreV1Api()

    def create_namespaced_service(self, namespace, body):
        """
        create service
        :param namespace:
        :param body:
        :return:
        """
        print("starting......")
        try:
            resp = self.k8s_core_v1.create_namespaced_service(namespace, body)
        except Exception as ex:
            raise ex
        print("Service created. status='%s'" % resp.metadata.name)
