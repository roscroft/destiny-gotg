 ///<summary>
///HTTP Method: POST
///Access: Private

public string UpdateUserAdmin(   ) { 
RestRequest request = new RestRequest($"/User/UpdateUserAdmin/{param1}/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: POST
///Access: Private

public string CreateConversation(   ) { 
RestRequest request = new RestRequest($"/Message/CreateConversation/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: POST
///Access: Private

public string CreateConversationV2(   ) { 
RestRequest request = new RestRequest($"/Message/CreateConversationV2/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: 

public string GetAllianceInvitedToJoinInvitations(   ) { 
RestRequest request = new RestRequest($"/Message/AllianceInvitations/InvitationsToJoinAnotherGroup/{param1}/{param2}/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: 

public string GetAllianceJoinInvitations(   ) { 
RestRequest request = new RestRequest($"/Message/AllianceInvitations/RequestsToJoinYourGroup/{param1}/{param2}/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: 

public string GetConversationById(   ) { 
RestRequest request = new RestRequest($"/Message/GetConversationById/{conversationId}/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: 
///<param name="format"></param>
///</summary>

public string GetConversationByIdV2( object format ) { 
RestRequest request = new RestRequest($"/Message/GetConversationByIdV2/{param1}/");
request.AddHeader("X-API-KEY", Apikey);
request.AddParameter("format, format");
IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: 

public string GetConversationsV2(   ) { 
RestRequest request = new RestRequest($"/Message/GetConversationsV2/{param1}/{param2}/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: 

public string GetConversationsV3(   ) { 
RestRequest request = new RestRequest($"/Message/GetConversationsV3/{param1}/{param2}/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: 
///<param name="format"></param>
///</summary>

public string GetConversationsV4( object format ) { 
RestRequest request = new RestRequest($"/Message/GetConversationsV4/{param1}/");
request.AddHeader("X-API-KEY", Apikey);
request.AddParameter("format, format");
IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: Private
///<param name="format">Unknown. Default is 0.</param>
///</summary>

public string GetConversationsV5( object format ) { 
RestRequest request = new RestRequest($"/Message/GetConversationsV5/{currentPage}/");
request.AddHeader("X-API-KEY", Apikey);
request.AddParameter("format, format");
IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: 

public string GetConversationThreadV2(   ) { 
RestRequest request = new RestRequest($"/Message/GetConversationThreadV2/{param1}/{param2}/{param3}/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: 
///<param name="format"></param>
///<param name="before"></param>
///<param name="after"></param>
///</summary>

public string GetConversationThreadV3( object format, object before, object after ) { 
RestRequest request = new RestRequest($"/Message/GetConversationThreadV3/{param1}/{param2}/");
request.AddHeader("X-API-KEY", Apikey);
request.AddParameter("format, format");request.AddParameter("before, before");request.AddParameter("after, after");
IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: 

public string GetConversationWithMemberId(   ) { 
RestRequest request = new RestRequest($"/Message/GetConversationWithMember/{memberId}/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: 
///<param name="format"></param>
///</summary>

public string GetConversationWithMemberIdV2( object format ) { 
RestRequest request = new RestRequest($"/Message/GetConversationWithMemberV2/{param1}/");
request.AddHeader("X-API-KEY", Apikey);
request.AddParameter("format, format");
IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: 
///<param name="format"></param>
///</summary>

public string GetGroupConversations( object format ) { 
RestRequest request = new RestRequest($"/Message/GetGroupConversations/{param1}/");
request.AddHeader("X-API-KEY", Apikey);
request.AddParameter("format, format");
IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: 

public string GetInvitationDetails(   ) { 
RestRequest request = new RestRequest($"/Message/Invitations/{param1}/Details/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: 

public string GetTotalConversationCount(   ) { 
RestRequest request = new RestRequest($"/Message/GetTotalConversationCount/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: 

public string GetUnreadConversationCountV2(   ) { 
RestRequest request = new RestRequest($"/Message/GetUnreadPrivateConversationCount/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: 

public string GetUnreadConversationCountV3(   ) { 
RestRequest request = new RestRequest($"/Message/GetUnreadConversationCountV3/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: 

public string GetUnreadConversationCountV4(   ) { 
RestRequest request = new RestRequest($"/Message/GetUnreadConversationCountV4/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: 

public string GetUnreadGroupConversationCount(   ) { 
RestRequest request = new RestRequest($"/Message/GetUnreadGroupConversationCount/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: 

public string LeaveConversation(   ) { 
RestRequest request = new RestRequest($"/Message/LeaveConversation/{param1}/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: POST
///Access: Private

public string ModerateGroupWall(   ) { 
RestRequest request = new RestRequest($"/Message/ModerateGroupWall/{param1}/{param2}/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: POST
///Access: Private

public string ReviewAllInvitations(   ) { 
RestRequest request = new RestRequest($"/Message/Invitations/ReviewAllDirect/{param1}/{param2}/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: POST
///Access: Private

public string ReviewInvitation(   ) { 
RestRequest request = new RestRequest($"/Message/Invitations/{param1}/{param2}/{param3}/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: POST
///Access: Private

public string ReviewInvitationDirect(   ) { 
RestRequest request = new RestRequest($"/Message/Invitations/ReviewDirect/{invitationId}/{invitationResponseState}/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: POST
///Access: Private

public string ReviewInvitations(   ) { 
RestRequest request = new RestRequest($"/Message/Invitations/ReviewListDirect/{param1}/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: POST
///Access: Private

public string SaveMessageV2(   ) { 
RestRequest request = new RestRequest($"/Message/SaveMessageV2/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: POST
///Access: Private

public string SaveMessageV3(   ) { 
RestRequest request = new RestRequest($"/Message/SaveMessageV3/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: POST
///Access: Private

public string SaveMessageV4(   ) { 
RestRequest request = new RestRequest($"/Message/SaveMessageV4/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: POST
///Access: Private

public string UpdateConversationLastViewedTimestamp(   ) { 
RestRequest request = new RestRequest($"/Message/Conversations/UpdateLastViewedTimestamp/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
