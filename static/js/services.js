var start=undefined;
var end=undefined;
var text=undefined;
var service_type=undefined;
var group_ids_string=undefined;


function ServiceFiltering(){
	var select=document.getElementsById('services_available');
	select.innerHTML="";
	const instance=axios.create({
		baseURL: 'https://127.0.0.1:8000',
		timeout: 5000,
	});

	instance.get('/api/servicefilter',{
		params:{
			service=service_type,
			group_ids=group_ids_string,
			start_time=start_time,
			end_time=end_time,
			text=text,
		}
	}).then(
		function(response){
			reply=response.data;
			console.log(reply);

			for (item in reply)
			{
				if(reply[item].is_active==true){
					if(reply[item].service_type in ['Food','Shopping']){
						if(reply[item].is_member==true){
							select.innerHTML += "<li> <div>" +
							"<h4>"reply[item].service_type+" Service</h4>" +
				 			"<h5>" + reply[item].vendor + "</h5>" +
							"<p> by " + reply[item].initiator + "</p>" +
							"<h4><p>Start Time: " + reply[item].start_time + "<br> End Time: " + reply[item].end_time + "</p> </h4>" +
							"<span> " + reply[item].service_desc + "</span>" +
							"<button >Already a member</button>"
							+ " </div> </li>";
						}

						else{
							{#here, reply[item] is our service object, can access fields directly,#}
							select.innerHTML += "<li> <div>" +
							"<h4>"reply[item].service_type+" Service</h4>" +
							"<h5>" + reply[item].vendor + "</h5>" +
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
							"<h4>Event Service</h4>" +
				 			"<h5>" + reply[item].event_type + "</h5>" +
							"<h5>at " + reply[item].location + "</h5>"
							"<p> by " + reply[item].initiator + "</p>" +
							"<h4><p>Start Time: " + reply[item].start_time + "<br> End Time: " + reply[item].end_time + "</p> </h4>" +
							"<span> " + reply[item].service_desc + "</span>" +
							"<button >Already a member</button>"
							+ "</div> </li>";
						}

						else{
							{#here, reply[item] is our service object, can access fields directly,#}
							select.innerHTML += "<li><div>" +
							"<h4>Event Service</h4>" +
							"<h5>" + reply[item].event_type + "</h5>" +
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
							"<h4>Travel Service</h4>" +
				 			"<h5>via " + reply[item].travel + "</h5>" +
							"<h4><p>From: " + reply[item].start_point + "<br> To: " + reply[item].end_point + "</p></h4>"
							"<p> by " + reply[item].initiator + "</p>" +
							"<h4><p>Start Time: " + reply[item].start_time + "<br> End Time: " + reply[item].end_time + "</p> </h4>" +
							"<span> " + reply[item].service_desc + "</span>" +
							"<button >Already a member</button>"
							+ "</div> </li>";
						}

						else{
							{#here, reply[item] is our service object, can access fields directly,#}
							select.innerHTML += "<li><div>" +
							"<h4>Travel Service</h4>" +
							"<h5>" + reply[item].travel + "</h5>" +
							"<h4><p>From: " + reply[item].start_point + "<br> To: " + reply[item].end_point + "</p></h4>"
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
	var btn=getElementsById(service_id);

	if(btn.innerHTML=='Already a member'){
		alert("You are already a member of this service")
	}

	if(btn.innerHTML=='Join Service'){
	axios.put('/api/addservicemember/',{
		params:{
			id=service_id,
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
	else if ( end==undefined || end=="" ){
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
	service_type = String(c);
	if (service=="all"){
		service=undefined;
	}
	ServiceFiltering();
}

function group_filter(){
	var list = document.getElementsByClassName("grp");
	group_ids_string = ""

	for(var i=0; i<list.length; i++){
		group_ids_string += String(list[i].group_id)+" ";
	}

	if(group_ids_string==""){
		group_ids_string=undefined;
	}

	ServiceFiltering();
}
