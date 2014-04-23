angular.module('account.student', ['ui.router', 'ngTable'])
.config(function ($stateProvider, $interpolateProvider, $urlRouterProvider) {
      //allow django templates and singular to co-exist
      $interpolateProvider.startSymbol('[[');
      $interpolateProvider.endSymbol(']]');

/*      var settings = {
        name: 'settings',
        url: '/settings',
        templateUrl: '/student_edit_profile.html'
      };
*/

      var studentProfile = {
        name: 'studentEditProfile',
        url: '/editprofile',
        templateUrl: 'student_edit_profile.html',
        controller: 'StudentController'
      };


      var studentEnquiries = {
        name: 'studentenquiries',
        url: '/messages',
        templateUrl: 'student_enquiries.html',
        controller: 'DemoCtrl'
      };

      var changePassword = {
        name: 'changePassword',
        url: '/password',
        templateUrl: '../password/change/'
        };


      $stateProvider
      .state(studentProfile)
      .state(changePassword)
      .state(studentEnquiries);
    })

.controller('StudentController', function ($scope, $http) {
  $http.get('profile/api/').success(function(data) {
    $scope.student = data;
    console.log(data.about_me);
  });

})


 .controller('EnquiryController', function ($scope, $http) {
  $http.get('enquiries/api/').success(function(data) {
    $scope.enquiries = data;
    console.log(data[0].content);
  });



})

.controller('DemoCtrl', function($scope, $filter, $http, ngTableParams) {

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
