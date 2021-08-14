from dagster import repository, pipeline, solid

@solid
def hello():
    return "hello"

@solid
def world():
    return "world"

@pipeline(name="hello_world_pipeline")
def hello_world_pipeline():
    hello()
    world()


@repository(name="hello_world_repo")
def hello_world_repo():
	return [hello_world_pipeline]
