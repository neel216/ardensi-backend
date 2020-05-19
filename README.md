# Ardensi App Backend

## Development Environment Setup

Development environment intended for Unix/Linux/Ubuntu operating systems

### Setup virtual environment
- In the ardensi-backend root directory, execute `python3 -m venv .venv` to create a python3 virtual environment
- Activate the virtual environment with  `source .venv/bin/activate`

### Install the [Google Cloud SDK](https://cloud.google.com/sdk/docs/quickstarts)
- Login with your Google Account credentials and make sure you're an editor on the ardensi-api gcloud project
- Select `divine-cortex-277508` as the project

## Run Development Environment

Enter the virtual environment with  `source .venv/bin/activate`

### Make Commands
- Use `make clean` while in virtual environment to install/clean up dependencies
- Use `make run` while in virtual environment to start backend locally

To deploy:
- Use `make deploy` to build and push service to gcloud server

## Deployment
Use `make deploy` to push build to gcloud server, or:
- Execute `gcloud beta app deploy --project divine-cortex-277508` in terminal

View live logs in terminal with `gcloud app logs tail -s default` NOTE: has delay
