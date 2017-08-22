 ///<summary>
///HTTP Method: POST
///Access: Private

public string ReachModelSneakerNet(   ) { 
RestRequest request = new RestRequest($"/Game/ReachModelSneakerNet/{param1}/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: 
///<param name="q"></param>
///</summary>

public string AdminUserSearch( object q ) { 
RestRequest request = new RestRequest($"/Admin/Member/Search/");
request.AddHeader("X-API-KEY", Apikey);
request.AddParameter("q, q");
IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: POST
///Access: Private

public string BulkEditPost(   ) { 
RestRequest request = new RestRequest($"/Admin/BulkEditPost/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: 
///<param name="membershipFilter"></param>
///<param name="startdate"></param>
///<param name="enddate"></param>
///</summary>

public string GetAdminHistory( object membershipFilter, object startdate, object enddate ) { 
RestRequest request = new RestRequest($"/Admin/GlobalHistory/{param1}/{param2}/");
request.AddHeader("X-API-KEY", Apikey);
request.AddParameter("membershipFilter, membershipFilter");request.AddParameter("startdate, startdate");request.AddParameter("enddate, enddate");
IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: POST
///Access: Private

public string GetAssignedReports(   ) { 
RestRequest request = new RestRequest($"/Admin/Assigned/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: POST
///Access: Private

public string GetDisciplinedReportsForMember(   ) { 
RestRequest request = new RestRequest($"/Admin/Member/{param1}/Reports/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: 

public string GetRecentDisciplineAndFlagHistoryForMember(   ) { 
RestRequest request = new RestRequest($"/Admin/Member/{param1}/RecentIncludingFlags/{param2}");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: POST
///Access: Private

public string GetResolvedReports(   ) { 
RestRequest request = new RestRequest($"/Admin/Reports/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: 

public string GetUserBanState(   ) { 
RestRequest request = new RestRequest($"/Admin/Member/{param1}/GetBanState/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: 

public string GetUserPostHistory(   ) { 
RestRequest request = new RestRequest($"/Admin/Member/{param1}/PostHistory/{param2}/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: 

public string GetUserWebClientIpHistory(   ) { 
RestRequest request = new RestRequest($"/Admin/Member/{param1}/GetWebClientIpHistory/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: POST
///Access: Private

public string GloballyIgnoreItem(   ) { 
RestRequest request = new RestRequest($"/Admin/Ignores/GloballyIgnore/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: POST
///Access: Private

public string OverrideBanOnUser(   ) { 
RestRequest request = new RestRequest($"/Admin/Member/{param1}/SetBan/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: POST
///Access: Private

public string OverrideGlobalIgnore(   ) { 
RestRequest request = new RestRequest($"/Admin/Ignores/OverrideGlobalIgnore/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: POST
///Access: Private

public string OverrideGroupWallBanOnUser(   ) { 
RestRequest request = new RestRequest($"/Admin/Member/{param1}/SetGroupWallBan/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: POST
///Access: Private

public string OverrideMsgBanOnUser(   ) { 
RestRequest request = new RestRequest($"/Admin/Member/{param1}/SetMsgBan/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: POST
///Access: Private

public string OverturnReport(   ) { 
RestRequest request = new RestRequest($"/Admin/Reports/Overturn/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: POST
///Access: Private

public string ResolveReport(   ) { 
RestRequest request = new RestRequest($"/Admin/Assigned/Resolve/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
