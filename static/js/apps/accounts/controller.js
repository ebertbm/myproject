
angular.module('account.student', ['ui.router'])
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
        templateUrl: 'student_enquiries.html'
      };


      $stateProvider
      .state(studentProfile)
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
    console.log(data);
  });

});