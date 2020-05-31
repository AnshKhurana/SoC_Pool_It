var start=undefined;
var end=undefined;
var text=undefined;
var service_type=undefined;
var group_ids_string=undefined;



window.onload=function ServiceFiltering(){
					var select=document.getElementById("services_available");
					select.innerHTML=" ";
//	const axios = require("axios").default;

					axios.get("http://127.0.0.1:8000/api/servicefilter/",{
						params:{
							service:service_type,
							group_ids:group_ids_string,
							start_time:start,
							end_time:end,
							text:text
						}
					}).then(
						function(response){
							reply=response.data;
							console.log(reply);

							for (item in reply){
								if(reply[item].is_active==true){
									if(reply[item].service_type=='Food' || reply[item].service_type=='Shopping'){
										if(reply[item].is_member==true){
											select.innerHTML += "<li> <div>" +
											"<h3>" + reply[item].service_type+" Service</h3>" +
				 							"<h2>" + reply[item].vendor + "</h2>" +
											"<p> by " + reply[item].initiator + "</p>" +
											"<h4><p>Start Time: " + reply[item].start_time + "<br> End Time: " + reply[item].end_time + "</p> </h4>" +
											"<span> " + reply[item].service_desc + "</span>" +
											"<button >Already a member</button>"
											+ " </div> </li>";
										}

										else{
											select.innerHTML += "<li> <div>" +
											"<h3>" + reply[item].service_type+" Service</h3>" +
											"<h2>" + reply[item].vendor + "</h2>" +
											"<p> by " + reply[item].initiator + "</p>" +
											"<h4><p>Start Time: " + reply[item].start_time + "<br> End Time: " + reply[item].end_time + "</p> </h4>" +
											"<span> " + reply[item].service_desc + "</span>" +
											"<button onclick=\"join_service(" + reply[item].service_id + ")\" id=\"" + reply[item].service_id + "\">Join Service</button>"
											+ "</div> </li>";
										}
									}

									if(reply[item].service_type=='Event'){
										if(reply[item].is_member==true){
											select.innerHTML += "<li><div>" +
											"<h3>Event Service</h3>" +
				 							"<h2>" + reply[item].event_type + "</h2>" +
											"<h5>at " + reply[item].location + "</h5>"
											"<p> by " + reply[item].initiator + "</p>" +
											"<h4><p>Start Time: " + reply[item].start_time + "<br> End Time: " + reply[item].end_time + "</p> </h4>" +
											"<span> " + reply[item].service_desc + "</span>" +
											"<button >Already a member</button>"
											+ "</div> </li>";
										}

										else{
											select.innerHTML += "<li><div>" +
											"<h3>Event Service</h3>" +
											"<h2>" + reply[item].event_type + "</h2>" +
											"<p> by " + reply[item].initiator + "</p>" +
											"<h4><p>Start Time: " + reply[item].start_time + "<br> End Time: " + reply[item].end_time + "</p> </h4>" +
											"<span> " + reply[item].service_desc + "</span>" +
											"<button onclick=\"join_service(" + reply[item].service_id + ")\" id=\"" + reply[item].service_id + "\">Join Service</button>"
											+ "</div> </li>";
										}
									}

									if(reply[item].service_type=='Travel'){
										if(reply[item].is_member==true){
											select.innerHTML += "<li><div>" +
											"<h3>Travel Service</h3>" +
				 							"<h5>via " + reply[item].transport + "</h5>" +
											"<h4><p>From: " + reply[item].start_point + "<br> To: " + reply[item].end_point + "</p></h4>"
											"<p> by " + reply[item].initiator + "</p>" +
											"<h4><p>Start Time: " + reply[item].start_time + "<br> End Time: " + reply[item].end_time + "</p> </h4>" +
											"<span> " + reply[item].service_desc + "</span>" +
											"<button >Already a member</button>"
											+ "</div> </li>";
										}

										else{
											select.innerHTML += "<li><div>" +
											"<h3>Travel Service</h3>" +
											"<h5>" + reply[item].transport + "</h5>" +
											"<h4><p>From: " + reply[item].start_point + "<br> To: " + reply[item].end_point + "</p></h4>"
											"<p> by " + reply[item].initiator + "</p>" +
											"<h4><p>Start Time: " + reply[item].start_time + "<br> End Time: " + reply[item].end_time + "</p> </h4>" +
											"<span> " + reply[item].service_desc + "</span>" +
											"<button onclick=\"join_service(" + reply[item].service_id + ")\" id=\"" + reply[item].service_id + "\">Join Service</button>"
											+ "</div> </li>";
										}
									}

									if(reply[item].service_type=="Other"){
										if(reply[item].is_member==true){
											select.innerHTML += "<li> <div>" +
											"<h3>Other Service</h3>" +
											"<p> by " + reply[item].initiator + "</p>" +
											"<h4><p>Start Time: " + reply[item].start_time + "<br> End Time: " + reply[item].end_time + "</p> </h4>" +
											"<span> " + reply[item].service_desc + "</span>" +
											"<button >Already a member</button>"
											+ " </div> </li>";
										}

										else{
											select.innerHTML += "<li> <div>" +
											"<h3>Other Service</h3>" +
											"<p> by " + reply[item].initiator + "</p>" +
											"<h4><p>Start Time: " + reply[item].start_time + "<br> End Time: " + reply[item].end_time + "</p> </h4>" +
											"<span> " + reply[item].service_desc + "</span>" +
											"<button onclick=\"join_service(" + reply[item].service_id + ")\" id=\"" + reply[item].service_id + "\">Join Service</button>"
											+ "</div> </li>";
										}
									}
								}
							}

						}).catch(function(error){
							//handle error
							alert(error);
							console.log(error.toJSON()); 
						})
				}


function join_service(service_id){
	var btn=getElementById(service_id);

	if(btn.innerHTML=='Already a member'){
		alert("You are already a member of this service")
	}

	if(btn.innerHTML=='Join Service'){
//		const axios = require('axios').default;
		axios.get('http://127.0.0.1:8000/api/addservicemember/',{
			params:{
				id:service_id,
			}
		}).then(
			function(response){
				reply=response.data;
				console.log(reply);
				if(reply.message=='Successfully joined the service'){
					btn.innerHTML="Already a member";
				}

				else{
					btn.innerHTML="Service ended"
				}
			})
	}
}

function DateTime(){
	start=document.getElementById("from").value;
	end=document.getElementById("until").value;

	if (start==undefined || start=="" ){
		start = undefined;
	}
	if ( end==undefined || end=="" ){
		end=undefined;
	}
	
	ServiceFiltering();
}

function search_service(){
	text=document.getElementById("myInput").value;
	
	if (text==""){
		text=undefined;
	}

	ServiceFiltering();
}

categories("all")
function categories(c){
	var checkbox=document.getElementByClassName("CatCheck");
	service_type = String(c);
	if (service_type=="all"){
		service_type=undefined;
	}
	if(checked.checked== true)
	ServiceFiltering();
}



function group_filter() {
    var list = document.querySelectorAll(`input[name="group"]:checked`);
    let group_ids_string = "";

    for(var i=0; i<list.length; i++){
		group_ids_string += String(list[i].value)+" ";
	}

    if(group_ids_string==""){
		group_ids_string=undefined;
	}
    ServiceFiltering();
}




