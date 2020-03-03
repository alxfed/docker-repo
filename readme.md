Docker repo

<pre>
mkdir -p /tmp/tfserving
cd /tmp/tfserving
git clone https://github.com/tensorflow/serving
</pre>

then

<pre>
docker run -p 8501:8501 \
  --mount type=bind,\
  source=/tmp/tfserving/serving/tensorflow_serving/servables/tensorflow/testdata/saved_model_half_plus_two_cpu,\
  target=/models/half_plus_two \
  -e MODEL_NAME=half_plus_two -t tensorflow/serving &
</pre>

to query

<pre>
curl -d '{"instances": [1.0, 2.0, 5.0]}' \
  -X POST http://localhost:8501/v1/models/half_plus_two:predict
</pre>