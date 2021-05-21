$( function() {
    $( "#following-range" ).slider({
      range: true,
      values:[1,10000],
      min: 1,
      max: 10000,
      slide: function( event, ui ) {
        $( "#id_following_count__gt" ).val( ui.values[ 0 ]);
        $( "#id_following_count__lt" ).val(ui.values[ 1 ] );
      }
    });
  } );

  $( function() {
    $( "#follower-range" ).slider({
      range: true,
      values:[1,10000],
      min: 9000,
      max: 100000,
      slide: function( event, ui ) {
        $( "#id_follower_count__gt" ).val(ui.values[ 0 ]);
        $( "#id_follower_count__lt").val(ui.values[ 1 ] );
      }
    });
    
  } );