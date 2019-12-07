import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import com.hp.hpl.jena.query.QueryExecution;
import com.hp.hpl.jena.query.QueryExecutionFactory;
import com.hp.hpl.jena.query.QuerySolution;
import com.hp.hpl.jena.query.ResultSet;

public class SemanticWeb {
	private static String TWITTER_API = "http://34.69.24.144:3030/twitter/sparql"; // Akhi
	private static String REDDIT_API = "http://35.188.92.96:3030/reddit/sparql"; // Rahul

	public static String execSelectAndPrint(String serviceURI, String query) {
		QueryExecution q = QueryExecutionFactory.sparqlService(serviceURI, query);
		ResultSet results = q.execSelect();
		JSONArray arr = new JSONArray();
		try {
			while (results.hasNext()) {
				JSONObject obj = new JSONObject();

				QuerySolution soln = results.nextSolution();
				soln.toString();
				obj.put("tag", soln.get("tag"));
				obj.put("twitter_username", soln.get("user_name"));
				obj.put("twitter_text", soln.get("tweet_text"));
				obj.put("reddit_username", soln.get("reddit_username"));
				obj.put("reddit_text", soln.get("reddit_comment"));
				arr.put(obj);
			}
			JSONObject comments = new JSONObject();
			comments.put("data", arr);
			System.out.println(comments.toString());
			return comments.toString();
		} catch (JSONException e) {
			e.printStackTrace();
		}
		return null;
	}

	public static String getData(String team, boolean supportFirstTeam) {

		if (supportFirstTeam) {
			return getSupportersForFirstTeam(team);
		} else {
			return getSupportersForSecondTeam(team);
		}
	}
	
	private static String getSupportersForFirstTeam(String team) {
		String query = "PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>\n" + 
				"PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>\n" + 
				"PREFIX owl: <http://www.w3.org/2002/07/owl#>\n" + 
				"PREFIX foaf:  <http://xmlns.com/foaf/0.1/>\n" + 
				"PREFIX reddit: <http://www.semanticweb.org/rahul5111/ontologies/2019/10/untitled-ontology-10#>\n" + 
				"PREFIX twitter: <http://www.semanticweb.org/rahul5111/ontologies/2019/10/untitled-ontology-9#>\n" + 
				"PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>\n" + 
				"\n" + 
				"\n" + 
				"SELECT  ?reddit_username  ?reddit_comment ?user_name ?tweet_text ?sc\n" + 
				"WHERE\n" + 
				"{\n" + 
				"	?reddit reddit:has_comment ?reddit_comment .\n" + 
				"	?reddit reddit:reddit_wriiten_by ?user .\n" + 
				"	?user  reddit:has_name  ?reddit_username .\n" + 
				"    ?reddit reddit:tag ?tag.\n" + 
				"  	?reddit reddit:sevirity_score ?sc\n" + 
				"	FILTER(?tag = \""+ team + "\") .\n" + 
				"  	FILter(xsd:float(?sc) > 5)\n" + 
				"  SERVICE <"+TWITTER_API+">{ \n" + 
				"    SELECT ?tweet_text ?tag ?user_name ?sc\n" + 
				"	where{\n" + 
				"	?tweet twitter:written_by ?user .\n" + 
				"	?user  twitter:user_name ?user_name .\n" + 
				"	?tweet twitter:has_text_content ?tweet_text .\n" + 
				"	?tweet twitter:severity_score ?sc.\n" + 
				"	?tweet twitter:tag ?tag.\n" + 
				"  }\n" + 
				"}\n" + 
				"}\n" + 
				"ORDER BY ?sc\n" + 
				"Limit 100";
		System.out.println("Query 1 is " + query);
		return execSelectAndPrint(REDDIT_API, query);
	}
	
	
	private static String getSupportersForSecondTeam(String team) {
		String query = "PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>\n" + 
				"PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>\n" + 
				"PREFIX owl: <http://www.w3.org/2002/07/owl#>\n" + 
				"PREFIX foaf:  <http://xmlns.com/foaf/0.1/>\n" + 
				"PREFIX reddit: <http://www.semanticweb.org/rahul5111/ontologies/2019/10/untitled-ontology-10#>\n" + 
				"PREFIX twitter: <http://www.semanticweb.org/rahul5111/ontologies/2019/10/untitled-ontology-9#>\n" + 
				"PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>\n" + 
				"\n" + 
				"\n" + 
				"SELECT  ?reddit_username  ?reddit_comment ?user_name ?tweet_text ?sc\n" + 
				"WHERE\n" + 
				"{\n" + 
				"	?reddit reddit:has_comment ?reddit_comment .\n" + 
				"	?reddit reddit:reddit_wriiten_by ?user .\n" + 
				"	?user  reddit:has_name  ?reddit_username .\n" + 
				"    ?reddit reddit:tag ?tag.\n" + 
				"  	?reddit reddit:sevirity_score ?sc\n" + 
				"	FILTER(?tag = \""+ team + "\") .\n" + 
				"  	FILter(xsd:float(?sc) < 5)\n" + 
				"  SERVICE <"+TWITTER_API+">{ \n" + 
				"    SELECT ?tweet_text ?tag ?user_name ?sc\n" + 
				"	where{\n" + 
				"	?tweet twitter:written_by ?user .\n" + 
				"	?user  twitter:user_name ?user_name .\n" + 
				"	?tweet twitter:has_text_content ?tweet_text .\n" + 
				"	?tweet twitter:severity_score ?sc.\n" + 
				"	?tweet twitter:tag ?tag.\n" + 
				"  }\n" + 
				"}\n" + 
				"}\n" + 
				"ORDER BY ?sc\n" + 
				"Limit 100";
		System.out.println("Query 2 is " + query);
		return execSelectAndPrint(REDDIT_API, query);
	}
}