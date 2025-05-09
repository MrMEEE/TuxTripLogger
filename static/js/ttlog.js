$('#logoutModal form').on('submit', function (e) {
    e.preventDefault(); // Prevent the default form submission

    const csrfToken = $('input[name="csrfmiddlewaretoken"]').val(); // Get the token from the form

    $.ajax({
        url: $(this).attr('action'),
        type: 'POST',
        headers: {
            'X-CSRFToken': csrfToken
        },
        success: function (response) {
            // Redirect or handle success
            window.location.href = '/';
        },
        error: function (xhr) {
            // Handle error
            alert('Logout failed. Please try again.');
        }
    });
});