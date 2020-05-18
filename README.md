# Ardensi App Backend

## Development Environment Setup

### Setup virtual environment
- In the ardensi-backend root directory, execute `python3 -m venv .venv` to create a python 3 virtual environment.
- Activate the virtual environment with  `source .venv/bin/activate`
- Install dependencies with `pip3 install -r requirements.txt`

### Install the [Google Cloud SDK](https://cloud.google.com/sdk/docs/quickstarts)
- Login using the Ardensi Team credentials (get from team member)
- Select `ardensi-api` as the project

## Run Development Environment

### Make Commands
- Use `make run` while in virtual environment to start ardensi backend locally
- Use `make clean` while in virtual environment to clean up dependencies
- Use `make deploy` to build and push service to gcloud server

## Deployment
- Add dependencies to server library with `pip install -t lib -r requirements.txt`
- To push to gcloud, execute in terminal: `gcloud app deploy --project divine-cortex-277508` where divine-cortex-277508 is the projectID
- View live logs in terminal with `gcloud app logs tail -s default` NOTE: has delay
