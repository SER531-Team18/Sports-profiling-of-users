<!DOCTYPE html>
<html>
<head>

<link rel="stylesheet" type="text/css" href="./index.css" />
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
</head>
<body>
	<div class="header">
		<div class="header-logo">
			<img src="./What-is-Semantic-Web.jpeg" alt="logo" class="logo">
			<h1 class="title">Sematic Based User Profiling</h1>
		</div>
	</div>
	<h1>Please select the game:</h1>

	<div class="homepage-container">
		<section id="CLEvsDEN" onclick='selectedGame("CLEvsDEN")'>
			<h1>CLEvsDEN</h1>
			<img class="games" src="./cleveland-browns-denver-broncos-logo1.jpg"
				alt="ClevelandBrownsvsDenverBroncos" data-gamename="Cleveland" />
		</section>
		<section id="NEvsBAL" onclick='selectedGame("NEvsBAL")'>
			<h1>NEvsBAL</h1>
			<img src="./New-England-Patriots-@-Baltimore-Ravens.jpg"
				alt="New-England-Patriots-@-Baltimore-Ravens" />
		</section>
		<section id="NYJvsMIA" onclick='selectedGame("NYJvsMIA")'>
			<h1>NYJvsMIA</h1>
			<img src="./newyorkvsmaimi.png" alt="newyorkvsmaimi" />
		</section>
		<section id="LakeShow" onclick='selectedGame("LakersVsSpurs")'>
			<h1>LakersVsSpurs</h1>
			<img src="./spurs_vs_lakers.jpg" alt="spurs_vs_lakers" />
		</section>
		<section id="MINvsKC" onclick='selectedGame("MINvsKC")'>
			<h1>MINvsKC</h1>
			<img src="./vikings-vs-chiefs.jpg" alt="vikings-vs-chiefs" />
		</section>
	</div>
	<br />
	<br />
	<div>
		<label class="game_label"> Game Selected is</label> <input type="text"
			id="gameName" class="input_text"></input><div id="loading" class="hide" >Loading<img style="height:50px; width:50px" src="./giphy.gif"/></div>
	</div>
	
	<div style="float: left">
		<h1>Please select nature of Users:</h1>
		<div class="radiotext">
			<input type="radio" name="type" id="support" value="30"/>
			Supporters - Users who commented positively for the first team and against second team<br> 
			<input type="radio" name="type" id="hater" value="60"/> 
			Haters - Users who commented against the first team, in support of second team.<br>
			<span class="button" onclick="submit()">Submit</span>
		</div>
		<div style="margin-top: 70px; text-align: center">
			
			<div id="clvData"></div>
		</div>

	</div>

</body>
<script>

$(document).ready(function(){
  //testAjax();
});

	var selectGame = "";
	function selectedGame(game) {
		document.getElementById("gameName").value = game;
		selectGame = game;
	}
	function submit() {
		if(selectGame == "") {
			alert("No Game Selected");
			return;
		}
		
		$("#clvData").html("");
		if (document.getElementById('support').checked) {
			getData("true");
		} else if (document.getElementById('hater').checked) {
			getData("false");
		}
		
	}

	function getData(support) {
		
		if(selectGame=="LakersVsSpurs"){
			selectGame = "LakeShow";
		}
		$("#loading").removeClass("hide");
		url = "http://localhost:8080/MavenWebApp/getData.action?team="+selectGame+"&support="+support;
		sendAjaxRequest(url, function(resp) {
			var json = resp.data;
			var obj = JSON.parse(json);
			var table = "<table id=\"comment_table\">";
			table += "<tr>";
			table += "<th> User Name </th>";
			table += "<th> Comment </th>";
			table += "</tr>";
			for (i in obj.data) {
				console.log(obj.data[i].twitter_username);
				table += getRow(obj.data[i].reddit_text,
						obj.data[i].reddit_username);
				table += getRow(obj.data[i].twitter_text,
						obj.data[i].twitter_username);
			}
			$("#clvData").html(table);
			$("#loading").addClass("hide");
		});
	}

	function getRow(comment, user) {
		var row = "<tr>";
		row += "<td>" + user + "</td>";
		row += "<td>" + comment + "</td>";
		row += "</tr>";
		return row;
	}

	function sendAjaxRequest(url, successCallBackFn) {
		$.ajax({
			type : "GET",
			url : url,
			success : successCallBackFn,
			statusCode : {
				419 : function() {
					showPage("");
				}
			},
			error : function() {
				alert("Unable to process your request.");
			}
		});
	}
</script>
</html>