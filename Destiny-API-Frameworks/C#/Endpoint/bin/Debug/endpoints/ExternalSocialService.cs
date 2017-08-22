 ///<summary>
///HTTP Method: GET
///Access: 
///<param name="head"></param>
///<param name="ctype"></param>
///<param name="tag"></param>
///<param name="currentpage">The current page to return. Starts at 1.</param>
///<param name="searchtext"></param>
///</summary>

public string SearchContentWithText( object head, object ctype, object tag, object currentpage, object searchtext ) { 
RestRequest request = new RestRequest($"/Content/Search/{param1}/");
request.AddHeader("X-API-KEY", Apikey);
request.AddParameter("head, head");request.AddParameter("ctype, ctype");request.AddParameter("tag, tag");request.AddParameter("currentpage, currentpage");request.AddParameter("searchtext, searchtext");
IRestResponse response = client.Execute(request);
return response.Response;
}
