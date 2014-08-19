
/*Anular app for updating dashbord Realtime*/

var app = angular.module('details',['ui.bootstrap']);
app.controller('DetailsController',function($scope,$log,$http)
{
   $scope.empList={};
   $scope.updateFn=function(data)
   {
     $scope.empList=data;
     $scope.$digest();
   };


   // Data for select in panel dashboard
   $scope.tripData = [];
   $scope.findAlltrips = function(){
	   $http.get("http://54.89.248.120:1337/trips/findAlltrips")
	   		.success(function(data){
	   			$scope.tripData = data;
	   		});
   	};
   	$scope.findAlltrips();

   	$scope.changeModel = function(){
   		
   		$log.info($scope.searchTrip);
   		$scope.tripData.forEach(function(data){
   			if(data.trip_id === $scope.searchTrip)
   				$scope.item = data;
   		});
   	};
   	$scope.resetFn =function(){
   		$scope.item={};
   		$scope.searchTrip ={};
   	}
 });
