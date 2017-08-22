 ///<summary>
///HTTP Method: GET
///Access: 

public string GetSurvey(   ) { 
RestRequest request = new RestRequest($"/Survey/GetSurvey/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: POST
///Access: Private

public string ApproveFireteamThread(   ) { 
RestRequest request = new RestRequest($"/Forum/Recruit/Approve/{param1}/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: POST
///Access: Private

public string ChangeLockState(   ) { 
RestRequest request = new RestRequest($"/Forum/ChangeLockState/{param1}/{param2}/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: POST
///Access: Private

public string ChangePinState(   ) { 
RestRequest request = new RestRequest($"/Forum/ChangePinState/{param1}/{param2}/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: POST
///Access: Private

public string CreateContentComment(   ) { 
RestRequest request = new RestRequest($"/Forum/CreateContentComment/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: POST
///Access: Private

public string CreatePost(   ) { 
RestRequest request = new RestRequest($"/Forum/CreatePost/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: POST
///Access: Private

public string DeletePost(   ) { 
RestRequest request = new RestRequest($"/Forum/DeletePost/{param1}/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: POST
///Access: Private

public string EditPost(   ) { 
RestRequest request = new RestRequest($"/Forum/EditPost/{param1}/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: 
///<param name="locales"></param>
///</summary>

public string GetCoreTopicsPaged( object locales ) { 
RestRequest request = new RestRequest($"/Forum/GetCoreTopicsPaged/{param1}/{param2}/{param3}/{param4}/");
request.AddHeader("X-API-KEY", Apikey);
request.AddParameter("locales, locales");
IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: 

public string GetForumTagCountEstimate(   ) { 
RestRequest request = new RestRequest($"/Forum/GetForumTagCountEstimate/{param1}/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: 
///<param name="partialtag"></param>
///</summary>

public string GetForumTagSuggestions( object partialtag ) { 
RestRequest request = new RestRequest($"/Forum/GetForumTagSuggestions/");
request.AddHeader("X-API-KEY", Apikey);
request.AddParameter("partialtag, partialtag");
IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: 

public string GetPoll(   ) { 
RestRequest request = new RestRequest($"/Forum/Poll/{param1}/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: 
///<param name="quantity"></param>
///<param name="tagsSinceDate"></param>
///</summary>

public string GetPopularTags( object quantity, object tagsSinceDate ) { 
RestRequest request = new RestRequest($"/Forum/GetPopularTags/");
request.AddHeader("X-API-KEY", Apikey);
request.AddParameter("quantity, quantity");request.AddParameter("tagsSinceDate, tagsSinceDate");
IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: 
///<param name="showbanned"></param>
///</summary>

public string GetPostAndParent( object showbanned ) { 
RestRequest request = new RestRequest($"/Forum/GetPostAndParent/{childPostId}/");
request.AddHeader("X-API-KEY", Apikey);
request.AddParameter("showbanned, showbanned");
IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: 
///<param name="showbanned"></param>
///</summary>

public string GetPostAndParentAwaitingApproval( object showbanned ) { 
RestRequest request = new RestRequest($"/Forum/GetPostAndParentAwaitingApproval/{childPostId}/");
request.AddHeader("X-API-KEY", Apikey);
request.AddParameter("showbanned, showbanned");
IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: 
///<param name="showbanned"></param>
///</summary>

public string GetPostsThreadedPaged( object showbanned ) { 
RestRequest request = new RestRequest($"/Forum/GetPostsThreadedPaged/{parentPostId}/{page}/{pageSize}/{replySize}/{getParentPost}/{rootThreadMode}/{sortMode}/");
request.AddHeader("X-API-KEY", Apikey);
request.AddParameter("showbanned, showbanned");
IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: 
///<param name="showbanned"></param>
///</summary>

public string GetPostsThreadedPagedFromChild( object showbanned ) { 
RestRequest request = new RestRequest($"/Forum/GetPostsThreadedPagedFromChild/{childPostId}/{page}/{pageSize}/{replySize}/{rootThreadMode}/{sortMode}/");
request.AddHeader("X-API-KEY", Apikey);
request.AddParameter("showbanned, showbanned");
IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: POST
///Access: Private

public string GetRecruitmentThreadSummaries(   ) { 
RestRequest request = new RestRequest($"/Forum/Recruit/Summaries/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: 

public string GetTopicForContent(   ) { 
RestRequest request = new RestRequest($"/Forum/GetTopicForContent/{contentId}/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: Public
///<param name="tagstring">Filter by tags. Comma separated.</param>
///<param name="locales"></param>
///</summary>

public string GetTopicsPaged( object tagstring, object locales ) { 
RestRequest request = new RestRequest($"/Forum/GetTopicsPaged/{page}/{pageSize}/{group}/{sort}/{quickDate}/{categoryFilter}/");
request.AddHeader("X-API-KEY", Apikey);
request.AddParameter("tagstring, tagstring");request.AddParameter("locales, locales");
IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: POST
///Access: Private

public string JoinFireteamThread(   ) { 
RestRequest request = new RestRequest($"/Forum/Recruit/Join/{param1}/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: POST
///Access: Private

public string KickBanFireteamApplicant(   ) { 
RestRequest request = new RestRequest($"/Forum/Recruit/KickBan/{param1}/{param2}/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: POST
///Access: Private

public string LeaveFireteamThread(   ) { 
RestRequest request = new RestRequest($"/Forum/Recruit/Leave/{param1}/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: POST
///Access: Private

public string MarkReplyAsAnswer(   ) { 
RestRequest request = new RestRequest($"/Forum/MarkReplyAsAnswer/{param1}/{param2}/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: POST
///Access: Private

public string ModerateGroupPost(   ) { 
RestRequest request = new RestRequest($"/Forum/Post/{param1}/GroupModerate/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: POST
///Access: Private

public string ModeratePost(   ) { 
RestRequest request = new RestRequest($"/Forum/Post/{param1}/Moderate/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: POST
///Access: Private

public string ModerateTag(   ) { 
RestRequest request = new RestRequest($"/Forum/Tags/{param1}/Moderate/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: POST
///Access: Private

public string PollVote(   ) { 
RestRequest request = new RestRequest($"/Forum/Poll/Vote/{param1}/{param2}/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: POST
///Access: Private

public string RatePost(   ) { 
RestRequest request = new RestRequest($"/Forum/RatePost/{param1}/{param2}/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
