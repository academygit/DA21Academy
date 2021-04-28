# Copyright 2017 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import logging

from flask import Flask
from flask import request
# from items import Items

from google.cloud import bigquery

app = Flask(__name__)
item_util = Items()

@app.route('/price', methods=['GET'])
def price():
    """Given an item_id returns the price of the item."""
    identifier = request.args.get('item_id')
    if identifier is None:
      return 'No item_id code provided.', 400

    # maybe_price = item_util.get_item_price_new(identifier)
    client = bigquery.Client(project='gce-testailua')
    query = """
    SELECT item_id 
    FROM `gce-testailua.endpoint_test.items` 
    WHERE item_id like '%s';
    """ % (identifier)
    maybe_price = client.query(query)

    if maybe_price is None:
      return 'Price not found : %s' % identifier, 400
    return maybe_price, 200

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
