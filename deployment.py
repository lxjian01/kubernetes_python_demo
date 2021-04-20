from os import path

import yaml
from kubernetes import client, config, watch

class Deployment():

    def __init__(self,deployment,namespace,yaml_file):
        """

        :param deployment: nginx-deployment
        :param namespace: default
        :param yaml_file: yamls/deployments/nginx-deployment.yaml
        """
        self.deployment = deployment
        self.namespace = namespace
        self.body = self.get_body(yaml_file)

    def get_body(self,yaml_file):
        """
        get deploy yaml body
        :param yaml_file:
        :return:
        """
        with open(yaml_file) as f:
            body = yaml.safe_load(f)
            return body

    def patch(self):
        print("starting......")
        k8s_apps_v1 = client.AppsV1Api()
        resp = k8s_apps_v1.patch_namespaced_deployment(self.deployment,self.namespace,self.body)
        print("Deployment created. status='%s'" % resp.metadata.name)

    def create(self):
        print("starting......")
        k8s_apps_v1 = client.AppsV1Api()
        resp = k8s_apps_v1.patch_namespaced_deployment(self.deployment, self.namespace, self.body)
        print("Deployment created. status='%s'" % resp.metadata.name)