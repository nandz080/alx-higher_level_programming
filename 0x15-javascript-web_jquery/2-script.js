$('DIV#red_header').on('click keypress', function (event) {
    // Check if the event is a mouse click or the Enter key (key code 13)
    if (event.type === 'click' || (event.type === 'keypress' && event.which === 13)) {
        $('header').css('color', '#FF0000');
    }
});

