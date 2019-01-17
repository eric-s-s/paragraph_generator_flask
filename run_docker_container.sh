container_name="paragraph_generator_server"
image_name="paragraph_generator_flask"
port="8080"

docker stop "${container_name}"

docker rm "${container_name}"
docker run -p "${port}":"${port}" --name "${container_name}"  "${image_name}"
