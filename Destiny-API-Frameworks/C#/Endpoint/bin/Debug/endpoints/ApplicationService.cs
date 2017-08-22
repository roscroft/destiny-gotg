 ///<summary>
///HTTP Method: GET
///Access: Private
///<param name="callback"></param>
///</summary>


public string GetCurrentUser( object callback ) 
 { 
RestRequest request = new RestRequest($"/JSONP/GetBungieNetUser/");
request.AddHeader("X-API-KEY", Apikey);
request.AddParameter("callback, callback");
IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: POST
///Access: Private

public string ApplicationSearch(   ) { 
RestRequest request = new RestRequest($"/App/Search/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: POST
///Access: Private

public string ChangeApiKeyStatus(   ) { 
RestRequest request = new RestRequest($"/App/ChangeApiKeyState/{param1}/{param2}/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: POST
///Access: Private

public string CreateApiKey(   ) { 
RestRequest request = new RestRequest($"/App/CreateApiKey/{param1}/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: POST
///Access: Private

public string CreateApplication(   ) { 
RestRequest request = new RestRequest($"/App/CreateApplication/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: POST
///Access: Private

public string EditApplication(   ) { 
RestRequest request = new RestRequest($"/App/EditApplication/{param1}/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: POST
///Access: Public

public string GetAccessTokensFromCode(   ) { 
RestRequest request = new RestRequest($"/App/GetAccessTokensFromCode/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: POST
///Access: Public

public string GetAccessTokensFromRefreshToken(   ) { 
RestRequest request = new RestRequest($"/App/GetAccessTokensFromRefreshToken/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: 

public string GetApplication(   ) { 
RestRequest request = new RestRequest($"/App/Application/{param1}/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: 

public string GetApplicationApiKeys(   ) { 
RestRequest request = new RestRequest($"/App/ApplicationApiKeys/{param1}/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: 

public string GetAuthorizationForUserAndApplication(   ) { 
RestRequest request = new RestRequest($"/App/Authorization/{param1}/{param2}/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: Private
///<param name="currentPage">The current page to return. Starts at 1.</param>
///</summary>

public string GetAuthorizations( object currentPage ) { 
RestRequest request = new RestRequest($"/App/Authorizations/{param1}/");
request.AddHeader("X-API-KEY", Apikey);
request.AddParameter("currentPage, currentPage");
IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: POST
///Access: Private

public string GetOAuthTokens(   ) { 
RestRequest request = new RestRequest($"/App/oauth/token/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: POST
///Access: Private

public string PrivateApplicationSearch(   ) { 
RestRequest request = new RestRequest($"/App/PrivateSearch/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
