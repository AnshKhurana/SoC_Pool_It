var start=undefined;
var end=undefined;
var text=undefined;
var service_type=undefined;
var group_ids_string=undefined;



function ServiceFiltering(){
	var select=document.getElementById("services_available");
	select.innerHTML=" ";
	axios.get("http://127.0.0.1:8000/api/servicefilter/",{
		params:{
			group_ids:group_ids_string,
			service:service_type,
			start_time:start,
			end_time:end,
			text:text
		}
	}).then(
		function(response){
			reply=response.data;
			console.log(reply);
			console.log(response.request);

			for (item in reply){
				if(reply[item].is_active===true){
					if(reply[item].service_type==='Food' || reply[item].service_type==='Shopping'){
						if(reply[item].is_member===true){
							select.innerHTML += "<li> <div>" +
							"<h3>" + reply[item].service_type+" Service</h3>" +
 							"<h2>" + reply[item].vendor + "</h2>" +
							"<p> by " + reply[item].initiator + "</p>" +
							"<h4><p>Start Time: " + reply[item].start_time + "<br> End Time: " + reply[item].end_time + "</p> </h4>" +
							"<span> " + reply[item].service_desc + "</span>" +
							"<button >Already a member</button>" +
							" </div> </li>";
						}

						else if(reply[item].is_member===false){
							select.innerHTML += "<li> <div>" +
							"<h3>" + reply[item].service_type+" Service</h3>" +
							"<h4 id=\"msg "+ reply[item].service_id + "\" style=\"'color: Red;'\"></h4>" +
							"<h2>" + reply[item].vendor + "</h2>" +
							"<p> by " + reply[item].initiator + "</p>" +
							"<h4><p>Start Time: " + reply[item].start_time + "<br> End Time: " + reply[item].end_time + "</p> </h4>" +
							"<span> " + reply[item].service_desc + "</span>" +
							"<button onclick=\"join_service(" + "'" + reply[item].service_id + "'" + ")\" id=\"" + reply[item].service_id + "\">Join Service</button>" +
							"</div> </li>";
						}
					}

					if(reply[item].service_type==='Event'){
						if(reply[item].is_member===true){
							select.innerHTML += "<li><div>" +
							"<h3>Event Service</h3>" +
 							"<h2>" + reply[item].event_type + "</h2>" +
							"<h5>at " + reply[item].location + "</h5>" +
							"<p> by " + reply[item].initiator + "</p>" +
							"<h4><p>Start Time: " + reply[item].start_time + "<br> End Time: " + reply[item].end_time + "</p> </h4>" +
							"<span> " + reply[item].service_desc + "</span>" +
							"<button >Already a member</button>" +
							"</div> </li>";
						}

						else if(reply[item].is_member===false){
							select.innerHTML += "<li><div>" +
							"<h3>Event Service</h3>" +
							"<h4 id=\"msg "+ reply[item].service_id + "\" style=\"'color: Red;'\"></h4>" +
							"<h2>" + reply[item].event_type + "</h2>" +
							"<h5>at " + reply[item].location + "</h5>" +
							"<p> by " + reply[item].initiator + "</p>" +
							"<h4><p>Start Time: " + reply[item].start_time + "<br> End Time: " + reply[item].end_time + "</p> </h4>" +
							"<span> " + reply[item].service_desc + "</span>" +
							"<button onclick=\"join_service(" + "'" + reply[item].service_id + "'" + ")\" id=\"" + reply[item].service_id + "\">Join Service</button>" +
							"</div> </li>";
						}
					}

					if(reply[item].service_type==='Travel'){
						if(reply[item].is_member===true){
							select.innerHTML += "<li><div>" +
							"<h3>Travel Service</h3>" +
 							"<h4>via " + reply[item].transport + "</h4>" +
							"<h4><p>From: " + reply[item].start_point + "<br> To: " + reply[item].end_point + "</p></h4>" +
							"<p> by " + reply[item].initiator + "</p>" +
							"<h4><p>Start Time: " + reply[item].start_time + "<br> End Time: " + reply[item].end_time + "</p> </h4>" +
							"<span> " + reply[item].service_desc + "</span>" +
							"<button >Already a member</button>" +
							"</div> </li>";
						}

						else if(reply[item].is_member===false){
							select.innerHTML += "<li><div>" +
							"<h3>Travel Service</h3>" +
							"<h4 id=\"msg "+ reply[item].service_id + "\" style=\"'color: Red;'\"></h4>" +
							"<h4>" + reply[item].transport + "</h4>" +
							"<h4><p>From: " + reply[item].start_point + "<br> To: " + reply[item].end_point + "</p></h4>" +
							"<p> by " + reply[item].initiator + "</p>" +
							"<h4><p>Start Time: " + reply[item].start_time + "<br> End Time: " + reply[item].end_time + "</p> </h4>" +
							"<span> " + reply[item].service_desc + "</span>" +
							"<button onclick=\"join_service(" + "'" + reply[item].service_id + "'" + ")\" id=\"" + reply[item].service_id + "\">Join Service</button>" +
							"</div> </li>";
						}
					}

					if(reply[item].service_type==="Other"){
						if(reply[item].is_member===true){
							select.innerHTML += "<li> <div>" +
							"<h3>Other Service</h3>" +
							"<p> by " + reply[item].initiator + "</p>" +
							"<h4><p>Start Time: " + reply[item].start_time + "<br> End Time: " + reply[item].end_time + "</p> </h4>" +
							"<span> " + reply[item].service_desc + "</span>" +
							"<button >Already a member</button>" +
							" </div> </li>";
						}

						else if(reply[item].is_member===false){
							select.innerHTML += "<li> <div>" +
							"<h3>Other Service</h3>" +
							"<h4 id=\"msg "+ reply[item].service_id + "\" style=\"'color: Red;'\"></h4>" +
							"<p> by " + reply[item].initiator + "</p>" +
							"<h4><p>Start Time: " + reply[item].start_time + "<br> End Time: " + reply[item].end_time + "</p> </h4>" +
							"<span> " + reply[item].service_desc + "</span>" +
							"<button onclick=\"join_service(" + "'" + reply[item].service_id + "'" + ")\" id=\"" + reply[item].service_id + "\">Join Service</button>" +
							"</div> </li>";
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


////////////////////////////////////////////////////////////////////////////


function join_service(service_id){
	var btn=document.getElementById(service_id);

	if(btn.innerHTML==='Already a member'){
		alert("You are already a member of this service");
	}

	if(btn.innerHTML==='Join Service'){
		r=confirm("Are you sure about joining this service?")
		if (r===true){
			axios.get('http://127.0.0.1:8000/api/addservicemember/',{
				params:{
					id:service_id,
				}
			}).then(
				function(response){
					reply=response.data;
					console.log(reply);
					if(reply.message==='Successfully joined the service'){
						btn.innerHTML="Already a member";
						document.getElementById("msg " +service_id).innerHTML = "You have successfully joined the service";
						setTimeout(function(){
    						document.getElementById("msg " + service_id).innerHTML = '';
							}, 3000);
					}

					else{
						btn.innerHTML="Service ended"
					}
			}).catch(
				function(error){
					alert(error);
					console.log(error.toJSON());
			})
		}
	}
}


////////////////////////////////////////////////////////////////////////////


function DateTime(){
	start=document.getElementById("from").value;
	end=document.getElementById("until").value;

	if (start===undefined || start==="" ){
		start = undefined;
	}
	if ( end===undefined || end==="" ){
		end=undefined;
	}
	
	ServiceFiltering();
}


////////////////////////////////////////////////////////////////////////////


function search_service(){
	text=document.getElementById("myInput").value;
	
	if (text===""){
		text=undefined;
	}

	ServiceFiltering();
}


////////////////////////////////////////////////////////////////////////////


categories()
function categories(){
	var category=document.querySelectorAll(`input[name="category"]:checked`);
	
//	if (category[0]){
//		service_type=category[0].value;
//	}

//	else {
//		service_type=undefined;
//	}
//	ServiceFiltering();
//}

	var categories_arr=[];

	for (var i=0; i<category.length; i++){
		categories_arr.push(category[i].value);
	}

	if (categories_arr===[]){
		service_type=undefined;
	}

	else{
		service_type=categories_arr.toString();
	}
	ServiceFiltering();

}

////////////////////////////////////////////////////////////////////////////


function group_filter() {
	var list = document.querySelectorAll(`input[name="group"]:checked`);
	var group_ids_arr =[];

	for(var i=0; i<list.length; i++){
		group_ids_arr.push(list[i].value);
	}

	if(group_ids_arr===[]){	
		group_ids_string=undefined;
	}

	else{
		group_ids_string=group_ids_arr.toString();
	}

	ServiceFiltering();
}


////////////////////////////////////////////////////////////////////////////
