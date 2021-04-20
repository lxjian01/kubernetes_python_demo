from os import path

from kubernetes import client, config, watch

from deployment import Deployment

config.load_kube_config()

v1 = client.CoreV1Api()
print("Listing pods with their IPs:")
ret = v1.list_pod_for_all_namespaces(watch=False)
for i in ret.items:
    print("%s\t%s\t%s" % (i.status.pod_ip, i.metadata.namespace, i.metadata.name))

if __name__ == '__main__':
    yaml_file = "yamls/deployments/nginx-deployment.yaml"
    yaml_file_path = path.join(path.dirname(__file__), yaml_file)
    deployment = Deployment("nginx-deployment","default",yaml_file_path)
    deployment.patch()


