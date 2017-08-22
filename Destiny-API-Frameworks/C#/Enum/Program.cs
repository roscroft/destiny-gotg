using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;

namespace JsonToEnum
{
    class Program
    {
        static void Main(string[] args)
        {
            int counter = 0;
            string line;
            string name_space = "JsonToEnum.Export"; //Namespace to export to
            List<string> EnumEntries = new List<string>(); 
            StreamReader enumjson = new StreamReader("enum.txt"); //Json file(yes its .txt)
            string curdef = "UNDEFINED";

            while ((line = enumjson.ReadLine()) != null) //If line exists
            {
                string _line;
                _line = line.Replace('{', ' '); //Remove all brackets
                _line = _line.Replace('}', ' ');
                _line = _line.Trim(); //Trim off whitespace
                if (_line != " " && _line != "," && _line != string.Empty)//Make sure line isn't blank or a comma.
                {
                    string[] words = _line.Split(':'); //Split line into an array of strings
                    if (words.Count() != 0) //If the string array isnt blank
                    {
                        if (words[1] == string.Empty) //Check to see if the line has nothing after the : 
                                                      //    `"IgnoredItemType": ` would pass this check
                        {
                            if (EnumEntries.Count > 0) //If the list has any information stored
                            {
                                var formattedentries = string.Join(" ", EnumEntries); //Formated stored enum info into one large sentence

                                //Format .cs file
                                var formattedOutput = $"namespace {name_space} {{ \r\n " + 
                                    $"\tpublic enum {curdef} " +
                                    $"\r\n \t{{ \r\n " +
                                    $"\t\t" + string.Join(" \r\n \t\t", EnumEntries) + "" +
                                    " \r\n \t} " +
                                    "\r\n } ";

                                //Write .cs file
                                File.WriteAllText($"enums/{curdef}.cs", formattedOutput);
                                Console.WriteLine($"Exported {curdef}.cs");
                                //Wipe stored enum info
                                EnumEntries.Clear();
                                //Change current definition
                                curdef = words[0].Replace('"', ' ');
                                counter++;
                            }
                            else
                            {
                                //This code runs on the very first entry as EnumEntries contains nothing.
                                curdef = words[0].Replace('"', ' ');
                            }
                        }
                        else
                        {
                            //If the line HAS content after the : this will run
                            //ex: `"All": 0,` 
                            string FormattedEnumEntry;
                            FormattedEnumEntry = _line.Replace(':', '=');
                            //`"All" = 0,`
                            FormattedEnumEntry = FormattedEnumEntry.Replace('"', ' ');
                            //`All = 0,` <--- VALID C# CODE
                            EnumEntries.Add(FormattedEnumEntry);
                            //Add to stored enum info. used later
                        }
                    }
                    else
                    {
                        Console.WriteLine("Line blank.");
                    }
                }
            }

            Console.ReadLine();
        }
    }
}
