 ///<summary>
///HTTP Method: POST
///Access: Private

public string VerifyAge(   ) { 
RestRequest request = new RestRequest($"/Tokens/VerifyAge/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: POST
///Access: Private

public string EquipItem(   ) { 
RestRequest request = new RestRequest($"/Destiny/EquipItem/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: POST
///Access: Private

public string EquipItems(   ) { 
RestRequest request = new RestRequest($"/Destiny/EquipItems/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: Public
///<param name="definitions">Include definitions in the response. Use while testing.</param>
///</summary>

public string GetAccount( object definitions ) { 
RestRequest request = new RestRequest($"/Destiny/{membershipType}/Account/{destinyMembershipId}/");
request.AddHeader("X-API-KEY", Apikey);
request.AddParameter("definitions, definitions");
IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: 
///<param name="definitions">Include definitions in the response. Use while testing.</param>
///</summary>

public string GetAccountSummary( object definitions ) { 
RestRequest request = new RestRequest($"/Destiny/{membershipType}/Account/{destinyMembershipId}/Summary/");
request.AddHeader("X-API-KEY", Apikey);
request.AddParameter("definitions, definitions");
IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: 

public string GetActivityBlob(   ) { 
RestRequest request = new RestRequest($"/Destiny/Stats/ActivityBlob/{e}/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: Public
///<param name="mode">Game mode to return. Required.</param>
///<param name="count">The number of results to return.</param>
///<param name="page">The current page to return. Starts at 1.</param>
///<param name="definitions">Include definitions in the response. Use while testing.</param>
///</summary>

public string GetActivityHistory( object mode, object count, object page, object definitions ) { 
RestRequest request = new RestRequest($"/Destiny/Stats/ActivityHistory/{membershipType}/{destinyMembershipId}/{characterId}/");
request.AddHeader("X-API-KEY", Apikey);
request.AddParameter("mode, mode");request.AddParameter("count, count");request.AddParameter("page, page");request.AddParameter("definitions, definitions");
IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: 
///<param name="definitions">Include definitions in the response. Use while testing.</param>
///</summary>

public string GetAdvisorsForAccount( object definitions ) { 
RestRequest request = new RestRequest($"/Destiny/{membershipType}/Account/{destinyMembershipId}/Advisors/");
request.AddHeader("X-API-KEY", Apikey);
request.AddParameter("definitions, definitions");
IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: Public
///<param name="definitions">Include definitions in the response. Use while testing.</param>
///</summary>

public string GetAdvisorsForCharacter( object definitions ) { 
RestRequest request = new RestRequest($"/Destiny/{membershipType}/Account/{destinyMembershipId}/Character/{characterId}/Advisors/");
request.AddHeader("X-API-KEY", Apikey);
request.AddParameter("definitions, definitions");
IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: 
///<param name="definitions">Include definitions in the response. Use while testing.</param>
///</summary>

public string GetAdvisorsForCharacterV2( object definitions ) { 
RestRequest request = new RestRequest($"/Destiny/{membershipType}/Account/{destinyMembershipId}/Character/{characterId}/Advisors/V2/");
request.AddHeader("X-API-KEY", Apikey);
request.AddParameter("definitions, definitions");
IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: Private
///<param name="definitions">Include definitions in the response. Use while testing.</param>
///</summary>

public string GetAdvisorsForCurrentCharacter( object definitions ) { 
RestRequest request = new RestRequest($"/Destiny/{membershipType}/MyAccount/Character/{characterId}/Advisors/");
request.AddHeader("X-API-KEY", Apikey);
request.AddParameter("definitions, definitions");
IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: Public
///<param name="definitions">Include definitions in the response. Use while testing.</param>
///</summary>

public string GetAllItemsSummary( object definitions ) { 
RestRequest request = new RestRequest($"/Destiny/{membershipType}/Account/{destinyMembershipId}/Items/");
request.AddHeader("X-API-KEY", Apikey);
request.AddParameter("definitions, definitions");
IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: 
///<param name="definitions">Include definitions in the response. Use while testing.</param>
///</summary>

public string GetAllVendorsForCurrentCharacter( object definitions ) { 
RestRequest request = new RestRequest($"/Destiny/{membershipType}/MyAccount/Character/{characterId}/Vendors/");
request.AddHeader("X-API-KEY", Apikey);
request.AddParameter("definitions, definitions");
IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: 
///<param name="definitions">Include definitions in the response. Use while testing.</param>
///</summary>

public string GetBondAdvisors( object definitions ) { 
RestRequest request = new RestRequest($"/Destiny/{membershipType}/MyAccount/Advisors/Bonds/");
request.AddHeader("X-API-KEY", Apikey);
request.AddParameter("definitions, definitions");
IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: Private
///<param name="definitions">Include definitions in the response. Use while testing.</param>
///</summary>

public string GetCharacter( object definitions ) { 
RestRequest request = new RestRequest($"/Destiny/{membershipType}/Account/{destinyMembershipId}/Character/{characterId}/Complete/");
request.AddHeader("X-API-KEY", Apikey);
request.AddParameter("definitions, definitions");
IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: Public
///<param name="definitions">Include definitions in the response. Use while testing.</param>
///</summary>

public string GetCharacterActivities( object definitions ) { 
RestRequest request = new RestRequest($"/Destiny/{membershipType}/Account/{destinyMembershipId}/Character/{characterId}/Activities/");
request.AddHeader("X-API-KEY", Apikey);
request.AddParameter("definitions, definitions");
IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: Public
///<param name="definitions">Include definitions in the response. Use while testing.</param>
///</summary>

public string GetCharacterInventory( object definitions ) { 
RestRequest request = new RestRequest($"/Destiny/{membershipType}/Account/{destinyMembershipId}/Character/{characterId}/Inventory/");
request.AddHeader("X-API-KEY", Apikey);
request.AddParameter("definitions, definitions");
IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: 
///<param name="definitions">Include definitions in the response. Use while testing.</param>
///</summary>

public string GetCharacterInventorySummary( object definitions ) { 
RestRequest request = new RestRequest($"/Destiny/{membershipType}/Account/{destinyMembershipId}/Character/{characterId}/Inventory/Summary/");
request.AddHeader("X-API-KEY", Apikey);
request.AddParameter("definitions, definitions");
IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: Public
///<param name="definitions">Include definitions in the response. Use while testing.</param>
///</summary>

public string GetCharacterProgression( object definitions ) { 
RestRequest request = new RestRequest($"/Destiny/{membershipType}/Account/{destinyMembershipId}/Character/{characterId}/Progression/");
request.AddHeader("X-API-KEY", Apikey);
request.AddParameter("definitions, definitions");
IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: Public
///<param name="definitions">Include definitions in the response. Use while testing.</param>
///</summary>

public string GetCharacterSummary( object definitions ) { 
RestRequest request = new RestRequest($"/Destiny/{membershipType}/Account/{destinyMembershipId}/Character/{characterId}/");
request.AddHeader("X-API-KEY", Apikey);
request.AddParameter("definitions, definitions");
IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: 
///<param name="modes"></param>
///<param name="statid"></param>
///<param name="maxtop"></param>
///</summary>

public string GetClanLeaderboards( object modes, object statid, object maxtop ) { 
RestRequest request = new RestRequest($"/Destiny/Stats/ClanLeaderboards/{param1}/");
request.AddHeader("X-API-KEY", Apikey);
request.AddParameter("modes, modes");request.AddParameter("statid, statid");request.AddParameter("maxtop, maxtop");
IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: Public
///<param name="definitions">Include definitions in the response. Use while testing.</param>
///</summary>

public string GetDestinyAggregateActivityStats( object definitions ) { 
RestRequest request = new RestRequest($"/Destiny/Stats/AggregateActivityStats/{membershipType}/{destinyMembershipId}/{characterId}/");
request.AddHeader("X-API-KEY", Apikey);
request.AddParameter("definitions, definitions");
IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: Public
///<param name="tpage"></param>
///<param name="count">The number of results to return. Default is 10.</param>
///<param name="name">Filter by name.</param>
///<param name="order">Order results.</param>
///<param name="orderstathash"></param>
///<param name="direction"></param>
///<param name="rarity">Filter by item rarity.</param>
///<param name="step"></param>
///<param name="categories"></param>
///<param name="weaponPerformance"></param>
///<param name="impactEffects"></param>
///<param name="guardianAttributes"></param>
///<param name="lightAbilities"></param>
///<param name="damageTypes">Filter by damage type.</param>
///<param name="matchrandomsteps"></param>
///<param name="definitions">Include definitions in the response. Use while testing.</param>
///<param name="sourcecat"></param>
///<param name="sourcehash"></param>
///</summary>

public string GetDestinyExplorerItems( object tpage, object count, object name, object order, object orderstathash, object direction, object rarity, object step, object categories, object weaponPerformance, object impactEffects, object guardianAttributes, object lightAbilities, object damageTypes, object matchrandomsteps, object definitions, object sourcecat, object sourcehash ) { 
RestRequest request = new RestRequest($"/Destiny/Explorer/Items/");
request.AddHeader("X-API-KEY", Apikey);
request.AddParameter("tpage, tpage");request.AddParameter("count, count");request.AddParameter("name, name");request.AddParameter("order, order");request.AddParameter("orderstathash, orderstathash");request.AddParameter("direction, direction");request.AddParameter("rarity, rarity");request.AddParameter("step, step");request.AddParameter("categories, categories");request.AddParameter("weaponPerformance, weaponPerformance");request.AddParameter("impactEffects, impactEffects");request.AddParameter("guardianAttributes, guardianAttributes");request.AddParameter("lightAbilities, lightAbilities");request.AddParameter("damageTypes, damageTypes");request.AddParameter("matchrandomsteps, matchrandomsteps");request.AddParameter("definitions, definitions");request.AddParameter("sourcecat, sourcecat");request.AddParameter("sourcehash, sourcehash");
IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: Public
///<param name="page">The current page to return. Starts at 1.</param>
///<param name="count">The number of results per page. Default is 10.</param>
///<param name="name">Filter by name.</param>
///<param name="direction"></param>
///<param name="weaponPerformance"></param>
///<param name="impactEffects"></param>
///<param name="guardianAttributes"></param>
///<param name="lightAbilities"></param>
///<param name="damageTypes">Filter by damage type.</param>
///<param name="definitions">Include definitions in the response. Use while testing.</param>
///</summary>

public string GetDestinyExplorerTalentNodeSteps( object page, object count, object name, object direction, object weaponPerformance, object impactEffects, object guardianAttributes, object lightAbilities, object damageTypes, object definitions ) { 
RestRequest request = new RestRequest($"/Destiny/Explorer/TalentNodeSteps/");
request.AddHeader("X-API-KEY", Apikey);
request.AddParameter("page, page");request.AddParameter("count, count");request.AddParameter("name, name");request.AddParameter("direction, direction");request.AddParameter("weaponPerformance, weaponPerformance");request.AddParameter("impactEffects, impactEffects");request.AddParameter("guardianAttributes, guardianAttributes");request.AddParameter("lightAbilities, lightAbilities");request.AddParameter("damageTypes, damageTypes");request.AddParameter("definitions, definitions");
IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: Public

public string GetDestinyLiveTileContentItems(   ) { 
RestRequest request = new RestRequest($"/Destiny/LiveTiles/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: Public

public string GetDestinyManifest(   ) { 
RestRequest request = new RestRequest($"/Destiny/Manifest/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: Public
///<param name="definitions">Include definitions in the response. Use while testing.</param>
///<param name="version"></param>
///</summary>

public string GetDestinySingleDefinition( object definitions, object version ) { 
RestRequest request = new RestRequest($"/Destiny/Manifest/{definitionType}/{definitionId}/");
request.AddHeader("X-API-KEY", Apikey);
request.AddParameter("definitions, definitions");request.AddParameter("version, version");
IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: Public
///<param name="definitions">Include definitions in the response. Use while testing.</param>
///</summary>

public string GetExcellenceBadges( object definitions ) { 
RestRequest request = new RestRequest($"/Destiny/Stats/GetExcellenceBadges/{membershipType}/{destinyMembershipId}/");
request.AddHeader("X-API-KEY", Apikey);
request.AddParameter("definitions, definitions");
IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: Public
///<param name="definitions">Include definitions in the response. Use while testing.</param>
///<param name="flavour">Indicates flavour stats should be included with player card data. More testing needed.</param>
///<param name="single">Return data for a single cardId.</param>
///</summary>

public string GetGrimoireByMembership( object definitions, object flavour, object single ) { 
RestRequest request = new RestRequest($"/Destiny/Vanguard/Grimoire/{membershipType}/{destinyMembershipId}/");
request.AddHeader("X-API-KEY", Apikey);
request.AddParameter("definitions, definitions");request.AddParameter("flavour, flavour");request.AddParameter("single, single");
IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: Public

public string GetGrimoireDefinition(   ) { 
RestRequest request = new RestRequest($"/Destiny/Vanguard/Grimoire/Definition/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: Public
///<param name="periodType">Indicates a specific period type to return.</param>
///<param name="modes">Game modes to return. Comma separated.</param>
///<param name="groups">Group of stats to include, otherwise only general stats are returned. Comma separated.</param>
///<param name="monthstart">First month to return when monthly stats are requested. Use the format YYYY-MM.</param>
///<param name="monthend">Last month to return when monthly stats are requested. Use the format YYYY-MM.</param>
///<param name="daystart">First day to return when daily stats are requested. Use the format YYYY-MM-DD.</param>
///<param name="dayend">Last day to return when daily stats are requested. Use the format YYYY-MM-DD.</param>
///</summary>

public string GetHistoricalStats( object periodType, object modes, object groups, object monthstart, object monthend, object daystart, object dayend ) { 
RestRequest request = new RestRequest($"/Destiny/Stats/{membershipType}/{destinyMembershipId}/{characterId}/");
request.AddHeader("X-API-KEY", Apikey);
request.AddParameter("periodType, periodType");request.AddParameter("modes, modes");request.AddParameter("groups, groups");request.AddParameter("monthstart, monthstart");request.AddParameter("monthend, monthend");request.AddParameter("daystart, daystart");request.AddParameter("dayend, dayend");
IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: Public

public string GetHistoricalStatsDefinition(   ) { 
RestRequest request = new RestRequest($"/Destiny/Stats/Definition/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: Public
///<param name="groups">Groups of stats to include, otherwise only general stats are returned. Comma separated.</param>
///</summary>

public string GetHistoricalStatsForAccount( object groups ) { 
RestRequest request = new RestRequest($"/Destiny/Stats/Account/{membershipType}/{destinyMembershipId}/");
request.AddHeader("X-API-KEY", Apikey);
request.AddParameter("groups, groups");
IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: Public
///<param name="definitions">Include definitions in the response. Use while testing.</param>
///</summary>

public string GetItemDetail( object definitions ) { 
RestRequest request = new RestRequest($"/Destiny/{membershipType}/Account/{destinyMembershipId}/Character/{characterId}/Inventory/{itemInstanceId}/");
request.AddHeader("X-API-KEY", Apikey);
request.AddParameter("definitions, definitions");
IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: 
///<param name="definitions">Include definitions in the response. Use while testing.</param>
///</summary>

public string GetItemReferenceDetail( object definitions ) { 
RestRequest request = new RestRequest($"/Destiny/{param1}/Account/{param2}/Character/{param3}/ItemReference/{param4}/");
request.AddHeader("X-API-KEY", Apikey);
request.AddParameter("definitions, definitions");
IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: Private
///<param name="modes">Game modes to return. Comma separated.</param>
///<param name="statid"></param>
///<param name="maxtop"></param>
///</summary>

public string GetLeaderboards( object modes, object statid, object maxtop ) { 
RestRequest request = new RestRequest($"/Destiny/Stats/Leaderboards/{membershipType}/{destinyMembershipId}/");
request.AddHeader("X-API-KEY", Apikey);
request.AddParameter("modes, modes");request.AddParameter("statid, statid");request.AddParameter("maxtop, maxtop");
IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: Private
///<param name="modes">Game modes to return. Comma separated.</param>
///<param name="statid"></param>
///<param name="maxtop"></param>
///</summary>

public string GetLeaderboardsForCharacter( object modes, object statid, object maxtop ) { 
RestRequest request = new RestRequest($"/Destiny/Stats/Leaderboards/{membershipType}/{destinyMembershipId}/{characterId}/");
request.AddHeader("X-API-KEY", Apikey);
request.AddParameter("modes, modes");request.AddParameter("statid, statid");request.AddParameter("maxtop, maxtop");
IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: Private
///<param name="modes">Game modes to return. Comma separated.</param>
///<param name="code">Unknown, further testing needed.</param>
///</summary>

public string GetLeaderboardsForPsn( object modes, object code ) { 
RestRequest request = new RestRequest($"/Destiny/Stats/LeaderboardsForPsn/");
request.AddHeader("X-API-KEY", Apikey);
request.AddParameter("modes, modes");request.AddParameter("code, code");
IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: Public
///<param name="ignorecase">Default is false when not specified. True to cause a caseless search to be used.</param>
///</summary>

public string GetMembershipIdByDisplayName( object ignorecase ) { 
RestRequest request = new RestRequest($"/Destiny/{membershipType}/Stats/GetMembershipIdByDisplayName/{displayName}/");
request.AddHeader("X-API-KEY", Apikey);
request.AddParameter("ignorecase, ignorecase");
IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: Private
///<param name="definitions">Include definitions in the response. Use while testing.</param>
///<param name="flavour">Indicates flavour stats should be included with player card data. More testing needed.</param>
///<param name="single">Return data for a single cardId.</param>
///</summary>

public string GetMyGrimoire( object definitions, object flavour, object single ) { 
RestRequest request = new RestRequest($"/Destiny/Vanguard/Grimoire/{membershipType}/");
request.AddHeader("X-API-KEY", Apikey);
request.AddParameter("definitions, definitions");request.AddParameter("flavour, flavour");request.AddParameter("single, single");
IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: Public
///<param name="definitions">Include definitions in the response. Use while testing.</param>
///</summary>

public string GetPostGameCarnageReport( object definitions ) { 
RestRequest request = new RestRequest($"/Destiny/Stats/PostGameCarnageReport/{activityInstanceId}/");
request.AddHeader("X-API-KEY", Apikey);
request.AddParameter("definitions, definitions");
IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: Public
///<param name="definitions">Include definitions in the response. Use while testing.</param>
///</summary>

public string GetPublicAdvisors( object definitions ) { 
RestRequest request = new RestRequest($"/Destiny/Advisors/");
request.AddHeader("X-API-KEY", Apikey);
request.AddParameter("definitions, definitions");
IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: 
///<param name="definitions">Include definitions in the response. Use while testing.</param>
///</summary>

public string GetPublicAdvisorsV2( object definitions ) { 
RestRequest request = new RestRequest($"/Destiny/Advisors/V2/");
request.AddHeader("X-API-KEY", Apikey);
request.AddParameter("definitions, definitions");
IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: Public
///<param name="definitions">Include definitions in the response. Use while testing.</param>
///</summary>

public string GetPublicVendor( object definitions ) { 
RestRequest request = new RestRequest($"/Destiny/Vendors/{vendorId}/");
request.AddHeader("X-API-KEY", Apikey);
request.AddParameter("definitions, definitions");
IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: Public
///<param name="definitions">Include definitions in the response. Use while testing.</param>
///</summary>

public string GetPublicVendorWithMetadata( object definitions ) { 
RestRequest request = new RestRequest($"/Destiny/Vendors/{vendorId}/Metadata/");
request.AddHeader("X-API-KEY", Apikey);
request.AddParameter("definitions, definitions");
IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: Public
///<param name="definitions">Include definitions in the response. Use while testing.</param>
///</summary>

public string GetPublicXurVendor( object definitions ) { 
RestRequest request = new RestRequest($"/Destiny/Advisors/Xur/");
request.AddHeader("X-API-KEY", Apikey);
request.AddParameter("definitions, definitions");
IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: Private
///<param name="definitions">Include definitions in the response. Use while testing.</param>
///</summary>

public string GetRecordBookCompletionStatus( object definitions ) { 
RestRequest request = new RestRequest($"/Destiny/{membershipType}/MyAccount/RecordBooks/{recordBookHash}/Completion/");
request.AddHeader("X-API-KEY", Apikey);
request.AddParameter("definitions, definitions");
IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: Public
///<param name="definitions">Include definitions in the response. Use while testing.</param>
///</summary>

public string GetSpecialEventAdvisors( object definitions ) { 
RestRequest request = new RestRequest($"/Destiny/Events/");
request.AddHeader("X-API-KEY", Apikey);
request.AddParameter("definitions, definitions");
IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: Public
///<param name="definitions">Include definitions in the response. Use while testing.</param>
///</summary>

public string GetTriumphs( object definitions ) { 
RestRequest request = new RestRequest($"/Destiny/{membershipType}/Account/{destinyMembershipId}/Triumphs/");
request.AddHeader("X-API-KEY", Apikey);
request.AddParameter("definitions, definitions");
IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: Public
///<param name="definitions">Include definitions in the response. Use while testing.</param>
///</summary>

public string GetUniqueWeaponHistory( object definitions ) { 
RestRequest request = new RestRequest($"/Destiny/Stats/UniqueWeapons/{membershipType}/{destinyMembershipId}/{characterId}/");
request.AddHeader("X-API-KEY", Apikey);
request.AddParameter("definitions, definitions");
IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: Private
///<param name="definitions">Include definitions in the response. Use while testing.</param>
///<param name="accountId">A valid destinyMembershipId.</param>
///</summary>

public string GetVault( object definitions, object accountId ) { 
RestRequest request = new RestRequest($"/Destiny/{membershipType}/MyAccount/Vault/");
request.AddHeader("X-API-KEY", Apikey);
request.AddParameter("definitions, definitions");request.AddParameter("accountId, accountId");
IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: 
///<param name="definitions">Include definitions in the response. Use while testing.</param>
///<param name="accountId">A valid destinyMembershipId.</param>
///</summary>

public string GetVaultSummary( object definitions, object accountId ) { 
RestRequest request = new RestRequest($"/Destiny/{membershipType}/MyAccount/Vault/Summary/");
request.AddHeader("X-API-KEY", Apikey);
request.AddParameter("definitions, definitions");request.AddParameter("accountId, accountId");
IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: Private
///<param name="definitions">Include definitions in the response. Use while testing.</param>
///</summary>

public string GetVendorForCurrentCharacter( object definitions ) { 
RestRequest request = new RestRequest($"/Destiny/{membershipType}/MyAccount/Character/{characterId}/Vendor/{vendorId}/");
request.AddHeader("X-API-KEY", Apikey);
request.AddParameter("definitions, definitions");
IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: Private
///<param name="definitions">Include definitions in the response. Use while testing.</param>
///</summary>

public string GetVendorForCurrentCharacterWithMetadata( object definitions ) { 
RestRequest request = new RestRequest($"/Destiny/{membershipType}/MyAccount/Character/{characterId}/Vendor/{vendorId}/Metadata/");
request.AddHeader("X-API-KEY", Apikey);
request.AddParameter("definitions, definitions");
IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: Private
///<param name="definitions">Include definitions in the response. Use while testing.</param>
///</summary>

public string GetVendorItemDetailForCurrentCharacter( object definitions ) { 
RestRequest request = new RestRequest($"/Destiny/{membershipType}/MyAccount/Character/{characterId}/Vendor/{vendorId}/Item/{itemId}/");
request.AddHeader("X-API-KEY", Apikey);
request.AddParameter("definitions, definitions");
IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: Private
///<param name="definitions">Include definitions in the response. Use while testing.</param>
///</summary>

public string GetVendorItemDetailForCurrentCharacterWithMetadata( object definitions ) { 
RestRequest request = new RestRequest($"/Destiny/{membershipType}/MyAccount/Character/{characterId}/Vendor/{vendorId}/Item/{itemId}/Metadata/");
request.AddHeader("X-API-KEY", Apikey);
request.AddParameter("definitions, definitions");
IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: Private
///<param name="definitions">Include definitions in the response. Use while testing.</param>
///</summary>

public string GetVendorSummariesForCurrentCharacter( object definitions ) { 
RestRequest request = new RestRequest($"/Destiny/{membershipType}/MyAccount/Character/{characterId}/Vendors/Summaries/");
request.AddHeader("X-API-KEY", Apikey);
request.AddParameter("definitions, definitions");
IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: Public

public string SearchDestinyPlayer(   ) { 
RestRequest request = new RestRequest($"/Destiny/SearchDestinyPlayer/{membershipType}/{displayName}/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: POST
///Access: Private

public string SetItemLockState(   ) { 
RestRequest request = new RestRequest($"/Destiny/SetLockState/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: POST
///Access: Private

public string SetQuestTrackedState(   ) { 
RestRequest request = new RestRequest($"/Destiny/SetQuestTrackedState/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
