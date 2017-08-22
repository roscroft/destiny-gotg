 ///<summary>
///HTTP Method: POST
///Access: Private

public string RevokeAuthorization(   ) { 
RestRequest request = new RestRequest($"/App/RevokeAuthorization/{param1}/{param2}/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: POST
///Access: Private

public string CreateUser(   ) { 
RestRequest request = new RestRequest($"/User/CreateUser/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: POST
///Access: Private

public string EditSuccessMessageFlags(   ) { 
RestRequest request = new RestRequest($"/User/MessageFlags/Success/Update/{param1}/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: Private

public string GetAvailableAvatars(   ) { 
RestRequest request = new RestRequest($"/User/GetAvailableAvatars/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: 

public string GetAvailableAvatarsAdmin(   ) { 
RestRequest request = new RestRequest($"/User/GetAvailableAvatarsAdmin/{param1}/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: Public

public string GetAvailableThemes(   ) { 
RestRequest request = new RestRequest($"/User/GetAvailableThemes/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: Public

public string GetBungieAccount(   ) { 
RestRequest request = new RestRequest($"/User/GetBungieAccount/{membershipId}/{membershipType}/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: 

public string GetBungieNetUserById(   ) { 
RestRequest request = new RestRequest($"/User/GetBungieNetUserById/{membershipId}/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: Private

public string GetCountsForCurrentUser(   ) { 
RestRequest request = new RestRequest($"/User/GetCounts/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: 

public string GetCredentialTypesForAccount(   ) { 
RestRequest request = new RestRequest($"/User/GetCredentialTypesForAccount/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: 

public string GetCurrentBungieAccount(   ) { 
RestRequest request = new RestRequest($"/User/GetCurrentBungieAccount/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: 

public string GetCurrentBungieNetUser(   ) { 
RestRequest request = new RestRequest($"/User/GetCurrentBungieNetUser/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: Private

public string GetCurrentUser-(User)(   ) { 
RestRequest request = new RestRequest($"/User/GetBungieNetUser/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: 

public string GetMembershipDataById(   ) { 
RestRequest request = new RestRequest($"/User/GetMembershipsById/{membershipId}/{membershipType}/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: 

public string GetMembershipDataForCurrentUser(   ) { 
RestRequest request = new RestRequest($"/User/GetMembershipsForCurrentUser/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: 

public string GetMobileAppPairings(   ) { 
RestRequest request = new RestRequest($"/User/GetMobileAppPairings/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: 

public string GetMobileAppPairingsUncached(   ) { 
RestRequest request = new RestRequest($"/User/GetMobileAppPairingsUncached/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: 

public string GetNotificationSettings(   ) { 
RestRequest request = new RestRequest($"/User/GetNotificationSettings/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: 

public string GetPartnerships(   ) { 
RestRequest request = new RestRequest($"/User/{membershipId}/Partnerships/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: 

public string GetPlatformApiKeysForUser(   ) { 
RestRequest request = new RestRequest($"/User/GetPlatformApiKeysForUser/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: 

public string GetSignOutUrl(   ) { 
RestRequest request = new RestRequest($"/User/GetSignOutUrl/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: 

public string GetUserAliases(   ) { 
RestRequest request = new RestRequest($"/User/GetUserAliases/{membershipId}/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: 
///<param name="excludebungienet"></param>
///</summary>

public string GetUserMembershipIds( object excludebungienet ) { 
RestRequest request = new RestRequest($"/User/GetMembershipIds/");
request.AddHeader("X-API-KEY", Apikey);
request.AddParameter("excludebungienet, excludebungienet");
IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: POST
///Access: Private

public string LinkOverride(   ) { 
RestRequest request = new RestRequest($"/User/LinkOverride/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: POST
///Access: Private

public string RegisterMobileAppPair(   ) { 
RestRequest request = new RestRequest($"/User/RegisterMobileAppPair/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: POST
///Access: Private

public string RemovePartnership(   ) { 
RestRequest request = new RestRequest($"/User/Partnerships/{param1}/Remove/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: Public
///<param name="q">A valid Bungie.net username</param>
///</summary>

public string SearchUsers( object q ) { 
RestRequest request = new RestRequest($"/User/SearchUsers/");
request.AddHeader("X-API-KEY", Apikey);
request.AddParameter("q, q");
IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: 

public string SearchUsersPaged(   ) { 
RestRequest request = new RestRequest($"/User/SearchUsersPaged/{searchTerm}/{page}/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: 

public string SearchUsersPagedV2(   ) { 
RestRequest request = new RestRequest($"/User/SearchUsersPaged/{searchTerm}/{page}/{param3}/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: POST
///Access: Private

public string SetAcknowledged(   ) { 
RestRequest request = new RestRequest($"/User/Acknowledged/{ackId}/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: POST
///Access: Private

public string UnregisterMobileAppPair(   ) { 
RestRequest request = new RestRequest($"/User/UnregisterMobileAppPair/{param1}/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: POST
///Access: Private

public string UpdateDestinyEmblemAvatar(   ) { 
RestRequest request = new RestRequest($"/User/UpdateDestinyEmblemAvatar/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: POST
///Access: Private

public string UpdateNotificationSetting(   ) { 
RestRequest request = new RestRequest($"/User/Notification/Update/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: POST
///Access: Private

public string UpdateStateInfoForMobileAppPair(   ) { 
RestRequest request = new RestRequest($"/User/UpdateStateInfoForMobileAppPair/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: POST
///Access: Private

public string UpdateUser(   ) { 
RestRequest request = new RestRequest($"/User/UpdateUser/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
