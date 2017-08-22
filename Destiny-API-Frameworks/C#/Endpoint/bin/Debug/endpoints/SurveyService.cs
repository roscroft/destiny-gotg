 ///<summary>
///HTTP Method: GET
///Access: 
///<param name="types"></param>
///</summary>

public string GetAggregatedSocialFeed( object types ) { 
RestRequest request = new RestRequest($"/ExternalSocial/GetAggregatedSocialFeed/{param1}/");
request.AddHeader("X-API-KEY", Apikey);
request.AddParameter("types, types");
IRestResponse response = client.Execute(request);
return response.Response;
}
