# macinfo


# Get MAC Address Company Name

Find company name associated with a MAC Address

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to run this.

### Prerequisites

Signup and get your API-KEY from https://macaddress.io/api

Docker must be installed to run the code inside docker, or python to run it locally

### Installing

Clone the project, then build the docker image using following command:

```
docker build --tag=macinfo .
```

then run it using:

```
docker run  -e API_KEY=[API-KEY]  --rm -it macinfo  --mac  00:A0:C9:14:C8:29
```

