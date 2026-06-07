$(document).ready(function() {
    setInterval(function() {
        $.ajax({
            url: '',
            type: 'get',
            contentType: 'application/json',
            success: function(response) {

                $('#chat-content').html('')

                console.log('[DEBUG] response.lines: ' + response.lines)

                for (line of response.lines) {
                    let user = line[0]
                    let msg = line[1]

                    console.log('[DEBUG] user: ' + user)
                    console.log('[DEBUG] msg: ' + msg)

                    $('.chat-body').append(
                        '<span><span class="user">' + user + ': </span>' +
                        '<span class="msg">' + msg + '</span></span>\n'
                    )

                }
            }
        })
    }, 1000)
})
