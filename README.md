# cvtool_jobs_client
Image ingestion jobs.

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: v1
- Package version: 1.0.0
- Build package: io.swagger.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com//.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com//.git`)

Then import the package:
```python
import cvtool_jobs_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import cvtool_jobs_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import cvtool_jobs_client
from cvtool_jobs_client.rest import ApiException
from pprint import pprint
# create an instance of the API class
api_instance = cvtool_jobs_client.JobApi()
tenant_id = 'tenant_id_example' # str | tenant id
job_id = 'job_id_example' # str | job id
job_step = cvtool_jobs_client.JobStep() # JobStep | job step

try:
    api_instance.add_step(tenant_id, job_id, job_step)
except ApiException as e:
    print("Exception when calling JobApi->add_step: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://kingpick-image-ingestion-jobs-api.endpoints.ciandt-cognitive-sandbox.cloud.goog/v1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*JobApi* | [**add_step**](docs/JobApi.md#add_step) | **POST** /jobs/{job_id}/steps | 
*JobApi* | [**create**](docs/JobApi.md#create) | **POST** /jobs | 
*JobApi* | [**end_job**](docs/JobApi.md#end_job) | **POST** /jobs/{job_id}/end | 
*JobApi* | [**get**](docs/JobApi.md#get) | **GET** /jobs/{job_id} | 
*JobApi* | [**start_job**](docs/JobApi.md#start_job) | **POST** /jobs/{job_id}/start | 


## Documentation For Models

 - [Job](docs/Job.md)
 - [JobInputParameters](docs/JobInputParameters.md)
 - [JobStep](docs/JobStep.md)
 - [NewJobRequest](docs/NewJobRequest.md)


## Documentation For Authorization

 All endpoints do not require authorization.


## Author



