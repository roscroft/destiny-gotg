 ///<summary>
///HTTP Method: POST
///Access: Private

public string UnfollowGroupWithGroup(   ) { 
RestRequest request = new RestRequest($"/Group/{groupId}/Unfollow/{followGroupId}/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: POST
///Access: Private

public string FlagItem(   ) { 
RestRequest request = new RestRequest($"/Ignore/Flag/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: POST
///Access: Private

public string GetIgnoresForUser(   ) { 
RestRequest request = new RestRequest($"/Ignore/MyIgnores/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: 

public string GetIgnoreStatusForPost(   ) { 
RestRequest request = new RestRequest($"/Ignore/MyIgnores/Posts/{param1}/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: 

public string GetIgnoreStatusForUser(   ) { 
RestRequest request = new RestRequest($"/Ignore/MyIgnores/Users/{param1}/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: 

public string GetReportContext(   ) { 
RestRequest request = new RestRequest($"/Ignore/ReportContext/{param1}/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: POST
///Access: Private

public string IgnoreItem(   ) { 
RestRequest request = new RestRequest($"/Ignore/Ignore/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: 

public string MyLastReport(   ) { 
RestRequest request = new RestRequest($"/Ignore/MyLastReport/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
