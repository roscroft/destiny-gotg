 ///<summary>
///HTTP Method: POST
///Access: Private

public string UnfollowUser(   ) { 
RestRequest request = new RestRequest($"/Activity/User/{param1}/Unfollow/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: POST
///Access: Private

public string ApproveAllPending(   ) { 
RestRequest request = new RestRequest($"/Group/{groupId}/Members/ApproveAll/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: POST
///Access: Private

public string ApproveGroupMembership(   ) { 
RestRequest request = new RestRequest($"/Group/{groupId}/Members/{membershipId}/Approve/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: POST
///Access: Private

public string ApproveGroupMembershipV2(   ) { 
RestRequest request = new RestRequest($"/Group/{groupId}/Members/{membershipId}/ApproveV2/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: POST
///Access: Private

public string ApprovePendingForList(   ) { 
RestRequest request = new RestRequest($"/Group/{groupId}/Members/ApproveList/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: POST
///Access: Private

public string BanMember(   ) { 
RestRequest request = new RestRequest($"/Group/{groupId}/Members/{membershipId}/Ban/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: POST
///Access: Private

public string BreakAlliance(   ) { 
RestRequest request = new RestRequest($"/Group/{groupId}/Relationship/{allyGroupId}/BreakAlliance/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: POST
///Access: Private

public string BreakAlliances(   ) { 
RestRequest request = new RestRequest($"/Group/{groupId}/BreakAlliances/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: POST
///Access: Private

public string CreateGroup(   ) { 
RestRequest request = new RestRequest($"/Group/Create/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: POST
///Access: Private

public string CreateGroupV2(   ) { 
RestRequest request = new RestRequest($"/Group/Create/V2/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: POST
///Access: Private

public string CreateMinimalGroup(   ) { 
RestRequest request = new RestRequest($"/Group/Create/Minimal/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: POST
///Access: Private

public string DenyAllPending(   ) { 
RestRequest request = new RestRequest($"/Group/{groupId}/Members/DenyAll/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: POST
///Access: Private

public string DenyGroupMembership(   ) { 
RestRequest request = new RestRequest($"/Group/{groupId}/Members/{membershipId}/Deny/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: POST
///Access: Private

public string DenyGroupMembershipV2(   ) { 
RestRequest request = new RestRequest($"/Group/{groupId}/Members/{membershipId}/DenyV2/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: POST
///Access: Private

public string DenyPendingForList(   ) { 
RestRequest request = new RestRequest($"/Group/{groupId}/Members/DenyList/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: POST
///Access: Private

public string DesignateClanFounder(   ) { 
RestRequest request = new RestRequest($"/Group/{param1}/DesignateClanFounder/{param2}/{param3}/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: POST
///Access: Private

public string DisableClanForGroup(   ) { 
RestRequest request = new RestRequest($"/Group/{groupId}/Clans/Disable/{clanMembershipType}/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: POST
///Access: Private

public string DisbandAlliance(   ) { 
RestRequest request = new RestRequest($"/Group/{groupId}/BreakAllAlliances/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: POST
///Access: Private

public string EditGroup(   ) { 
RestRequest request = new RestRequest($"/Group/{groupId}/Edit/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: POST
///Access: Private
///<param name="clanPlatformType">Unknown. Default is 0.</param>
///</summary>

public string EditGroupMembership( object clanPlatformType ) { 
RestRequest request = new RestRequest($"/Group/{groupId}/Members/{membershipId}/SetMembershipType/{groupMembershipType}/");
request.AddHeader("X-API-KEY", Apikey);
request.AddParameter("clanPlatformType, clanPlatformType");
IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: POST
///Access: Private

public string EditGroupV2(   ) { 
RestRequest request = new RestRequest($"/Group/{groupId}/EditV2/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: POST
///Access: Private
///<param name="clanName"></param>
///</summary>

public string EnableClanForGroup( object clanName ) { 
RestRequest request = new RestRequest($"/Group/{groupId}/Clans/Enable/{clanMembershipType}/");
request.AddHeader("X-API-KEY", Apikey);
request.AddParameter("clanName, clanName");
IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: POST
///Access: Private

public string FollowGroupsWithGroup(   ) { 
RestRequest request = new RestRequest($"/Group/{groupId}/FollowList/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: POST
///Access: Private

public string FollowGroupWithGroup(   ) { 
RestRequest request = new RestRequest($"/Group/{groupId}/Follow/{followGroupId}/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: 
///<param name="itemsPerPage"></param>
///<param name="currentPage">The current page to return. Starts at 1.</param>
///</summary>

public string GetAdminsOfGroup( object itemsPerPage, object currentPage ) { 
RestRequest request = new RestRequest($"/Group/{groupId}/Admins/");
request.AddHeader("X-API-KEY", Apikey);
request.AddParameter("itemsPerPage, itemsPerPage");request.AddParameter("currentPage, currentPage");
IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: Public
///<param name="itemsPerPage">Items per page. Default is 10.</param>
///<param name="currentPage">The current page to return. Starts at 1.</param>
///</summary>

public string GetAdminsOfGroupV2( object itemsPerPage, object currentPage ) { 
RestRequest request = new RestRequest($"/Group/{groupId}/AdminsV2/");
request.AddHeader("X-API-KEY", Apikey);
request.AddParameter("itemsPerPage, itemsPerPage");request.AddParameter("currentPage, currentPage");
IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: 

public string GetAllFoundedGroupsForMember(   ) { 
RestRequest request = new RestRequest($"/Group/User/{param1}/Founded/All/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: Private
///<param name="clanonly">true or false. Default false.</param>
///<param name="populatefriends">true or false. Default false.</param>
///</summary>

public string GetAllGroupsForCurrentMember( object clanonly, object populatefriends ) { 
RestRequest request = new RestRequest($"/Group/MyGroups/All/");
request.AddHeader("X-API-KEY", Apikey);
request.AddParameter("clanonly, clanonly");request.AddParameter("populatefriends, populatefriends");
IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: Public
///<param name="clanonly">true or false. Default false.</param>
///<param name="populatefriends">true or false. Default false.</param>
///</summary>

public string GetAllGroupsForMember( object clanonly, object populatefriends ) { 
RestRequest request = new RestRequest($"/Group/User/{membershipId}/All/");
request.AddHeader("X-API-KEY", Apikey);
request.AddParameter("clanonly, clanonly");request.AddParameter("populatefriends, populatefriends");
IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: Public
///<param name="currentpage">The current page to return. Starts at 1.</param>
///<param name="populatefriends"></param>
///</summary>

public string GetAlliedGroups( object currentpage, object populatefriends ) { 
RestRequest request = new RestRequest($"/Group/{groupId}/Allies/");
request.AddHeader("X-API-KEY", Apikey);
request.AddParameter("currentpage, currentpage");request.AddParameter("populatefriends, populatefriends");
IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: 

public string GetAvailableAvatars-(Group)(   ) { 
RestRequest request = new RestRequest($"/Group/GetAvailableAvatars/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: 

public string GetAvailableThemes-(Group)(   ) { 
RestRequest request = new RestRequest($"/Group/GetAvailableThemes/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: 
///<param name="itemsPerPage"></param>
///<param name="currentPage">The current page to return. Starts at 1.</param>
///</summary>

public string GetBannedMembersOfGroup( object itemsPerPage, object currentPage ) { 
RestRequest request = new RestRequest($"/Group/{groupId}/Banned/");
request.AddHeader("X-API-KEY", Apikey);
request.AddParameter("itemsPerPage, itemsPerPage");request.AddParameter("currentPage, currentPage");
IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: Private
///<param name="itemsPerPage">Items per page. Default is 10.</param>
///<param name="currentPage">The current page to return. Starts at 1.</param>
///</summary>

public string GetBannedMembersOfGroupV2( object itemsPerPage, object currentPage ) { 
RestRequest request = new RestRequest($"/Group/{groupId}/BannedV2/");
request.AddHeader("X-API-KEY", Apikey);
request.AddParameter("itemsPerPage, itemsPerPage");request.AddParameter("currentPage, currentPage");
IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: Public

public string GetClanAttributeDefinitions(   ) { 
RestRequest request = new RestRequest($"/Group/GetClanAttributeDefinitions/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: 

public string GetDeletedGroupsForCurrentMember(   ) { 
RestRequest request = new RestRequest($"/Group/MyGroups/Deleted/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: 
///<param name="clanonly"></param>
///<param name="populatefriends"></param>
///</summary>

public string GetFoundedGroupsForMember( object clanonly, object populatefriends ) { 
RestRequest request = new RestRequest($"/Group/User/{membershipId}/Founded/{currentPage}/");
request.AddHeader("X-API-KEY", Apikey);
request.AddParameter("clanonly, clanonly");request.AddParameter("populatefriends, populatefriends");
IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: 
///<param name="populatefriends"></param>
///</summary>

public string GetGroup( object populatefriends ) { 
RestRequest request = new RestRequest($"/Group/{groupId}/");
request.AddHeader("X-API-KEY", Apikey);
request.AddParameter("populatefriends, populatefriends");
IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: 
///<param name="populatefriends"></param>
///</summary>

public string GetGroupByName( object populatefriends ) { 
RestRequest request = new RestRequest($"/Group/Name/{groupName}/");
request.AddHeader("X-API-KEY", Apikey);
request.AddParameter("populatefriends, populatefriends");
IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: 
///<param name="populatefriends"></param>
///</summary>

public string GetGroupsFollowedByGroup( object populatefriends ) { 
RestRequest request = new RestRequest($"/Group/{groupId}/Following/{currentPage}/");
request.AddHeader("X-API-KEY", Apikey);
request.AddParameter("populatefriends, populatefriends");
IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: 
///<param name="populatefriends"></param>
///</summary>

public string GetGroupsFollowingGroup( object populatefriends ) { 
RestRequest request = new RestRequest($"/Group/{groupId}/FollowedBy/{currentPage}/");
request.AddHeader("X-API-KEY", Apikey);
request.AddParameter("populatefriends, populatefriends");
IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: 
///<param name="partialtag"></param>
///</summary>

public string GetGroupTagSuggestions( object partialtag ) { 
RestRequest request = new RestRequest($"/Group/GetGroupTagSuggestions/");
request.AddHeader("X-API-KEY", Apikey);
request.AddParameter("partialtag, partialtag");
IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: 
///<param name="clanonly"></param>
///<param name="populatefriends"></param>
///</summary>

public string GetJoinedGroupsForCurrentMember( object clanonly, object populatefriends ) { 
RestRequest request = new RestRequest($"/Group/MyGroups/");
request.AddHeader("X-API-KEY", Apikey);
request.AddParameter("clanonly, clanonly");request.AddParameter("populatefriends, populatefriends");
IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: 
///<param name="clanonly"></param>
///<param name="populatefriends"></param>
///</summary>

public string GetJoinedGroupsForCurrentMemberV2( object clanonly, object populatefriends ) { 
RestRequest request = new RestRequest($"/Group/MyGroups/V2/{currentPage}/");
request.AddHeader("X-API-KEY", Apikey);
request.AddParameter("clanonly, clanonly");request.AddParameter("populatefriends, populatefriends");
IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: 
///<param name="clanonly"></param>
///<param name="populatefriends"></param>
///</summary>

public string GetJoinedGroupsForMember( object clanonly, object populatefriends ) { 
RestRequest request = new RestRequest($"/Group/User/{membershipId}/");
request.AddHeader("X-API-KEY", Apikey);
request.AddParameter("clanonly, clanonly");request.AddParameter("populatefriends, populatefriends");
IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: 
///<param name="clanonly"></param>
///<param name="populatefriends"></param>
///</summary>

public string GetJoinedGroupsForMemberV2( object clanonly, object populatefriends ) { 
RestRequest request = new RestRequest($"/Group/User/{membershipId}/Joined/{currentPage}/");
request.AddHeader("X-API-KEY", Apikey);
request.AddParameter("clanonly, clanonly");request.AddParameter("populatefriends, populatefriends");
IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: Public
///<param name="populatefriends">true or false</param>
///</summary>

public string GetJoinedGroupsForMemberV3( object populatefriends ) { 
RestRequest request = new RestRequest($"/Group/User/{membershipId}/JoinedV3/{currentPage}/");
request.AddHeader("X-API-KEY", Apikey);
request.AddParameter("populatefriends, populatefriends");
IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: Public
///<param name="currentPage">The current page to return. Starts at 1.</param>
///<param name="memberType">Default is -1. -1=All Members, 0=Member, 1=Admin, 2=Founder</param>
///<param name="sort">Default is 0.</param>
///<param name="platformType">A valid clan membership type. Default is 0. Required. 0=None, 1=Xbox, 2=PSN</param>
///</summary>

public string GetMembersOfClan( object currentPage, object memberType, object sort, object platformType ) { 
RestRequest request = new RestRequest($"/Group/{groupId}/ClanMembers/");
request.AddHeader("X-API-KEY", Apikey);
request.AddParameter("currentPage, currentPage");request.AddParameter("memberType, memberType");request.AddParameter("sort, sort");request.AddParameter("platformType, platformType");
IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: 
///<param name="itemsPerPage"></param>
///<param name="currentPage">The current page to return. Starts at 1.</param>
///<param name="memberType"></param>
///<param name="platformType"></param>
///<param name="sort"></param>
///</summary>

public string GetMembersOfGroup( object itemsPerPage, object currentPage, object memberType, object platformType, object sort ) { 
RestRequest request = new RestRequest($"/Group/{groupId}/Members/");
request.AddHeader("X-API-KEY", Apikey);
request.AddParameter("itemsPerPage, itemsPerPage");request.AddParameter("currentPage, currentPage");request.AddParameter("memberType, memberType");request.AddParameter("platformType, platformType");request.AddParameter("sort, sort");
IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: 
///<param name="itemsPerPage"></param>
///<param name="currentPage">The current page to return. Starts at 1.</param>
///<param name="memberType"></param>
///<param name="platformType"></param>
///<param name="sort"></param>
///</summary>

public string GetMembersOfGroupV2( object itemsPerPage, object currentPage, object memberType, object platformType, object sort ) { 
RestRequest request = new RestRequest($"/Group/{groupId}/MembersV2/");
request.AddHeader("X-API-KEY", Apikey);
request.AddParameter("itemsPerPage, itemsPerPage");request.AddParameter("currentPage, currentPage");request.AddParameter("memberType, memberType");request.AddParameter("platformType, platformType");request.AddParameter("sort, sort");
IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: Public
///<param name="itemsPerPage">Items per page. Default is 10.</param>
///<param name="currentPage">The current page to return. Starts at 1.</param>
///<param name="memberType">Default is -1. -1=All Members, 0=Member, 1=Admin, 2=Founder</param>
///<param name="platformType">A valid clan membership type. Default is 0. 0=None, 1=Xbox, 2=PSN</param>
///<param name="sort">Default is 0.</param>
///<param name="nameSearch">Not working?</param>
///</summary>

public string GetMembersOfGroupV3( object itemsPerPage, object currentPage, object memberType, object platformType, object sort, object nameSearch ) { 
RestRequest request = new RestRequest($"/Group/{groupId}/MembersV3/");
request.AddHeader("X-API-KEY", Apikey);
request.AddParameter("itemsPerPage, itemsPerPage");request.AddParameter("currentPage, currentPage");request.AddParameter("memberType, memberType");request.AddParameter("platformType, platformType");request.AddParameter("sort, sort");request.AddParameter("nameSearch, nameSearch");
IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: 

public string GetMyClanMemberships(   ) { 
RestRequest request = new RestRequest($"/Group/MyClans/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: Private

public string GetPendingClanMemberships(   ) { 
RestRequest request = new RestRequest($"/Group/{groupId}/Clan/{clanMembershipType}/Pending/{currentPage}/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: 
///<param name="populatefriends"></param>
///</summary>

public string GetPendingGroupsForCurrentMember( object populatefriends ) { 
RestRequest request = new RestRequest($"/Group/MyPendingGroups/");
request.AddHeader("X-API-KEY", Apikey);
request.AddParameter("populatefriends, populatefriends");
IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: 
///<param name="populatefriends"></param>
///</summary>

public string GetPendingGroupsForCurrentMemberV2( object populatefriends ) { 
RestRequest request = new RestRequest($"/Group/MyPendingGroups/V2/{currentPage}/");
request.AddHeader("X-API-KEY", Apikey);
request.AddParameter("populatefriends, populatefriends");
IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: 
///<param name="populatefriends"></param>
///</summary>

public string GetPendingGroupsForMember( object populatefriends ) { 
RestRequest request = new RestRequest($"/Group/User/{membershipId}/Pending/");
request.AddHeader("X-API-KEY", Apikey);
request.AddParameter("populatefriends, populatefriends");
IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: 
///<param name="populatefriends"></param>
///</summary>

public string GetPendingGroupsForMemberV2( object populatefriends ) { 
RestRequest request = new RestRequest($"/Group/User/{membershipId}/PendingV2/{currentPage}/");
request.AddHeader("X-API-KEY", Apikey);
request.AddParameter("populatefriends, populatefriends");
IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: 
///<param name="itemsPerPage"></param>
///<param name="currentPage">The current page to return. Starts at 1.</param>
///</summary>

public string GetPendingMemberships( object itemsPerPage, object currentPage ) { 
RestRequest request = new RestRequest($"/Group/{groupId}/Members/Pending/");
request.AddHeader("X-API-KEY", Apikey);
request.AddParameter("itemsPerPage, itemsPerPage");request.AddParameter("currentPage, currentPage");
IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: Private
///<param name="currentPage">The current page to return. Starts at 1.</param>
///</summary>

public string GetPendingMembershipsV2( object currentPage ) { 
RestRequest request = new RestRequest($"/Group/{groupId}/Members/PendingV2/");
request.AddHeader("X-API-KEY", Apikey);
request.AddParameter("currentPage, currentPage");
IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: POST
///Access: Private
///<param name="populatefriends"></param>
///</summary>

public string GetRecommendedGroups( object populatefriends ) { 
RestRequest request = new RestRequest($"/Group/Recommended/");
request.AddHeader("X-API-KEY", Apikey);
request.AddParameter("populatefriends, populatefriends");
IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: POST
///Access: Public
///<param name="populatefriends">true or false.</param>
///</summary>

public string GroupSearch( object populatefriends ) { 
RestRequest request = new RestRequest($"/Group/Search/");
request.AddHeader("X-API-KEY", Apikey);
request.AddParameter("populatefriends, populatefriends");
IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: POST
///Access: Private

public string InviteClanMember(   ) { 
RestRequest request = new RestRequest($"/Group/{groupId}/InviteToClan/{membershipId}/{clanMembershipType}/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: POST
///Access: Private

public string InviteGroupMember(   ) { 
RestRequest request = new RestRequest($"/Group/{groupId}/Invite/{membershipId}/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: POST
///Access: Private

public string InviteManyToJoinAlliance(   ) { 
RestRequest request = new RestRequest($"/Group/{groupId}/Allies/InviteMany/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: POST
///Access: Private

public string InviteToJoinAlliance(   ) { 
RestRequest request = new RestRequest($"/Group/{groupId}/Allies/Invite/{allyGroupId}/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: POST
///Access: Private

public string JoinClanForGroup(   ) { 
RestRequest request = new RestRequest($"/Group/{groupId}/Clans/Join/{clanMembershipType}/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: POST
///Access: Private
///<param name="clanPlatformType">A valid clan membership type. 0=Group, 1=Xbox, 2=PSN</param>
///</summary>

public string KickMember( object clanPlatformType ) { 
RestRequest request = new RestRequest($"/Group/{groupId}/Members/{membershipId}/Kick/");
request.AddHeader("X-API-KEY", Apikey);
request.AddParameter("clanPlatformType, clanPlatformType");
IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: POST
///Access: Private

public string LeaveClanForGroup(   ) { 
RestRequest request = new RestRequest($"/Group/{groupId}/Clans/Leave/{clanMembershipType}/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: POST
///Access: Private

public string OverrideFounderAdmin(   ) { 
RestRequest request = new RestRequest($"/Group/{groupId}/Admin/FounderOverride/{membershipType}/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: POST
///Access: Private

public string RefreshClanSettingsInDestiny(   ) { 
RestRequest request = new RestRequest($"/Group/MyClans/Refresh/{clanMembershipType}/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: POST
///Access: Private
///<param name="populatefriends"></param>
///</summary>

public string RequestGroupMembership( object populatefriends ) { 
RestRequest request = new RestRequest($"/Group/{groupId}/Members/Apply/");
request.AddHeader("X-API-KEY", Apikey);
request.AddParameter("populatefriends, populatefriends");
IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: POST
///Access: Private
///<param name="populatefriends"></param>
///</summary>

public string RequestGroupMembershipV2( object populatefriends ) { 
RestRequest request = new RestRequest($"/Group/{groupId}/Members/ApplyV2/");
request.AddHeader("X-API-KEY", Apikey);
request.AddParameter("populatefriends, populatefriends");
IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: POST
///Access: Private

public string RequestToJoinAlliance(   ) { 
RestRequest request = new RestRequest($"/Group/{groupId}/Allies/RequestToJoin/{allyGroupId}/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: POST
///Access: Private
///<param name="populatefriends"></param>
///</summary>

public string RescindGroupMembership( object populatefriends ) { 
RestRequest request = new RestRequest($"/Group/{groupId}/Members/Rescind/");
request.AddHeader("X-API-KEY", Apikey);
request.AddParameter("populatefriends, populatefriends");
IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: POST
///Access: Private

public string SaveMigrationSelection(   ) { 
RestRequest request = new RestRequest($"/Group/{param1}/MigrationSelection/{param2}/{param3}/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: POST
///Access: Private

public string SetGroupAsAlliance(   ) { 
RestRequest request = new RestRequest($"/Group/{groupId}/SetAsAlliance/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: POST
///Access: Private

public string SetPrivacy(   ) { 
RestRequest request = new RestRequest($"/Group/{groupId}/Privacy/{param2}/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: POST
///Access: Private

public string UnbanMember(   ) { 
RestRequest request = new RestRequest($"/Group/{groupId}/Members/{membershipId}/Unban/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: POST
///Access: Private

public string UndeleteGroup(   ) { 
RestRequest request = new RestRequest($"/Group/{groupId}/Undelete/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: POST
///Access: Private

public string UnfollowAllGroupsWithGroup(   ) { 
RestRequest request = new RestRequest($"/Group/{groupId}/UnfollowAll/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: POST
///Access: Private

public string UnfollowGroupsWithGroup(   ) { 
RestRequest request = new RestRequest($"/Group/{groupId}/UnfollowList/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
