var map;
var poly;
var path;
var infowindow;
var autocomplete;
var follow_vehicle=0;
var uid;
var markersarr = {};
var vehicles = {};
var vehicle_id= -1;
var route_data;
var routearr={};
var route_count=0;
var poly_arr={};
var socket;
var colour_arr=["#00AD00","#6E9991","#0A1AA3","#FFA35C","#38332E","#26E8A1","#e37edb"];



var map_style =[{"featureType":"landscape","stylers":[{"hue":"#F1FF00"},{"saturation":-27.4},{"lightness":9.4},{"gamma":1}]},{"featureType":"road.highway","stylers":[{"hue":"#0099FF"},{"saturation":-20},{"lightness":36.4},{"gamma":1}]},{"featureType":"road.arterial","stylers":[{"hue":"#00FF4F"},{"saturation":0},{"lightness":0},{"gamma":1}]},{"featureType":"road.local","stylers":[{"hue":"#FFB300"},{"saturation":-38},{"lightness":11.2},{"gamma":1}]},{"featureType":"water","stylers":[{"hue":"#00B6FF"},{"saturation":4.2},{"lightness":-63.4},{"gamma":1}]},{"featureType":"poi","stylers":[{"hue":"#9FFF00"},{"saturation":0},{"lightness":0},{"gamma":1}]}];
    geolocation_marker = new google.maps.Marker({
                icon: {
                    url: 'static/images/geolocation-bluedot.png',
                    size: new google.maps.Size(17, 17),
                    origin: new google.maps.Point(0, 0),
                    anchor: new google.maps.Point(8, 8)
                },
                map: null,
                position: new google.maps.LatLng(0, 0)
     });


function init()
{


socket = io.connect('http://localhost:3000');

/*	socket.on('connect', function(data){
   });

   socket.on('reconnecting', function(data){
   });
*/
   socket.on('realtime', function (data) {
   	console.log(data);
  updatevehicle(data);
  if(data.trip_id==vehicle_id)
  {
  angular.element("#hideclick").scope().updateFn(data.det);
 	if(follow_vehicle==1)
 	follow(data.position);

  }

   });

    createmap();
    /*Load dashbord div on Right Top of the Map*/
    map.controls[google.maps.ControlPosition.RIGHT_TOP].push(document.getElementById('hideclick'));
     map.controls[google.maps.ControlPosition.LEFT_TOP].push(document.getElementById('left-panel'));
    document.getElementById("hideclick").style.display="none"; 
}


/*Create Google Map*/
function createmap()
{

	map_canvas = document.getElementById("map-canvas");
	var myOptions = 
	{
			center : new google.maps.LatLng(8.6033,77.0028),
			zoom : 11,
			mapTypeId : google.maps.MapTypeId.ROADMAP,
			streetViewControl: false,
			mapTypeControl: false,
			panControl: false,
			scaleControl: false,
	};

	map = new google.maps.Map(map_canvas, myOptions);
	infowindow = new google.maps.InfoWindow({
             content: 'holding...'
        });	

}

/*Function to update vechicle status and marker realtime*/
function updatevehicle(data)
{
	var point = new google.maps.LatLng(data.position.lat, data.position.lng);
	uid = data.trip_id;

	/*If uid not present in marker array Create new Vehicle else update the corresponding vehicle*/
	if(!(uid in markersarr))
		vehicles[uid] = createvehicle(data,point);
	else
	{
		vehicles[uid].contentinfo = data.emp;
		markersarr[uid].animateTo(point,{  
			easing : "linear",
			duration : 1000,
			complete : function(){

			}
		});
	}
	path = vehicles[uid].polyline.getPath();
	path.push(point);
}

/*Function for creating a new vehicle*/
function createvehicle(data,point)
{

		var image = 'bus.png';
		var	newmarker = new google.maps.Marker({
				position : point,
				map : map,
				id : uid,
				icon : image
			});
	
		/*Title Shows while mousehover to the vechile */
		newmarker.setTitle(data.det.trip_id);
		markersarr[uid]=newmarker;
	
	
 	 	google.maps.event.addListener(markersarr[uid], 'click', function() 
 	 	{
 	 		if(vehicle_id!==this.id && vehicle_id!==-1)
 	 		{
 	 			document.getElementById("show_btn").value="Show Route";
			     hide_route(vehicle_id);
 	 		}
	
 	 	   	vehicle_id=this.id;
 	 		socket.emit('click',vehicle_id);
 	    	document.getElementById('hideclick').style.display = "block";
 	    	
 	    	/*To stop following previous vechicle*/
 	    	 follow_vehicle=0;
			document.getElementById("follow_btn").value="Follow";
 	 	});
 	

 	 	 /*Poly is the polyline used to show the real time route of the vehicle*/
 	  	   var polyOptions = {
			   strokeColor: '#c0392b',
			   strokeOpacity: 1,
			   strokeWeight: 4 ,
			    zIndex: 150 
			};	
	
		  poly = new google.maps.Polyline(polyOptions);
 		  poly.setMap(map);
 			

 			if(uid in poly_arr)
 			{
 					polyline2=poly_arr[uid];
 			}
 			else
 			{
			 		/*Load static route of the vehicle while creating a new vehicle*/	
		//	 		 route_data=load_route(data.det.trip_id);
			 		
			 		/*Polyline 2 represent static route of the Vehicle*/
			 		  var polyline2 = new google.maps.Polyline({
					     path: [],
					     strokeColor: colour_arr[getRandomInt()],
					     strokeWeight: 4,
					     strokeOpacity: 1,
					     zIndex: 10 
						});
			
//comment
			/*			    
			   	     for(var i in route_data.routes)
			   	     {
			   	       var cord = new google.maps.LatLng(route_data.routes[i].shape_pt_lat,route_data.routes[i].shape_pt_lng);
			   	       polyline2.getPath().push(cord);
			       	  }
			 
			*/
			 }
				
 		return {
			uid : uid,
			marker : newmarker,
			contentinfo : data.emp,
			headingTo : uid,
			polyline:poly,
			route : polyline2	
	   	}

}


