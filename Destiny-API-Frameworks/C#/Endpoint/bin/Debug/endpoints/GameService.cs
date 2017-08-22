 ///<summary>
///HTTP Method: POST
///Access: Private

public string UnignoreItem(   ) { 
RestRequest request = new RestRequest($"/Ignore/Unignore/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: 

public string GetPlayerGamesById(   ) { 
RestRequest request = new RestRequest($"/Game/GetPlayerGamesById/{param1}/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
