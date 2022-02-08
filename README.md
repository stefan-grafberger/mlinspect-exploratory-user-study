# User Study

## Building and uploading the Docker Container
* Run `docker build . -t mlinspect-tasks` in this directory
* `docker tag mlinspect-tasks stefangrafberger/mlinspect-tasks`
* `docker login`
* `docker push stefangrafberger/mlinspect-tasks`

## Running the Docker Container
* `docker run -t --rm -p 8899:8899 stefangrafberger/mlinspect-tasks`

## Links to the task files
* `http://localhost:8899/notebooks/user_interviews/example-task-with-solution.ipynb`
* `http://localhost:8899/notebooks/user_interviews/task-1.ipynb`
* `http://localhost:8899/notebooks/user_interviews/task-2.ipynb`
