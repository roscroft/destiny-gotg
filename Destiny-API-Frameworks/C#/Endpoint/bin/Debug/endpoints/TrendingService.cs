 ///<summary>
///HTTP Method: POST
///Access: Private

public string ReturnAssignedReports(   ) { 
RestRequest request = new RestRequest($"/Admin/Assigned/ReturnAll");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: 

public string GetTrendingCategories(   ) { 
RestRequest request = new RestRequest($"/Trending/Categories/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: 

public string GetTrendingCategory(   ) { 
RestRequest request = new RestRequest($"/Trending/Categories/{param1}/{param2}/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
