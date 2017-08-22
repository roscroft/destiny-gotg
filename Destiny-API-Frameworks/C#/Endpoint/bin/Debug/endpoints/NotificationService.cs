 ///<summary>
///HTTP Method: POST
///Access: Private

public string UserIsTyping(   ) { 
RestRequest request = new RestRequest($"/Message/UserIsTyping/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: 
///<param name="timeout"></param>
///</summary>

public string GetRealTimeEvents( object timeout ) { 
RestRequest request = new RestRequest($"/Notification/Events/{param1}/{param2}/");
request.AddHeader("X-API-KEY", Apikey);
request.AddParameter("timeout, timeout");
IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: 

public string GetRecentNotificationCount(   ) { 
RestRequest request = new RestRequest($"/Notification/GetCount/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: Private
///<param name="format">Unknown. Default is 0.</param>
///</summary>

public string GetRecentNotifications( object format ) { 
RestRequest request = new RestRequest($"/Notification/GetRecent/");
request.AddHeader("X-API-KEY", Apikey);
request.AddParameter("format, format");
IRestResponse response = client.Execute(request);
return response.Response;
}
