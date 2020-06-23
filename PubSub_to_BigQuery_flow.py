import argparse
import logging

import apache_beam as beam
import json

table_spec = 'valiant-nucleus-162210:music_events.music_events'

def parse_pubsub(line):
    return json.loads(line)

def run(argv=None):
  """Build and run the pipeline."""

  parser = argparse.ArgumentParser()
  parser.add_argument(
      '--input_topic', dest='input_topic', required=True,
      help='Input PubSub topic of the form "/topics/<PROJECT>/<TOPIC>".')
  known_args, pipeline_args = parser.parse_known_args(argv)

  with beam.Pipeline(argv=pipeline_args) as p:
    # Read from PubSub
    lines = p | beam.io.ReadFromPubSub(known_args.input_topic)
    #Adapt messages from PubSub to BQ table
    lines = lines | beam.Map(parse_pubsub)
    #Write to a BQ table 
    lines | beam.io.WriteToBigQuery(table_spec)

if __name__ == '__main__':
  logging.getLogger().setLevel(logging.INFO)
  run()