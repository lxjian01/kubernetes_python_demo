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
        self._k8s_apps_v1 = None

    @property
    def k8s_apps_v1(self):
        if self._k8s_apps_v1 is None:
            self._k8s_apps_v1= client.AppsV1Api()
        return self._k8s_apps_v1

    def get_body(self,yaml_file):
        """
        get deploy yaml body
        :param yaml_file:
        :return:
        """
        with open(yaml_file) as f:
            body = yaml.safe_load(f)
            return body

    def create(self):
        print("starting......")
        try:
            resp = self.k8s_apps_v1.create_namespaced_deployment(self.namespace, self.body)
        except Exception as ex:
            raise ex
        print("Deployment created. status='%s'" % resp.metadata.name)

    def patch(self):
        print("starting......")
        try:
            resp = self.k8s_apps_v1.patch_namespaced_deployment(self.deployment, self.namespace, self.body)
        except Exception as ex:
            raise ex
        print("Deployment patch. status='%s'" % resp.metadata.name)

    def delete(self):
        print("starting......")
        try:
            resp = self.k8s_apps_v1.delete_namespaced_deployment(self.deployment,self.namespace)
        except Exception as ex:
            raise ex
        print("Deployment delete. status='%s'" % resp.metadata.name)