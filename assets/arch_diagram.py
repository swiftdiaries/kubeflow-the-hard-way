# kubeflow architecture diagram
from diagrams import Cluster, Diagram, Edge
from diagrams.onprem.client import Users
from diagrams.k8s.network import Ingress, Service

with Diagram("Kubeflow Networking Architecture", show=False):
    user = Users("Users")
    with Cluster("API gateway"):
        ingress_gateway = Ingress("Ingress")
        user >> Edge(color="darkgreen") >> ingress_gateway

        ingress_gateway >> [Service("Central Dashboard Virtual Service"),
        Service("Notebooks App Virtual Service")]
