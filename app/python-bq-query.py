from google.cloud import bigquery

client = bigquery.Client(project='gce-testailua')
query = "select item_id from `gce-testailua.endpoint_test.items` where item_id=%s;" % (id)
dataset = client.dataset('endpoint_test')
table = dataset.table(name='items')
job = client.run_async_query('my-job', query)
job.destination = table
job.write_disposition= 'WRITE_TRUNCATE'
job.begin()