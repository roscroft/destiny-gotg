 ///<summary>
///HTTP Method: GET
///Access: 

public string GetTrendingEntryDetail(   ) { 
RestRequest request = new RestRequest($"/Trending/Details/{param1}/{param2}/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: POST
///Access: Private

public string ApplyOfferToCurrentDestinyMembership(   ) { 
RestRequest request = new RestRequest($"/Tokens/ApplyOfferToCurrentDestinyMembership/{param1}/{param2}/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: POST
///Access: Private

public string BreakBond(   ) { 
RestRequest request = new RestRequest($"/Tokens/RAF/BreakBond/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: POST
///Access: Private

public string ClaimAndApplyOnToken(   ) { 
RestRequest request = new RestRequest($"/Tokens/ClaimAndApplyToken/{tokenType}/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: POST
///Access: Private

public string ClaimToken(   ) { 
RestRequest request = new RestRequest($"/Tokens/Claim/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: POST
///Access: Private

public string ConsumeMarketplacePlatformCodeOffer(   ) { 
RestRequest request = new RestRequest($"/Tokens/ConsumeMarketplacePlatformCodeOffer/{param1}/{param2}/{param3}/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: 

public string GetCurrentUserOfferHistory(   ) { 
RestRequest request = new RestRequest($"/Tokens/OfferHistory/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: 

public string GetCurrentUserThrottleState(   ) { 
RestRequest request = new RestRequest($"/Tokens/ThrottleState/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: 

public string GetRAFEligibility(   ) { 
RestRequest request = new RestRequest($"/Tokens/RAF/GetEligibility/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: 

public string MarketplacePlatformCodeOfferHistory(   ) { 
RestRequest request = new RestRequest($"/Tokens/MarketplacePlatformCodeOfferHistory/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: POST
///Access: Private

public string RAFClaim(   ) { 
RestRequest request = new RestRequest($"/Tokens/RAF/Claim/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: POST
///Access: Private

public string RAFGenerateReferralCode(   ) { 
RestRequest request = new RestRequest($"/Tokens/RAF/GenerateReferralCode/{param1}/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: 

public string RAFGetNewPlayerBondDetails(   ) { 
RestRequest request = new RestRequest($"/Tokens/RAF/GetNewPlayerBondDetails/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: 

public string RAFGetVeteranBondDetails(   ) { 
RestRequest request = new RestRequest($"/Tokens/RAF/GetVeteranBondDetails/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
