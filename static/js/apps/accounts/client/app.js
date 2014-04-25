angular.module('account.client', ['ui.router', 'ngTable'])
.config(function ($stateProvider, $interpolateProvider, $urlRouterProvider) {
      //allow django templates and singular to co-exist
      $interpolateProvider.startSymbol('[[');
      $interpolateProvider.endSymbol(']]');

      $stateProvider
      .state('home', {
        url: '/home',
        templateUrl: 'client/dashboard.html'
      })
      .state('editprofile', {
        url: '/editprofile',
        templateUrl: 'client/client_edit_profile.html'
      })
      .state('institution', {
        url: '/institution',
        templateUrl: 'client/institution_edit.html',
        controller: 'ListCtrl'
      })
      .state('list.item', {
        url: '/:item',
        templateUrl: 'templates/list.item.html',
        controller: function($scope, $stateParams) {
          $scope.item = $stateParams.item;
        }
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
});
