 ///<summary>
///HTTP Method: POST
///Access: Private

public string SubmitContent(   ) { 
RestRequest request = new RestRequest($"/CommunityContent/Submit/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: 

public string GetAvailableLocales(   ) { 
RestRequest request = new RestRequest($"//GetAvailableLocales/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: 

public string GetCommonSettings(   ) { 
RestRequest request = new RestRequest($"//Settings/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: Public
///<param name="includestreaming"></param>
///</summary>

public string GetGlobalAlerts( object includestreaming ) { 
RestRequest request = new RestRequest($"//GlobalAlerts/");
request.AddHeader("X-API-KEY", Apikey);
request.AddParameter("includestreaming, includestreaming");
IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: 

public string GetSystemStatus(   ) { 
RestRequest request = new RestRequest($"//Status/{param1}/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
