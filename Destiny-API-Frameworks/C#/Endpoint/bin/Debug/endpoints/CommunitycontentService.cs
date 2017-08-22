 ///<summary>
///HTTP Method: POST
///Access: Private

public string TransferItem(   ) { 
RestRequest request = new RestRequest($"/Destiny/TransferItem/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: POST
///Access: Private

public string AdminSetCommunityLiveMemberBanStatus(   ) { 
RestRequest request = new RestRequest($"/CommunityContent/Live/Partnerships/{param1}/{param2}/Ban/{param3}/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: POST
///Access: Private

public string AdminSetCommunityLiveMemberFeatureStatus(   ) { 
RestRequest request = new RestRequest($"/CommunityContent/Live/Partnerships/{param1}/{param2}/Feature/{param3}/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: POST
///Access: Private

public string AlterApprovalState(   ) { 
RestRequest request = new RestRequest($"/CommunityContent/AlterApprovalState/{param1}/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: POST
///Access: Private

public string EditContent(   ) { 
RestRequest request = new RestRequest($"/CommunityContent/Edit/{param1}/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: 
///<param name="name"></param>
///</summary>

public string GetAdminCommunityLiveStatuses( object name ) { 
RestRequest request = new RestRequest($"/CommunityContent/Live/Admin/{param1}/{param2}/{param3}/");
request.AddHeader("X-API-KEY", Apikey);
request.AddParameter("name, name");
IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: 

public string GetApprovalQueue(   ) { 
RestRequest request = new RestRequest($"/CommunityContent/Queue/{param1}/{param2}/{param3}/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: 

public string GetCommunityContent(   ) { 
RestRequest request = new RestRequest($"/CommunityContent/Get/{param1}/{param2}/{param3}/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: 

public string GetCommunityFeaturedActivityModes(   ) { 
RestRequest request = new RestRequest($"/CommunityContent/Live/ActivityModes/Featured/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: 
///<param name="modeHash">Filter by ActivityModeType.</param>
///<param name="streamLocale"></param>
///</summary>

public string GetCommunityLiveStatuses( object modeHash, object streamLocale ) { 
RestRequest request = new RestRequest($"/CommunityContent/Live/All/{partnershipType}/{communityStatusSort}/{page}/");
request.AddHeader("X-API-KEY", Apikey);
request.AddParameter("modeHash, modeHash");request.AddParameter("streamLocale, streamLocale");
IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: 

public string GetCommunityLiveStatusesForClanmates(   ) { 
RestRequest request = new RestRequest($"/CommunityContent/Live/Clan/{partnershipType}/{communityStatusSort}/{page}/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: 

public string GetCommunityLiveStatusesForFriends(   ) { 
RestRequest request = new RestRequest($"/CommunityContent/Live/Friends/{partnershipType}/{communityStatusSort}/{page}/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: 
///<param name="streamLocale"></param>
///</summary>

public string GetFeaturedCommunityLiveStatuses( object streamLocale ) { 
RestRequest request = new RestRequest($"/CommunityContent/Live/Featured/{partnershipType}/{communityStatusSort}/{page}/");
request.AddHeader("X-API-KEY", Apikey);
request.AddParameter("streamLocale, streamLocale");
IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: 

public string GetStreamingStatusForMember(   ) { 
RestRequest request = new RestRequest($"/CommunityContent/Live/Users/{partnershipType}/{membershipType}/{membershipId}/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
