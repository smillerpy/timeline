var Timeline = Backbone.Collection.extend({
  url: '/timeline/api/v1/timeline_card/',
  parse: function(response) {
          this.recent_meta = response.meta || {};
          return response.objects || response;
      }
});

var TimelineView = Backbone.View.extend({
      el: '.timeline_timeline',
      initialize: function(options) {
        this.options = options;
        _.bindAll(this, 'render');
        this.full = false;
        this.type_filter = undefined
        this.render();
      },
      clean_all: function(options){
        this.$el.children().remove();
        this.offset = 0;
        this.options = options;
        _.bindAll(this, 'render');
        this.full = false;
        this.render();
      },
      set_filter_type: function(event_type){
          this.type_filter = event_type != '' ? event_type : undefined;
          this.clean_all();
      },
      load_more: function(){
        this.render();
      },
      render_results: function (instance){
        var that = instance;
        var _render = function (timeline_coll) {
          if (timeline_coll.models.length > 0){
            that.limit = timeline_coll.recent_meta.limit;
            that.offset = timeline_coll.recent_meta.offset + that.limit;
            _(timeline_coll.models).each(function(item, index) {
              var template = _.template($('#'+item.get('template')).html());
              that.$el.append(template({'event_card': item}));
            });
          }else{
              if (timeline_coll.recent_meta.is_generating_timeline){
                  setTimeout(that.clean_all, 4000);
              }else{
                  var template = _.template($('#no_more_events').html());
                  that.$el.append(template({}));
                  that.full = true;
              }
          }
          if (!timeline_coll.recent_meta.is_generating_timeline){
              $('#tl-loader').hide()
          }
          that.rendering=false;
        };
 
        return _render;
      },
      render: function () {
        if (this.rendering) { return this}
        this.rendering=true;
        $('#tl-loader').show()
        var timeline_model = new Timeline();
        filters = {}
        filters.contact_id = CONTACT_ID;
        if (this.type_filter){
            filters.type = this.type_filter;
        }
        if (this.offset){
          filters.offset = this.offset;
          filters.limit = this.limit;
        }
        timeline_model.fetch({
          data: filters,
          processData: true, 
          success: this.render_results(this)
        });
        return this;
      }
    });

var timeline_view;
$( document ).ready(function() {
    timeline_view = new TimelineView({});
});

$(window).scroll(function(event){
  if ((timeline_view.full == false) && (timeline_view.rendering == false) && ($(window).scrollTop() + $(window).height() > $(document).height() - 100)){
      timeline_view.load_more();
   }
});


