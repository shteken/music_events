sudo pip3 install pandas

cd music_events/

python3 generating_events.py



sudo pip3 install apache_beam[gcp]

cd music_events/

mv ../PubSub_to_BigQuery_flow.py .

gcloud config set compute/region europe-west3

python3 PubSub_to_BigQuery_flow.py --runner DataflowRunner --input_topic=projects/valiant-nucleus-162210/
topics/music_events --project valiant-nucleus-162210 --temp_location gs://music_events/tmp --staging_location gs://music_events/staging --streaming