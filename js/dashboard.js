		var toggle = false;
    	function fn()
    	{
    		if(!toggle){
    			toggle = true;
	    		$(".sidebar").css("margin-left","0px");
    		}
	    	else{
	    		toggle = false;
	    		$(".sidebar").css("margin-left","-25%");
	    	}

    	}
		var sourcedat=[];
		$.ajax({
		   type:'POST',
		   url: "http://54.89.248.120:1337/stops/findAllstops",
		   dataType: "json",
		   data: {},
		   success: function(data) {
		      console.log(data);
		      sourcedat = $.map(data, function(item) {
		         return {
		            label: item.stop_name
		         };
		      });
		   $("#from_stop").autocomplete({
		      source: sourcedat,
		      minLength: 0
		   });
		    $("#to_stop").autocomplete({
		      source: sourcedat,
		      minLength: 0
		   });
		  
		   }
		});

		var vechdata=[];
		$.ajax({
		   type:'POST',
		   url: "http://54.89.248.120:1337/vehicle/findAllvehicle",
		   dataType: "json",
		   data: {},
		   success: function(data) {
		      vechdata = $.map(data, function(item) {
		         return {
		            label: item.vehicle_id
		         };
		      });
		   $("#vehicle_input").autocomplete({
		      source: vechdata,
		      minLength: 0
		   });
		 
		   }
		});

