angular.module('account.client', ['ui.router', 'ngTable'])
.config(function ($stateProvider, $interpolateProvider, $urlRouterProvider) {
      //allow django templates and singular to co-exist
      $interpolateProvider.startSymbol('[[');
      $interpolateProvider.endSymbol(']]');

      $urlRouterProvider
      .when('/institution','/institution/details')
      .otherwise('/home');

      $stateProvider
      .state('home', {
        url: '/home',
        templateUrl: 'client/dashboard.html'
      })
      .state('editprofile', {
        url: '/editprofile',
        templateUrl: 'client/client_edit_profile.html'
      })
      .state('leads', {
        url: '/leads',
        templateUrl: 'client/leads.html',
        controller: 'EnquiryTableCtrl'
      })

      .state('institution', {
        url: '/institution',
        templateUrl: 'client/institution/' //This is template only to do angular routing
        //controller: 
      })
      .state('institution.details', {
        url: '/details',
        templateUrl: 'client/details.html',
      })
      .state('institution.academic', {
        url: '/academic',
        templateUrl: 'client/academic_details.html',
      })
      .state('institution.photos', {
        url: '/photos',
        templateUrl: 'client/photos.html',
      })
      .state('institution.videos', {
        url: '/videos',
        templateUrl: 'client/videos.html',
      });

    })

.controller("ListCtrl", function($scope) {
  $scope.shoppingList = [
  {name: 'Milk'},
  {name: 'Eggs'},
  {name: 'Bread'},
  {name: 'Cheese'},
  {name: 'Ham'}
  ];

  $scope.selectItem = function(selectedItem) {
    _($scope.shoppingList).each(function(item) {
      item.selected = false;
      if (selectedItem === item) {
        selectedItem.selected = true;
      }
    });
  };
})


.controller('InstRouteCtrl', ['$scope', '$stateParams', function($scope, $stateParams) {
    $scope.templateUrl = 'client/institution/'+ $stateParams.id+'/';
}])

.controller('EnquiryTableCtrl', function($scope, $filter, $http, ngTableParams) {

            $scope.tableParams = new ngTableParams({
                page: 1,            // show first page
                count: 10,          // count per page
                sorting: {
                    name: 'asc'     // initial sorting
                }
            }, {
               // total: data.length, // length of data
                getData: function($defer, params) {
                    // use build-in angular filter
                    $http.get('enquiries/api/').success(function(data) {
                      console.log(data[0].institution_interested);
                      console.log(data[0].institution_interested[0]);
                    var orderedData = params.sorting() ?
                                        $filter('orderBy')(data, params.orderBy()) :
                                        data;

                    $defer.resolve(orderedData.slice((params.page() - 1) * params.count(), params.page() * params.count()));
                });
                }
            });
});
