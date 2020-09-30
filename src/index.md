# Introduction

Kubeflow is an ML toolkit built on top of Kubernetes.

This tutorial walks you through using Kubeflow applications the hard way. This guide aims to show and teach the 
underlying Kubernetes APIs. \
Please refer to the [Getting Started Guide](https://www.kubeflow.org/docs/started/getting-started/) for easier installation.

This guide is not meant for production clusters, it's optimized for learning.

## Target Audience

This guide is for people looking to use Kubeflow in production and want to learn how the pieces fit together.

## Cluster Requirements

We will be using [KIND](https://kind.sigs.k8s.io/) to bootstrap clusters and we'll use different clusters for each application and learn it.

Alternatives:

- [Rancher's k3s](https://rancher.com/docs/k3s/latest/en/)