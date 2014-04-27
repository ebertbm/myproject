angular.module('account.client', ['ui.router', 'ngTable', 'ngTableExport'])
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
        templateUrl: 'client/institution/'
        //controller: 
      })
      .state('institution.details', {
        url: '/details',
        templateUrl: 'client/details.html'
      })
      .state('institution.contact', {
        url: '/contact',
        templateUrl: 'client/contact_details.html'
      })
      .state('institution.academic', {
        url: '/academic',
        templateUrl: 'client/academic_details.html'
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


.controller('EnquiryTableCtrl', function($scope, $filter, $http, ngTableParams, $sce) {

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
                    $http.get('institution_enquiries/api/').success(function(data) {
                      console.log(data);
                    var orderedData = params.sorting() ?
                                        $filter('orderBy')(data, params.orderBy()) :
                                        data;

                    $defer.resolve(orderedData.slice((params.page() - 1) * params.count(), params.page() * params.count()));
                });
                }
            });
});