/*Loads route of the vehicle vech_id*/
function load_route(vech_id)
{
	console.log(vech_id);
  $.ajax({
      type: 'POST',
      url: 'http://54.89.248.120:1337/route/findbyid',
      data: {"trip_id":vech_id},
      async: false,
      dataType: 'json',
      success: function(data)
      { 
      			route_data=data;    			
      },
      error: function()
       {
       		console.log("route load error");
       		route_data=-1; 
       }
    });
  return route_data;
    
}


function close_details()
{
	  follow_vehicle=0;
	  document.getElementById("hideclick").style.display="none"; 
	  document.getElementById("follow_btn").value="Follow";
	  document.getElementById("show_btn").value="Show Route";
	  vehicles[vehicle_id].route.setMap(null);
}



function follow(position)
{
	 map.setCenter(new google.maps.LatLng(position.lat,position.lng));
	 
}

function follow_toggle()
{	
		if(document.getElementById("follow_btn").value==="stop")
		{
			follow_vehicle=0;
			document.getElementById("follow_btn").value="Follow";
		}
		else
		{
			follow_vehicle=1;
			document.getElementById("follow_btn").value="stop";
			if(map.getZoom() < 15)
	 	       map.setZoom(15);
		}
}

/*Function to show and hide routes*/
function route_toggle()
{
	if(document.getElementById("show_btn").value==="Show Route")
	{
		document.getElementById("show_btn").value="Hide Route";
		show_route(vehicle_id);
	}
	else
	{
		document.getElementById("show_btn").value="Show Route";
		hide_route(vehicle_id);
	}
}

/*to generate*/
var randCount = -1;
function getRandomInt() {
	randCount++;
	if(colour_arr.length === randCount)
		randCount = 0;
	return randCount;
}

function showall_route()
{
	for(var i in markersarr)
				show_route(i);
}

function hideall_route()
{
	for(var i in markersarr)
				hide_route(i);
}
		
function show_route(id)
{
	vehicles[id].route.setMap(map);
}

function hide_route(id)
{
	vehicles[id].route.setMap(null);
}

function reset()
{
	 follow_vehicle=0;
	  document.getElementById("hideclick").style.display="none"; 
	  document.getElementById("follow_btn").value="Follow";
	  document.getElementById("show_btn").value="Show Route";
	  for(i in poly_arr)
	  		poly_arr[i].setMap(null);
}


function submit_search()
{
	var vid=$("#search_trip option:selected").text();
	console.log(vid);
				if(vid in markersarr)
      			{
      				poly_arr[vid]=vehicles[vid].route;
      				poly_arr[vid].setMap(map);
      			}
      			else if(vid in poly_arr)
      			{
      				poly_arr[vid].setMap(map);
      			}
      			else
      				disp_route(vid);
    /*var fr =document.getElementById("from_stop").value;
    var to =document.getElementById("to_stop").value;
    var vh =document.getElementById("vehicle_input").value;

    var jdata={"source":fr,"destination":to,"Vehicle_id":vh};
    console.log(jdata);
	  $.ajax({
      type: 'POST',
      url: 'http://54.89.248.120:1337/trips/findAlltrips',
      data: jdata,
      async:false,
      dataType: 'json',
      success: function(data)
      { 
      		for(var i in data)
      		{
      			
      			var vid=data[i].trip_id;
      			if(vid in markersarr)
      			{
      				poly_arr[vid]=vehicles[vid].route;
      				poly_arr[vid].setMap(map);
      			}
      			else if(vid in poly_arr)
      			{
      				poly_arr[vid].setMap(map);
      			}
      			else
      				disp_route(vid);
      		}
      },
      error: function()
      {
       		console.log("could not retrieve requested route");
       }
    });
*/
}

function disp_route(vech_id)
{
	/*Load static route of the vehicle while creating a new vehicle*/	
 		 route_data=load_route(vech_id);
 		
 		/*Polyline 2 represent static route of the Vehicle*/
 		  var polyline2 = new google.maps.Polyline({
		     path: [],
		     strokeColor: colour_arr[getRandomInt()],
		     strokeWeight: 4,
		     strokeOpacity: 1,
		     zIndex: 10 
			});
			    
   	     for(var i in route_data.routes)
   	     {
   	       var cord = new google.maps.LatLng(route_data.routes[i].shape_pt_lat,route_data.routes[i].shape_pt_lng);
   	       polyline2.getPath().push(cord);
       	  }
       	  polyline2.setMap(map);
       	  poly_arr[vech_id]=polyline2;
}

