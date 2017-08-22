using Newtonsoft.Json;
using Newtonsoft.Json.Linq;
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace JsonToEndpoint
{
    class Program
    {
        static void Main(string[] args)
        {
            string js;

            js = File.ReadAllText("destinyservice.json");
            //var output = line.Split('[', ']').Where((item, index) => index % 2 != 0).ToList();

            string _cs = null; //CSharp 
            string _sm = null; //Summary
            string _cd;
            string _m = null;
            Dictionary<string, string> _p = new Dictionary<string, string>(); //Parameters and description
            int counter = 0;


            dynamic deserializedobj = JsonConvert.DeserializeObject<dynamic>(js);
            
            foreach(var service in deserializedobj)
            {
                foreach (var method in service)
                {
                    foreach (var rawentry in method)
                    {
                        foreach (var key in rawentry)
                        {
                            foreach (var value in key)
                            {
                                string _key = Convert.ToString(key);
                                string[] keys = _key.Split(':');
                                _key = keys[0];
                                string _value = Convert.ToString(value);
                                //_key = _key.Trim();
                                //_key = _key.Trim('{');
                                //_key = _key.Trim('}');
                                //_key = _key.Replace('"', ' ');
                                //_value = _value.Trim();
                                //_value = _value.Trim('{');
                                //_value = _value.Trim('}');
                                //_value = _value.Replace('"', ' ');

                                string tempkey = _key.Replace('"', ' ');
                                tempkey = tempkey.Trim();

                                switch (tempkey.ToLower())
                                {
                                    case "name":
                                        if (_cs != null)
                                        {
                                            //Format
                                            string _summaries = "";
                                            string _parameters = "";

                                            if (_p.Count > 0)
                                            {
                                                List<string> parameters = new List<string>();
                                                foreach (var k in _p)
                                                {
                                                    _summaries = _summaries + $"///<param name=\"{k.Key}\">{k.Value}</param>\r\n";
                                                    parameters.Add(k.Key);
                                                }
                                                _parameters = string.Join(", object ", parameters);
                                                _sm = _sm + _summaries;
                                                _sm = _sm + "///</summary>";
                                            }


                                            if (_parameters != "")
                                            {
                                                _cs = _cs.Replace("-ARGUMENTS-", "object "+_parameters);
                                            }
                                            else
                                            {
                                                _cs = _cs.Replace("-ARGUMENTS-", " ");
                                            }

                                            _cs = _sm + "\r\n" + _cs;


                                            _cs = _cs + "\r\nIRestResponse response = client.Execute(request);\r\nreturn response.Response;\r\n}";

                                            counter++;

                                            //Export
                                            using (StreamWriter sq = File.AppendText($"endpoints/{service.Path}.cs"))
                                            {
                                                sq.WriteLine(_cs);
                                                Console.WriteLine($"Saved. {counter} endpoints done so far.");
                                            }
                                            //Reset
                                            _cs = $"public string {_value}( -ARGUMENTS- ) {{ \r\n";
                                            _cd = tempkey;
                                            _p.Clear();
                                        }
                                        else
                                        {
                                            //Prepare code
                                            _cs = $"\r\npublic string {_value}( -ARGUMENTS- ) \r\n {{ \r\n";
                                            _cd = tempkey;
                                        }
                                        break;
                                    case "method":
                                        //Prepare Summary
                                        _sm = " ";
                                        _sm = _sm + "///<summary>\r\n";
                                        _sm = _sm + $"///HTTP Method: {_value}";
                                        _m = _value;
                                        break;
                                    case "endpoint":
                                        _cs = _cs + $"RestRequest request = new RestRequest($\"{_value}\");\r\n";
                                        _cs = _cs + $"request.AddHeader(\"X-API-KEY\", Apikey);\r\n";
                                        break;
                                    case "params":
                                        foreach (JProperty obj in value)
                                        {
                                            string[] parameters = obj.ToString().Split(':');
                                            string param = parameters[0].Replace('"', ' ');
                                            param = param.Trim();
                                            _cs += $"request.AddParameter(\"{param}, {param}\");";
                                            _p.Add(param, $"{obj.Value["desc"]}");
                                        }
                                        break;
                                    case "post":
                                        if (_m.Contains("POST"))
                                        {

                                        }
                                        break;
                                    case "path":
                                        Console.WriteLine("path");
                                        break;
                                    case "access":
                                        _sm = _sm + "\r\n///Access: "+_value+"\r\n";
                                        break;
                                }
                            }
                        }
                    }
                }
            }

            Console.ReadLine();
        }
    }
}