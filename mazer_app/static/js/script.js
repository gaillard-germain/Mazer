var hidden = true;

$('#solution').on('click', function(event) {
  if (hidden) {
    hidden = false;
    $(this).val('Cacher solution');
    $('.path').addClass('highlight').removeClass('corridor');
  } else {
    hidden = true;
    $(this).val('Voir solution');
    $('.path').addClass('corridor').removeClass('highlight');
  }
});

$('form').on('submit', function(event) {
  if (!hidden) {
    hidden = true;
    $('#solution').val('voir solution');
  }
  $.ajax({
    url: '/gen',
    data: {
      seed: $('#seed').val(),
      width: $('#width').val(),
      height: $('#height').val()
    },
    type: 'POST'
    })
  .done(function(data) {
    if ($('#maze').has('svg')) {
      $('#maze svg').remove();
    }
    $('#maze').append(data);
  });
  event.preventDefault();
  event.stopPropagation();
});
