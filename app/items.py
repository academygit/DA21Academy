from google.cloud import bigquery

class Items(object):
  """An interface for reading data about items."""

  def get_item_price(id):
      client = bigquery.Client(project='gce-testailua')
      query = "select item_id from `gce-testailua.endpoint_test.items` where item_id=%s;" % (id)
      dataset = client.dataset('endpoint_test')
      table = dataset.table(name='items')
      job = client.run_async_query('my-job', query)
      job.destination = table
      job.write_disposition= 'WRITE_TRUNCATE'
      response = job.begin()
      return response

  def get_item_price_new(identifier):
      client = bigquery.Client(project='gce-testailua')
      query = """
      SELECT item_id 
      FROM `gce-testailua.endpoint_test.items` 
      WHERE item_id like '%s';
      """ % (identifier)
      query_job = client.query(query)
      return query_job