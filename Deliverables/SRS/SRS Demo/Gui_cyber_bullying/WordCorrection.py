import http.client, urllib.parse, json
class WordCorrection:
    def Correction(self , Text):
        data = {'text': Text}
        # NOTE: Replace this example key with a valid subscription key.
        key = 'eea5277cc5f943bc8c96d3dc439cc48e'

        host = 'api.cognitive.microsoft.com'
        path = '/bing/v7.0/spellcheck?'
        params = 'mkt=en-us&mode=proof'

        headers = {'Ocp-Apim-Subscription-Key': key,
        'Content-Type': 'application/x-www-form-urlencoded'}

        # The headers in the following example
        # are optional but should be considered as required:
        #
        # X-MSEdge-ClientIP: 999.999.999.999
        # X-Search-Location: lat: +90.0000000000000;long: 00.0000000000000;re:100.000000000000
        # X-MSEdge-ClientID: <Client ID from Previous Response Goes Here>

        conn = http.client.HTTPSConnection(host)
        body = urllib.parse.urlencode (data)
        conn.request ("POST", path + params, body, headers)
        response = conn.getresponse ()
        output = json.dumps(json.loads(response.read()), indent=4)
        resp_dict = json.loads(output)
        for i in range(len(resp_dict['flaggedTokens'])):
            Text = Text.replace(resp_dict['flaggedTokens'][i]['token'],resp_dict['flaggedTokens'][i]['suggestions'][0]['suggestion'])

        return Text