$(document).ready(function() {
    setInterval(function() {
        $.ajax({
            url: '',
            type: 'get',
            contentType: 'application/json',
            success: function(response) {

                $('#chat-content').html('')

                console.log('[DEBUG] response.lines: ' + response.lines)

                for (const [user, msg] of Object.entries(response.lines)) {

                    console.log('[DEBUG] user: ' + user)
                    console.log('[DEBUG] msg: ' + msg)

                    $('.chat-body').append(
                        '<p><span class="user">' + user + ': </span>' +
                        '<span class="msg">' + msg + '</span></p>\n'
                    )

                }
            }
        })
    }, 100)
})
