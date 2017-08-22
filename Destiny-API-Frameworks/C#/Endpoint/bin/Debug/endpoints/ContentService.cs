 ///<summary>
///HTTP Method: GET
///Access: 

public string ResetNotification(   ) { 
RestRequest request = new RestRequest($"/Notification/Reset/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: 

public string GetCareer(   ) { 
RestRequest request = new RestRequest($"/Content/Careers/{param1}/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: 

public string GetCareers(   ) { 
RestRequest request = new RestRequest($"/Content/Careers/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: 
///<param name="head"></param>
///</summary>

public string GetContentById( object head ) { 
RestRequest request = new RestRequest($"/Content/GetContentById/{param1}/{param2}/");
request.AddHeader("X-API-KEY", Apikey);
request.AddParameter("head, head");
IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: 
///<param name="head"></param>
///</summary>

public string GetContentByTagAndType( object head ) { 
RestRequest request = new RestRequest($"/Content/GetContentByTagAndType/{param1}/{param2}/{param3}/");
request.AddHeader("X-API-KEY", Apikey);
request.AddParameter("head, head");
IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: 

public string GetContentType(   ) { 
RestRequest request = new RestRequest($"/Content/GetContentType/{param1}/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: 

public string GetDestinyContent(   ) { 
RestRequest request = new RestRequest($"/Content/Site/Destiny/{param1}/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: 

public string GetDestinyContentV2(   ) { 
RestRequest request = new RestRequest($"/Content/Site/Destiny/V2/{param1}/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: 

public string GetFeaturedArticle(   ) { 
RestRequest request = new RestRequest($"/Content/Site/Featured/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: 

public string GetHomepageContent(   ) { 
RestRequest request = new RestRequest($"/Content/Site/Homepage/{param1}/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: 

public string GetHomepageContentV2(   ) { 
RestRequest request = new RestRequest($"/Content/Site/Homepage/V2/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: 

public string GetJobs(   ) { 
RestRequest request = new RestRequest($"/Content/Site/Jobs/{param1}/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: 
///<param name="itemsperpage"></param>
///<param name="currentpage">The current page to return. Starts at 1.</param>
///</summary>

public string GetNews( object itemsperpage, object currentpage ) { 
RestRequest request = new RestRequest($"/Content/Site/News/{param1}/{param2}/");
request.AddHeader("X-API-KEY", Apikey);
request.AddParameter("itemsperpage, itemsperpage");request.AddParameter("currentpage, currentpage");
IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: 

public string GetPromoWidget(   ) { 
RestRequest request = new RestRequest($"/Content/Site/Destiny/Promo/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: 

public string GetPublications(   ) { 
RestRequest request = new RestRequest($"/Content/Site/Publications/{param1}/");
request.AddHeader("X-API-KEY", Apikey);

IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: 
///<param name="searchtext"></param>
///</summary>

public string SearchCareers( object searchtext ) { 
RestRequest request = new RestRequest($"/Content/Careers/Search/");
request.AddHeader("X-API-KEY", Apikey);
request.AddParameter("searchtext, searchtext");
IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: GET
///Access: 
///<param name="head"></param>
///<param name="currentpage">The current page to return. Starts at 1.</param>
///<param name="itemsperpage"></param>
///</summary>

public string SearchContentByTagAndType( object head, object currentpage, object itemsperpage ) { 
RestRequest request = new RestRequest($"/Content/SearchContentByTagAndType/{param1}/{param2}/{param3}/");
request.AddHeader("X-API-KEY", Apikey);
request.AddParameter("head, head");request.AddParameter("currentpage, currentpage");request.AddParameter("itemsperpage, itemsperpage");
IRestResponse response = client.Execute(request);
return response.Response;
}
 ///<summary>
///HTTP Method: POST
///Access: Private
///<param name="head"></param>
///</summary>

public string SearchContentEx( object head ) { 
RestRequest request = new RestRequest($"/Content/SearchEx/{param1}/");
request.AddHeader("X-API-KEY", Apikey);
request.AddParameter("head, head");
IRestResponse response = client.Execute(request);
return response.Response;
}
