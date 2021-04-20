from kubernetes import client


class Pod():
    def __init__(self):
        self.k8s_apps_v1 = client.CoreV1Api()

    def get_pods(self):
        print("Listing pods with their IPs:")
        ret = self.k8s_apps_v1.list_pod_for_all_namespaces(watch=False)
        for i in ret.items:
            print("%s\t%s\t%s" % (i.status.pod_ip, i.metadata.namespace, i.metadata.name))