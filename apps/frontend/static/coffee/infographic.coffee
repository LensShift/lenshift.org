@InfographicController =
  extends: BaseController
  props: ['infographic_id']
  template: '#infographic_template'
  components:
    'section': SectionController
  data:
    sections: []
  computed:
    infographic: ->
      infographic_promise = new Promise (resolve, reject) =>
        $.ajax
          url: "/api/infographics/#{@infographic_id}",
          dataType: 'json'
          success: (response) ->
            resolve(response)
          error: ->
            reject()

      infographic_promise.then (response) ->
        @sections = response.sections
