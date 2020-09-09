# Introduction

Kubeflow is an ML platform built on top of Kubernetes.

The primary target users are infrastructure engineers and SREs who are already using Kubernetes for their application infrastructure and are starting to build out similar workflows/tooling to boost productivity of data scientists in their organisation.

### Who is Kubeflow for?
- SREs, Infrastructure Engineers using Kubernetes.
- Infrastructure teams building Data Science Productivity Platforms on
  Kubernetes.
- Teams with size more than 30 (you will need a team of 10 engineers to
  maintain the lifecycle of Kubeflow clusters).

### Who is Kubeflow not for?
- Data Scientists with little sysadmin skills.

## Why the gatekeeping?

The value provided by Kubeflow starts showing when the team starts scaling.
So for teams not meeting the criteria a managed services like [Weights and Biases](https://www.wandb.com/) for experiment tracking, [h20.ai](https://www.h2o.ai/products/h2o-driverless-ai/) for a Platform, [Seldon](https://www.seldon.io/tech/products/) for deploying ML models among the startups and on the hyper-scalers AWS (SageMaker), Azure ML or GCP's AI Platform should suffice.
The additional complexity incurred in maintenance of your infrastructure should
not come in the way of your core business logic which is essentially the
proverbial golden goose.

So I would strongly encourage people to try other platforms
and services ***before*** taking a look at Kubeflow.

Kubeflow is enormously complex and has many moving parts. Much like Kubernetes
in it's early stages. With continued efforts hopefully it will someday be as
accessible as Kubernetes. 
