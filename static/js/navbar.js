$(document).ready(function() {
    $('.navbar-icon').click(function() {
      $('.dropdown-menu').toggleClass('show');
    });
    $('.dropdown-menu').click(function(event) {
      event.stopPropagation();
    });
    $(document).click(function(event) {
      if (!$(event.target).closest('.navbar-icon').length) {
        $('.dropdown-menu').removeClass('show');
      }
    });
  });   