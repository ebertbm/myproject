angular.module('components', [])
 
  .directive('pane', function () {
  return {
    restrict: 'E',
    replace: true,
    transclude: true,
    scope: {},
    controller: function($scope, $element) {
      $scope.templateUrl = '';
      var tabs = $scope.tabs = [];
      var controller = this;
 
      this.selectTab = function (tab) {
        angular.forEach(tabs, function (tab) {
          tab.selected = false;
        });
        tab.selected = true;
      };
 
      this.setTabTemplate = function (templateUrl) {
        $scope.templateUrl = templateUrl;
      };
 
      this.addTab = function (tab) {
        if (tabs.length === 0) {
          controller.selectTab(tab);
        }
        tabs.push(tab);
      };
    },
    template:
      '<div class="row-fluid">' +
        '<div class="row-fluid">' +
          '<div class="nav nav-tabs" ng-transclude></div>' +
        '</div>' +
        '<div class="row-fluid">' +
          '<ng-include src="templateUrl">' +
        '</ng-include></div>' +
      '</div>'
  };
})
.directive('tab', function () {
  return {
    restrict: 'E',
    replace: true,
    require: '^pane',
    scope: {
      title: '@',
      templateUrl: '@'
    },
    link: function(scope, element, attrs, paneController) {
      paneController.addTab(scope);
 
      scope.select = function () {
        paneController.selectTab(scope);
      };
 
      scope.$watch('selected', function () {
        if (scope.selected) {
          paneController.setTabTemplate(scope.templateUrl);
        }
      });
    },
    template:
      '<li ng-class="{active: selected}">' +
        '<a href="" ng-click="select()">{{ title }}</a>' +
      '</li>'
  };
});