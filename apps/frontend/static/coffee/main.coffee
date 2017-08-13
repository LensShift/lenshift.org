@MainController =
  extends: BaseController
  delimiters: ['[[', ']]']
  components:
    'infographic': InfographicController

new Vue(MainController).$mount ".container"
