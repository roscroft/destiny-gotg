 ///<summary>
///HTTP Method: POST
///Access: Private

public string UnmarkReplyAsAnswer(   ) { 
RestRequest request = new RestRequest($"/Forum/UnmarkReplyAsAnswer/{param1}/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: POST
///Access: Private
///<param name="tag"></param>
///</summary>

public string FollowTag( object tag ) { 
RestRequest request = new RestRequest($"/Activity/Tag/Follow/");
request.AddHeader("X-API-KEY", Apikey);
request.AddParameter("tag, tag");
IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: POST
///Access: Private

public string FollowUser(   ) { 
RestRequest request = new RestRequest($"/Activity/User/{param1}/Follow/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: 
///<param name="currentpage">The current page to return. Starts at 1.</param>
///<param name="format"></param>
///</summary>

public string GetApplicationActivityForUser( object currentpage, object format ) { 
RestRequest request = new RestRequest($"/Activity/User/{param1}/Activities/Application/{param2}/");
request.AddHeader("X-API-KEY", Apikey);
request.AddParameter("currentpage, currentpage");request.AddParameter("format, format");
IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: 

public string GetEntitiesFollowedByCurrentUser(   ) { 
RestRequest request = new RestRequest($"/Activity/Following/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: 

public string GetEntitiesFollowedByCurrentUserV2(   ) { 
RestRequest request = new RestRequest($"/Activity/Following/V2/{param1}/{param2}/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: 

public string GetEntitiesFollowedByUser(   ) { 
RestRequest request = new RestRequest($"/Activity/User/{param1}/Following/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: 

public string GetEntitiesFollowedByUserV2(   ) { 
RestRequest request = new RestRequest($"/Activity/User/{param1}/Following/V2/{param2}/{param3}/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: 
///<param name="tag"></param>
///<param name="itemsperpage"></param>
///<param name="currentpage">The current page to return. Starts at 1.</param>
///</summary>

public string GetFollowersOfTag( object tag, object itemsperpage, object currentpage ) { 
RestRequest request = new RestRequest($"/Activity/Tag/Followers/");
request.AddHeader("X-API-KEY", Apikey);
request.AddParameter("tag, tag");request.AddParameter("itemsperpage, itemsperpage");request.AddParameter("currentpage, currentpage");
IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: Public
///<param name="itemsperpage">The number of items per page. Default is 50.</param>
///<param name="currentpage">The current page to return. Starts at 1.</param>
///</summary>

public string GetFollowersOfUser( object itemsperpage, object currentpage ) { 
RestRequest request = new RestRequest($"/Activity/User/{profileId}/Followers/");
request.AddHeader("X-API-KEY", Apikey);
request.AddParameter("itemsperpage, itemsperpage");request.AddParameter("currentpage, currentpage");
IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: 
///<param name="itemsperpage"></param>
///<param name="currentpage">The current page to return. Starts at 1.</param>
///<param name="format"></param>
///</summary>

public string GetForumActivityForUser( object itemsperpage, object currentpage, object format ) { 
RestRequest request = new RestRequest($"/Activity/User/{param1}/Activities/Forums/");
request.AddHeader("X-API-KEY", Apikey);
request.AddParameter("itemsperpage, itemsperpage");request.AddParameter("currentpage, currentpage");request.AddParameter("format, format");
IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: 
///<param name="currentpage">The current page to return. Starts at 1.</param>
///<param name="format"></param>
///</summary>

public string GetForumActivityForUserV2( object currentpage, object format ) { 
RestRequest request = new RestRequest($"/Activity/User/{param1}/Activities/ForumsV2/");
request.AddHeader("X-API-KEY", Apikey);
request.AddParameter("currentpage, currentpage");request.AddParameter("format, format");
IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: Public

public string GetFriends(   ) { 
RestRequest request = new RestRequest($"/Activity/Friends/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: 

public string GetFriendsAllNoPresence(   ) { 
RestRequest request = new RestRequest($"/Activity/Friends/AllNoPresence/{param1}/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: Private

public string GetFriendsPaged(   ) { 
RestRequest request = new RestRequest($"/Activity/Friends/Paged/{membershipType}/{currentPage}/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: 

public string GetGroupsFollowedByCurrentUser(   ) { 
RestRequest request = new RestRequest($"/Activity/Following/Groups/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: 

public string GetGroupsFollowedByUser(   ) { 
RestRequest request = new RestRequest($"/Activity/User/{param1}/Following/Groups/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: 

public string GetGroupsFollowedPagedByCurrentUser(   ) { 
RestRequest request = new RestRequest($"/Activity/Following/Groups/{param1}/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: 

public string GetGroupsFollowedPagedByUser(   ) { 
RestRequest request = new RestRequest($"/Activity/User/{param1}/Following/Groups/Paged/{param2}/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: 
///<param name="itemsperpage"></param>
///<param name="currentpage">The current page to return. Starts at 1.</param>
///<param name="format"></param>
///</summary>

public string GetLikeAndShareActivityForUser( object itemsperpage, object currentpage, object format ) { 
RestRequest request = new RestRequest($"/Activity/User/{param1}/Activities/LikesAndShares/");
request.AddHeader("X-API-KEY", Apikey);
request.AddParameter("itemsperpage, itemsperpage");request.AddParameter("currentpage, currentpage");request.AddParameter("format, format");
IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: 
///<param name="currentpage">The current page to return. Starts at 1.</param>
///<param name="format"></param>
///</summary>

public string GetLikeAndShareActivityForUserV2( object currentpage, object format ) { 
RestRequest request = new RestRequest($"/Activity/User/{param1}/Activities/LikesAndSharesV2/");
request.AddHeader("X-API-KEY", Apikey);
request.AddParameter("currentpage, currentpage");request.AddParameter("format, format");
IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: 
///<param name="currentpage">The current page to return. Starts at 1.</param>
///<param name="format"></param>
///</summary>

public string GetLikeShareAndForumActivityForUser( object currentpage, object format ) { 
RestRequest request = new RestRequest($"/Activity/User/{param1}/Activities/LikeShareAndForum/");
request.AddHeader("X-API-KEY", Apikey);
request.AddParameter("currentpage, currentpage");request.AddParameter("format, format");
IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: 

public string GetUsersFollowedByCurrentUser(   ) { 
RestRequest request = new RestRequest($"/Activity/Following/Users/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: POST
///Access: Private
///<param name="tag">A hashtag.</param>
///</summary>

public string UnfollowTag( object tag ) { 
RestRequest request = new RestRequest($"/Activity/Tag/Unfollow/");
request.AddHeader("X-API-KEY", Apikey);
request.AddParameter("tag, tag");
IRestResponse response = client.Execute(request);
return response.Response;
}
