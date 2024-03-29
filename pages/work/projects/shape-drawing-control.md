---
title: ShapeDrawingControl
slug: shape-drawing-control
template: project.html.tmpl
links:
  # Once this goes offline, use archive.org: https://web.archive.org/web/20150920172034/https://developer.mapquest.com/documentation/javascript-api/controls/
  - url: https://developer.mapquest.com/documentation/javascript-api/controls#drawingcontrol
    text: ShapeDrawingControl documentation
summary: MapQuest's JavaScript API for user-drawn shapes
---

My first major project at MapQuest was the ShapeDrawingControl, a map control
that lets users define geographical areas by drawing shapes on a map.

I began by assessing the existing code's state. Someone had
started on it in the past, but no one knew how close it was to
completion.

The existing code turned out to be a proof-of-concept broken by code drift.
It extended the ShapeOverlay classes with drag handles, but was buggy,
crash-prone, and did not work at all in IE 8, one of the targeted browsers.

While assessing the ShapeDrawingControl's state, I discovered
several issues with underlying code.

The Maps API has three different graphics engines
([VML](http://en.wikipedia.org/wiki/Vector_Markup_Language),
[SVG](http://en.wikipedia.org/wiki/Scalable_Vector_Graphics),
and [canvas](http://en.wikipedia.org/wiki/Canvas_element)),
and loads the correct one based on browser support.

Those three engines had huge swathes of duplicate logic, and past
maintainers had not kept them in sync. Each one had bugs not
present in the others (though some bugs were common to all
three).

Thus, I extracted the common code in the three engines
into a base graphics engine, then fixed the bugs I had
found.

I re-engineered the proof-of-concept for robustness and
correctness, and added support for IE 8.

I suggested, designed, and implemented several new features,
including the shape movement and deletion tools.

I wrote Jasmine specs for the new features, and wrote
documentation about the control for developer.mapquest.com.

Try the embedded demo below. It shows the control's built-in
behavior. A real website would use the control's events to do
something useful, like filtering search results with the
drawn shapes.

<div id="map" style="width: 600px; height: 600px;"></div>
<script src="http://open.mapquestapi.com/sdk/js/v7.2.s/mqa.toolkit.js?key=Fmjtd%7Cluu829u12h%2C8x%3Do5-947nur"></script>
<script type="text/javascript">
MQA.EventUtil.observe(window, 'load', function() {
    var options = {
        elt: document.getElementById('map'),
        zoom: 18,
        latLng: { lat: 40.052498, lng: -76.313839 }
    };

    window.map = new MQA.TileMap(options);
    MQA.withModule('shapedrawingcontrol', 'mousewheel', function() {
        map.addControl(new MQA.ShapeDrawingControl({
                color: '#000000',
                colorAlpha: 0.5,
                fillColor: '#000000',
                fillColorAlpha: 0.5,
                borderWidth: 2
            }),
            new MQA.MapCornerPlacement(MQA.MapCorner.TOP_LEFT,
                                       new MQA.Size(5,5))
        );

        map.enableMouseWheelZoom();
    });
});
</script>
